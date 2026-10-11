"""One aggregate participant, one Lifecycle backend, one publication assignment."""

from dataclasses import dataclass, field
from .history import (
    FieldHistory,
    FrameRecord,
    NodeHistory,
    HistoryEpoch,
    PublishedSelection,
    PreparedCommit,
    immutable,
)
from .values import normalize, decode, project_working
from .errors import TransactionRequiredError, UnavailableNodeError, ForeignManagerError
from .states import Setup, Idle, Editing, Completing, Faulted
from .callbacks import call, capture, dispatch, require_mutation
from .graph import traverse
from .policies import RaiseAbsent, ReadLastVisible
from .snapshots import FrameSnapshot
from .errors import ObjectAbsentError, HistoryFaultError, ReentrantOperationError
from .candidates import CandidateRead
from yidl_lifecycle.transaction_yidl import DEFAULT_TRANSACTION, GroupTransactionManager


@dataclass(slots=True)
class EditOverlay:
    base: PublishedSelection
    token: object
    roots: list
    touched: dict = field(default_factory=dict)
    transient: dict = field(default_factory=dict)
    provisional: set = field(default_factory=set)


class Aggregate:
    def __init__(self, manager):
        self.manager = manager

    def commit_order_key_for(self, key):
        return ()

    def requires_validation_for(self, key):
        return False

    def _prepare_commit_tx_by_key(self, key, token):
        m = self.manager
        m._state = Completing()
        m._prepared = m._prepare()

    def _apply_prepared_commit_tx_by_key(self, key, token):
        m = self.manager
        m._selection = m._prepared.selection
        m._installed_selection = m._selection
        m._installed_token = token

    def _rollback_tx_by_key(self, key, token):
        m = self.manager
        m._edit = None
        m._prepared = None

    def _after_commit_tx_by_key(self, key, token):
        self._rollback_tx_by_key(key, token)
        self.manager._state = Idle()

    def _after_rollback_tx_by_key(self, key, token):
        self.manager._state = Idle()


class UndoRedoManager:
    def __init__(self, *, tx_key=DEFAULT_TRANSACTION, absent_policy=None):
        self._callback_depth = 0
        self._state = Setup()
        dispatch(self, "transaction key hashing", lambda: hash(tx_key))
        self._tx_key = tx_key
        self._absent_policy = RaiseAbsent() if absent_policy is None else absent_policy
        if type(self.absent_policy) not in (RaiseAbsent, ReadLastVisible):
            raise TypeError("unsupported absent policy")
        self._selection = None
        self._nodes = {}
        self._next_node_id = 1
        self._next_frame_id = 1
        self._backend = GroupTransactionManager(tx_key)
        self._aggregate = Aggregate(self)
        self._edit = None
        self._prepared = None
        self._fault_reason = None
        self._confirmed_selection = True
        self._installed_selection = None
        self._installed_token = None
        self.last_completion = None

    @property
    def tx_key(self):
        return self._tx_key

    @property
    def absent_policy(self):
        return self._absent_policy

    def _key(self, key):
        def check():
            if key != self.tx_key:
                raise RuntimeError(f"unknown transaction key {key!r}")

        self._call("transaction key comparison/diagnostic", check)

    def _allocate_node(self):
        if isinstance(self._state, (Completing, Faulted)):
            require_mutation(self)
        if self._selection is not None and self._edit is None:
            raise TransactionRequiredError(
                "construction requires an active transaction"
            )
        result = self._next_node_id
        self._next_node_id += 1
        return result

    def _register(self, state):
        def check_keys():
            for fact in state.schema.fields:
                if (
                    fact["field_kind"] in ("managed", "transient")
                    and fact["tx_key_key"] != self.tx_key
                ):
                    raise RuntimeError(
                        f"{state.schema.name}.{fact['field_name']}: wrong transaction key"
                    )
            for name, key in state.schema.validators:
                self._key(key)

        self._call(f"{state.schema.name}: registration keys", check_keys)
        self._nodes[state.node_id] = state
        if self._edit:
            state.provisional = self._edit.token
            self._edit.provisional.add(state.node_id)

    def _available(self, state):
        if state.manager is not self:
            raise ForeignManagerError("node belongs to another manager")
        if self._selection is None:
            return
        if self._edit and state.node_id in self._edit.provisional:
            return
        history = self._selection.epoch.nodes.get(state.node_id)
        if history is None or not any(f <= self.frame_id for f in history.presence):
            raise UnavailableNodeError(
                f"node {state.node_id} has no surviving baseline at frame {self.frame_id}"
            )

    def initialize(self, *roots):
        require_mutation(self)
        if self._selection is not None or not roots:
            raise RuntimeError("initialize exactly once with at least one root")
        for root in roots:
            self._available(root._u_state)
        ids = tuple(dict.fromkeys(root.node_id for root in roots))
        candidate = self._candidate(ids, initial=True)
        nodes = {
            node_id: NodeHistory(
                self._nodes[node_id].schema,
                immutable(
                    {
                        name: FieldHistory((0,), (value,))
                        for name, value in fields.items()
                    }
                ),
                (0,),
            )
            for node_id, fields in candidate.items()
        }
        frame = FrameRecord(0, ids, frozenset(nodes))
        self._selection = PublishedSelection(
            HistoryEpoch(immutable(nodes), (frame,)), 0
        )
        self._state = Idle()

    def _raw_fields(self, node_id):
        state = self._nodes[node_id]
        values = {}
        for fact in state.schema.fields:
            if fact["field_kind"] != "managed":
                continue
            name = fact["field_name"]
            key = (node_id, name)
            if self._edit and key in self._edit.touched:
                value = self._edit.touched[key]
            elif self._selection and node_id in self._selection.epoch.nodes:
                value = (
                    self._selection.epoch.nodes[node_id].fields[name].at(self.frame_id)
                )
            else:
                value = state.values[name]
            values[name] = value
        return values

    def _candidate(self, roots, *, initial=False):
        cache = {}

        def frozen_fields(node_id):
            if node_id in cache:
                return cache[node_id]
            state = self._nodes[node_id]
            fields = {}
            for name, value in self._raw_fields(node_id).items():
                fact = state.schema.by_name[name]
                already_frozen = (
                    not initial
                    and node_id in self._selection.epoch.nodes
                    and (node_id, name) not in self._edit.touched
                )
                if fact["has_freeze"] and not already_frozen:
                    value = self._call(
                        f"{state.schema.name}.{name}: freeze",
                        lambda: fact["freeze"](value),
                    )
                fields[name] = self._call(
                    f"{state.schema.name}.{name}: stable value normalization",
                    lambda: normalize(value, self, f"{state.schema.name}.{name}"),
                )
            cache[node_id] = fields
            return fields

        present = traverse(roots, frozen_fields, self, reject_cycles=True)
        candidate = immutable(
            {node_id: immutable(cache[node_id]) for node_id in sorted(present)}
        )
        pin = CandidateRead(candidate)
        failures = []
        for node_id in sorted(present):
            state = self._nodes[node_id]
            facade = state.facade("default", pin)
            for name, key in state.schema.validators:
                try:
                    result = self._call(
                        f"{state.schema.name}.{name}: candidate validator node {node_id}",
                        lambda: getattr(facade, name)(),
                    )
                    if result is False:
                        raise ValueError(
                            f"{state.schema.name}.{name}: validator returned False at node {node_id}"
                        )
                except BaseException as exc:
                    failures.append(exc)
        if failures:
            raise BaseExceptionGroup("undoable candidate validation failed", failures)
        return candidate

    def begin(self, tx_key=DEFAULT_TRANSACTION):
        require_mutation(self)
        self._key(tx_key)
        self._state.require_initialized()
        owner = capture(self)
        token = None
        try:
            token = dispatch(self, "backend begin", lambda: self._backend.begin(tx_key))
            if owner.edit is None:
                self._edit = EditOverlay(
                    owner.selection, token, list(owner.selection.frame.roots)
                )
                dispatch(
                    self,
                    "backend enlist",
                    lambda: self._backend.enlist(self._aggregate, tx_key),
                )
            original_commit, original_rollback = (
                token._scope_commit,
                token._scope_rollback,
            )
            dispatch(
                self,
                "wrapper scope binding",
                lambda: token.bind_scope(
                    commit=lambda: self._scope_complete(original_commit, token),
                    rollback=lambda: self._scope_complete(original_rollback, token),
                ),
            )
            if (
                self._backend.active_transaction is not token
                or self._backend.begin_count != owner.begin_count + 1
                or (owner.token is not None and token is not owner.token)
                or self._selection is not owner.selection
                or self._state is not owner.state
                or self._edit is None
                or self._edit.token is not token
                or (owner.edit is not None and self._edit is not owner.edit)
            ):
                raise HistoryFaultError("begin setup lost its original ownership")
        except BaseException as setup_failure:
            # A rejected key callback before backend acquisition changes nothing,
            # including a previously joined edit. Later setup failures must close.
            if (
                isinstance(setup_failure, ReentrantOperationError)
                and token is None
                and owner.intact(self)
            ):
                raise
            self._abort_begin_setup(owner, token, setup_failure)
            raise
        self._state = Editing()
        return token

    def _abort_begin_setup(self, owner, returned_token, setup_failure):
        active = self._backend.active_transaction
        token = returned_token if returned_token is not None else owner.token
        if token is None:
            token = active
        failures = [setup_failure]
        owned = (
            token is not None
            and active is token
            and (owner.token is None or token is owner.token)
            and (owner.token is None or token.tx_id == owner.token_id)
            and token.tx_key is self.tx_key
        )
        no_acquisition = (
            token is None
            and owner.token is None
            and active is None
            and self._backend.begin_count == owner.begin_count == 0
        )
        try:
            if owned:
                try:
                    dispatch(
                        self,
                        "backend setup abort",
                        lambda: self._backend.rollback(self.tx_key),
                    )
                except BaseException as abort_failure:
                    failures.append(abort_failure)
        finally:
            self._edit = None
            self._prepared = None
        completion = None if token is None else token.completion
        self.last_completion = completion
        closed = no_acquisition or (
            owned
            and completion is not None
            and completion.ownership_preserved
            and completion.finalized
            and completion.discard_complete
            and completion.after_actions_complete
        )
        healthy_abort = (
            len(failures) == 1
            and not isinstance(setup_failure, HistoryFaultError)
            and closed
            and self._backend.active_transaction is None
            and self._backend.begin_count == 0
            and self._selection is owner.selection
            and not isinstance(self._state, Faulted)
        )
        if not healthy_abort:
            self._confirmed_selection = self._selection is owner.selection
            self._fault("failed begin setup has incomplete abort/ownership evidence")
            cause = (
                failures[0]
                if len(failures) == 1
                else BaseExceptionGroup("begin setup and abort failed", failures)
            )
            raise HistoryFaultError(self._fault_reason) from cause
        self._state = Idle()

    def _scope_complete(self, callback, token):
        require_mutation(self)
        if self._backend.active_transaction is not token:
            return dispatch(self, "backend stale scope completion", callback)
        return self._complete(callback, token)

    def active_transaction_for(self, tx_key=DEFAULT_TRANSACTION):
        self._key(tx_key)
        return self._call(
            "backend active transaction lookup",
            lambda: self._backend.active_transaction_for(tx_key),
        )

    def commit(self, tx_key=DEFAULT_TRANSACTION):
        require_mutation(self)
        self._key(tx_key)
        return self._complete(
            lambda: self._backend.commit(tx_key), self._backend.active_transaction
        )

    def rollback(self, tx_key=DEFAULT_TRANSACTION):
        require_mutation(self)
        self._key(tx_key)
        return self._complete(
            lambda: self._backend.rollback(tx_key), self._backend.active_transaction
        )

    def _require_edit(self):
        require_mutation(self)
        self._state.require_write()
        if (
            self._edit is None
            or self._backend.active_transaction is not self._edit.token
        ):
            raise TransactionRequiredError(
                "writes require the original active transaction"
            )
        return self._edit

    def _prepare(self, *, preview=False):
        edit = self._edit
        frame_id = self._next_frame_id
        if not preview:
            self._next_frame_id += 1
        cutoff = self.frame_id
        nodes = {}
        for node_id, history in self._selection.epoch.nodes.items():
            presence = tuple(f for f in history.presence if f <= cutoff)
            if presence:
                fields = {
                    name: hist.trim(cutoff) for name, hist in history.fields.items()
                }
                nodes[node_id] = NodeHistory(
                    history.schema, immutable(fields), presence
                )
        candidate = self._candidate(edit.roots)
        for node_id in candidate:
            state = self._nodes[node_id]
            previous = nodes.get(node_id)
            fields = {} if previous is None else dict(previous.fields)
            for fact in state.schema.fields:
                if fact["field_kind"] != "managed":
                    continue
                name = fact["field_name"]
                key = (node_id, name)
                if key not in edit.touched and previous is not None:
                    continue
                value = candidate[node_id][name]
                old = fields.get(name, FieldHistory())
                fields[name] = FieldHistory(
                    old.frame_ids + (frame_id,), old.values + (value,)
                )
            presence = (() if previous is None else previous.presence) + (frame_id,)
            nodes[node_id] = NodeHistory(state.schema, immutable(fields), presence)
        frame = FrameRecord(frame_id, tuple(edit.roots), frozenset(candidate))
        frames = self._selection.epoch.frames[: self.cursor + 1] + (frame,)
        selection = PublishedSelection(
            HistoryEpoch(immutable(nodes), frames), len(frames) - 1
        )
        return PreparedCommit(selection)

    @property
    def cursor(self):
        self._require_confirmed(initialized=True)
        return self._selection.cursor

    @property
    def frame_id(self):
        self._require_confirmed(initialized=True)
        return self._selection.frame.frame_id

    @property
    def frame_count(self):
        self._require_confirmed(initialized=True)
        return len(self._selection.epoch.frames)

    @property
    def roots(self):
        self._require_confirmed(initialized=True)
        ids = self._edit.roots if self._edit else self._selection.frame.roots
        return tuple(self._nodes[n].facade() for n in ids)

    @property
    def current_roots(self):
        self._require_confirmed(initialized=True)
        return tuple(
            self._nodes[n].facade("current") for n in self._selection.frame.roots
        )

    def _present(self, facade):
        if isinstance(facade._u_pin, CandidateRead):
            return facade.node_id in facade._u_pin.fields
        if facade._u_pin is not None:
            epoch, frame_id = facade._u_pin
            return facade.node_id in next(
                f.present for f in epoch.frames if f.frame_id == frame_id
            )
        if self._selection is None:
            return False
        if self._edit and facade._u_view != "current":
            return facade.node_id in self._call(
                "working graph traversal",
                lambda: traverse(
                    self._edit.roots, self._raw_fields, self, reject_cycles=False
                ),
            )
        return facade.node_id in self._selection.frame.present

    def _read_managed(self, facade, name, *, allow_thaw=False):
        self._require_confirmed()
        if isinstance(facade._u_pin, CandidateRead):
            pin = facade._u_pin
            return decode(
                pin.fields[facade.node_id][name],
                lambda n: self._nodes[n].facade(facade._u_view, pin),
            )
        state = facade._u_state
        edit = self._edit
        key = (state.node_id, name)
        if edit and facade._u_view != "current" and facade._u_pin is None:
            provisional = state.node_id in edit.provisional
            if not provisional and not self._present(facade):
                return self._committed_value(facade, name, absent=True)
            if key in edit.touched:
                return self._call(
                    f"{state.schema.name}.{name}: working value projection",
                    lambda: project_working(
                        edit.touched[key],
                        self,
                        facade._u_view,
                        in_place=facade._u_view == "working",
                    ),
                )
            fact = state.schema.by_name[name]
            if allow_thaw:
                if name in state.resolving:
                    from .errors import UndoableDefinitionError

                    raise UndoableDefinitionError(
                        f"{state.schema.name}.{name}: recursive thaw"
                    )
                state.resolving.add(name)
                try:

                    def materialize():
                        value = (
                            project_working(state.values[name], self, "working")
                            if provisional
                            else self._committed_value(facade, name)
                        )
                        return project_working(
                            fact["thaw"](value), self, "working", in_place=True
                        )

                    value = self._call(
                        f"{state.schema.name}.{name}: projection and thaw", materialize
                    )
                finally:
                    state.resolving.remove(name)
                edit.touched[key] = value
                return value
            if provisional:
                return self._call(
                    f"{state.schema.name}.{name}: provisional value projection",
                    lambda: project_working(state.values[name], self, facade._u_view),
                )
        return self._committed_value(facade, name)

    def _committed_value(self, facade, name, *, absent=False):
        pin = facade._u_pin
        if pin is None:
            epoch, frame_id = self._selection.epoch, self.frame_id
            working_present = (
                self._edit is not None
                and facade._u_view != "current"
                and self._present(facade)
            )
            if absent or (
                not working_present
                and facade.node_id not in self._selection.frame.present
            ):
                frame_id = self.absent_policy.resolve(facade.node_id, self._selection)
                pin = (epoch, frame_id)
        else:
            epoch, frame_id = pin
        try:
            history = epoch.nodes[facade.node_id].fields[name]
        except KeyError as exc:
            raise ObjectAbsentError(
                f"node {facade.node_id} absent at frame {frame_id}"
            ) from exc
        return decode(
            history.at(frame_id), lambda n: self._nodes[n].facade(facade._u_view, pin)
        )

    def _write_managed(self, facade, name, value):
        edit = self._require_edit()
        if facade._u_view == "current" or facade._u_pin is not None:
            raise TransactionRequiredError(
                "current facade is read-only for managed fields"
            )
        if facade.node_id not in edit.provisional and not self._present(facade):
            raise ObjectAbsentError(
                f"node {facade.node_id}: absent nodes cannot be edited"
            )
        fact = facade._u_state.schema.by_name[name]
        old = self._read_managed(facade, name, allow_thaw=False)
        equal = self._call(
            f"{facade._u_state.schema.name}.{name}: comparison",
            lambda: (
                old is value if fact["compare"] == "identity" else bool(old == value)
            ),
        )
        if not equal:
            edit.touched[(facade.node_id, name)] = value

    def can_undo(self):
        self._state.require_initialized()
        return self._edit is None and self.cursor > 0

    def can_redo(self):
        self._state.require_initialized()
        return self._edit is None and self.cursor + 1 < self.frame_count

    def _navigate(self, delta):
        require_mutation(self)
        self._state.require_initialized()
        if self._edit is not None:
            raise RuntimeError("navigation requires idle history")
        cursor = self.cursor + delta
        if not 0 <= cursor < self.frame_count:
            return False
        self._selection = PublishedSelection(self._selection.epoch, cursor)
        return True

    def undo(self):
        return self._navigate(-1)

    def redo(self):
        return self._navigate(1)

    def add_root(self, node):
        edit = self._require_edit()
        self._available(node._u_state)
        if node.node_id not in edit.roots:
            edit.roots.append(node.node_id)

    def remove_root(self, node):
        edit = self._require_edit()
        if node._u_state.manager is not self:
            raise ForeignManagerError("root belongs to another manager")
        if node.node_id in edit.roots:
            edit.roots.remove(node.node_id)

    def snapshot(self):
        self._require_confirmed(initialized=True)
        return FrameSnapshot(self._selection.epoch, self._selection.frame)

    def _call(self, context, function):
        return call(self, context, function)

    def _fault(self, reason):
        self._fault_reason = reason
        self._state = Faulted()
        self._edit = None
        self._prepared = None

    def validate(self, tx_key=DEFAULT_TRANSACTION):
        require_mutation(self)
        self._key(tx_key)
        edit = self._require_edit()
        before = self._state
        self._state = Completing()
        try:
            self._prepare(preview=True)
        finally:
            if not isinstance(self._state, Faulted):
                self._state = before

    def _complete(self, callback, token):
        if token is None:
            return dispatch(self, "backend completion", callback)
        before = self._selection
        result, failure = None, None
        try:
            result = dispatch(self, "backend completion", callback)
        except BaseException as exc:
            failure = exc
        completion = token.completion
        if completion is None and self._backend.active_transaction is token:
            if failure is not None:
                raise failure
            return result
        self.last_completion = completion
        intact = self._selection is before or (
            self._installed_token == token.tx_id
            and self._installed_selection is not None
            and self._selection is self._installed_selection
        )
        healthy = (
            completion is not None
            and completion.ownership_preserved
            and completion.finalized
            and completion.after_actions_complete
            and (
                completion.publication_complete
                or (completion.discard_complete and self._selection is before)
            )
            and self._backend.active_transaction is None
            and self._edit is None
            and intact
        )
        if not healthy:
            self._confirmed_selection = intact
            self._fault("backend ownership/publication/cleanup evidence is incomplete")
            raise HistoryFaultError(self._fault_reason) from failure
        self._state = Idle()
        if failure is not None:
            raise failure
        return result

    def _require_confirmed(self, *, initialized=False):
        if not self._confirmed_selection:
            raise HistoryFaultError("published selection integrity is unconfirmed")
        if initialized and self._selection is None:
            raise RuntimeError("history is not initialized")

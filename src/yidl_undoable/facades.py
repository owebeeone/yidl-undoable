"""Shared mechanics behind the matcher-selected generated field accessors."""

from dataclasses import dataclass, field
from .undoable_markers import MISSING, _HAS_DEFAULT_FACTORY
from .errors import UndoableDefinitionError, TransactionRequiredError
from .candidates import CandidateRead


@dataclass(slots=True)
class NodeState:
    manager: object
    node_id: int
    schema: object
    model: type
    inputs: dict = field(default_factory=dict)
    values: dict = field(default_factory=dict)
    constructing: bool = True
    resolving: set = field(default_factory=set)
    facades: dict = field(default_factory=dict)
    provisional: object = None

    def facade(self, view="default", pin=None):
        if pin is None and view in self.facades:
            return self.facades[view]
        view_class = self.model.__undoable_views__[view]
        result = object.__new__(view_class)
        result._u_state, result._u_view, result._u_pin = self, view, pin
        if pin is None:
            self.facades[view] = result
        return result


class RuntimeFacade:
    __slots__ = ("_u_state", "_u_view", "_u_pin")

    def _u_start(self, manager):
        node_id = manager._allocate_node()
        state = NodeState(manager, node_id, self.__undoable_schema__, type(self))
        self._u_state, self._u_view, self._u_pin = state, "default", None
        state.facades["default"] = self
        return state

    def _u_finish(self, state):
        for fact in state.schema.fields:
            self._u_resolve_constructor(fact["field_name"])
        state.constructing = False
        state.manager._register(state)

    def _u_resolve_constructor(self, name):
        state = self._u_state
        if name in state.values:
            return state.values[name]
        if name in state.resolving:
            raise UndoableDefinitionError(
                f"{state.schema.name}.{name}: recursive provider"
            )
        fact = state.schema.by_name[name]
        if fact["field_kind"] == "classvar":
            value = fact["default_value"]
        else:
            value = state.inputs.get(name, _HAS_DEFAULT_FACTORY)
            if value is _HAS_DEFAULT_FACTORY:
                if fact["field_kind"] == "static":
                    value = MISSING
                elif fact["has_default_factory"]:
                    state.resolving.add(name)
                    try:
                        value = self._u_factory(fact, "default")
                    finally:
                        state.resolving.remove(name)
                elif fact["has_default"]:
                    value = fact["default_value"]
                else:
                    raise UndoableDefinitionError(
                        f"{state.schema.name}.{name}: missing required value"
                    )
        if fact["field_kind"] == "binding":
            from .bindings import scalar_binding, map_binding

            validate = map_binding if fact["binding_shape"] == "map" else scalar_binding
            value = state.manager._call(
                f"{state.schema.name}.{name}: binding validation",
                lambda: validate(name, value),
            )
        state.values[name] = value
        return value

    def _u_factory(self, fact, role):
        return self._u_state.manager._call(
            f"{self._u_state.schema.name}.{fact['field_name']}: {role} factory",
            lambda: self._u_factory_unfenced(fact, role),
        )

    def _u_factory_unfenced(self, fact, role):
        state = self._u_state
        provider_names = fact[role + "_factory_param_names"]
        kwargs = {}
        for name in provider_names:
            if name == "self":
                kwargs[name] = self
            elif name == "cls":
                kwargs[name] = state.model
            elif state.constructing:
                kwargs[name] = self._u_constructor_provider(name)
            elif state.schema.by_name[name]["field_kind"] == "initvar":
                kwargs[name] = state.values[name]
            else:
                kwargs[name] = getattr(self, name)
        return fact[role + "_factory"](**kwargs)

    def _u_constructor_provider(self, name):
        value = self._u_resolve_constructor(name)
        if (
            self._u_state.schema.by_name[name]["field_kind"] == "static"
            and value is MISSING
        ):
            try:
                value = getattr(self, name)
            except AttributeError as exc:
                raise UndoableDefinitionError(
                    f"{self._u_state.schema.name}.{name}: lazy constructor provider is unset"
                ) from exc
            if value is MISSING:
                raise UndoableDefinitionError(
                    f"{self._u_state.schema.name}.{name}: lazy constructor provider is unset"
                )
        return value

    @property
    def default(self):
        return self._u_state.facade("default", self._u_pin)

    @property
    def current(self):
        return self._u_state.facade("current", self._u_pin)

    @property
    def working(self):
        return self._u_state.facade("working", self._u_pin)

    @property
    def node_id(self):
        return self._u_state.node_id

    @property
    def transaction_manager(self):
        return self._u_state.manager

    @property
    def present(self):
        return self._u_state.manager._present(self)

    def __eq__(self, other):
        return isinstance(other, RuntimeFacade) and self._u_state is other._u_state

    def __hash__(self):
        return hash((id(self._u_state.manager), self.node_id))

    def _u_baseline(self, name):
        state = self._u_state
        if name not in state.values:
            raise UndoableDefinitionError(
                f"{state.schema.name}.{name}: unresolved constructor field"
            )
        return state.values[name]

    def _u_read_plain(self, name):
        return self._u_baseline(name)

    def _u_write_plain(self, name, value):
        self._u_state.values[name] = value

    _u_read_binding = _u_read_plain

    def _u_write_scalar_binding(self, name, value):
        from .bindings import scalar_binding

        state = self._u_state
        result = state.manager._call(
            f"{state.schema.name}.{name}: binding validation",
            lambda: scalar_binding(name, value),
        )
        state.values[name] = result

    def _u_write_map_binding(self, name, value):
        from .bindings import map_binding

        state = self._u_state
        result = state.manager._call(
            f"{state.schema.name}.{name}: binding validation",
            lambda: map_binding(name, value),
        )
        state.values[name] = result

    _u_read_const = _u_read_plain

    def _u_write_const(self, name, value):
        raise AttributeError(f"{name}: const reference is read-only")

    def _u_read_managed(self, name):
        self._u_state.manager._require_confirmed()
        state = self._u_state
        if self._u_pin is None and (
            state.constructing or state.manager._selection is None
        ):
            return self._u_baseline(name)
        return state.manager._read_managed(self, name)

    def _u_write_managed(self, name, value):
        from .callbacks import require_mutation

        require_mutation(self._u_state.manager)
        if self._u_state.constructing:
            raise TransactionRequiredError(
                f"{name}: constructor baselines are read-only"
            )
        self._u_state.manager._write_managed(self, name, value)

    def _u_materialize_static(self, name, *, factory):
        state = self._u_state
        value = self._u_baseline(name)
        if value is MISSING:
            if name in state.resolving:
                raise UndoableDefinitionError(
                    f"{state.schema.name}.{name}: recursive lazy provider"
                )
            fact = state.schema.by_name[name]
            state.resolving.add(name)
            try:
                value = (
                    self._u_factory(fact, "default")
                    if factory
                    else fact["default_value"]
                )
            finally:
                state.resolving.remove(name)
            state.values[name] = value
        return value

    def _u_write_once_static(self, name, value):
        state = self._u_state
        if state.values[name] is not MISSING:
            raise AttributeError(f"{name}: lazy reference is already initialized")
        state.values[name] = value

    def _u_read_transient(self, name, *, factory):
        state = self._u_state
        if state.constructing:
            return self._u_baseline(name)
        edit = state.manager._edit
        historical_pin = self._u_pin is not None and not isinstance(
            self._u_pin, CandidateRead
        )
        if edit is None or self._u_view == "current" or historical_pin:
            return self._u_baseline(name)
        key = (state.node_id, name)
        if key not in edit.transient:
            fact = state.schema.by_name[name]
            if name in state.resolving:
                raise UndoableDefinitionError(
                    f"{state.schema.name}.{name}: recursive transient provider"
                )
            state.resolving.add(name)
            try:
                value = (
                    self._u_factory(fact, "working_default")
                    if factory
                    else self._u_baseline(name)
                )
            finally:
                state.resolving.remove(name)
            edit.transient[key] = value
        return edit.transient[key]

    def _u_write_transient(self, name, value):
        edit = self._u_state.manager._require_edit()
        if self._u_view == "current" or self._u_pin is not None:
            raise TransactionRequiredError("current transient facade is read-only")
        edit.transient[(self.node_id, name)] = value

    def _u_read_factory_static(self, name):
        return self._u_materialize_static(name, factory=True)

    def _u_read_default_static(self, name):
        return self._u_materialize_static(name, factory=False)

    def _u_read_unset_static(self, name):
        value = self._u_baseline(name)
        if value is MISSING:
            raise AttributeError(f"{name}: lazy field is unset")
        return value

    def _u_write_mutable_static(self, name, value):
        self._u_state.values[name] = value

    def _u_read_factory_transient(self, name):
        return self._u_read_transient(name, factory=True)

    def _u_read_baseline_transient(self, name):
        return self._u_read_transient(name, factory=False)

    def _u_read_current_managed(self, name):
        if (
            self._u_pin is not None
            or self._u_state.constructing
            or self._u_state.manager._selection is None
        ):
            return self._u_read_managed(name)
        self._u_state.manager._require_confirmed()
        return self._u_state.manager._committed_value(self, name)

    def _u_read_working_managed(self, name):
        return self._u_read_managed(name)

    def _u_read_thaw_managed(self, name):
        if (
            self._u_pin is not None
            or self._u_state.constructing
            or self._u_state.manager._selection is None
        ):
            return self._u_read_managed(name)
        return self._u_state.manager._read_managed(self, name, allow_thaw=True)

    def _u_write_current_managed(self, name, value):
        from .callbacks import require_mutation

        require_mutation(self._u_state.manager)
        raise TransactionRequiredError(f"{name}: current managed facade is read-only")

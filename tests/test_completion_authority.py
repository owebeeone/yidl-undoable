"""Synthetic backend failures exercise the exact authorized completion transition."""

from dataclasses import replace
import pytest
from yidl_undoable import *
from yidl_undoable.states import Editing


@undoable
class Model:
    value: int = managed(default=0)


def initialized():
    h = UndoRedoManager()
    node = Model(transaction_manager=h)
    h.initialize(node)
    return h, node, h.snapshot()


def assert_faulted(h, node, old, expected=0, *, confirmed=True):
    assert h._edit is None and h._prepared is None
    assert old.node(node.node_id).get("value") == 0
    if confirmed:
        assert node.value == h.snapshot().node(node.node_id).get("value") == expected
    else:
        with pytest.raises(HistoryFaultError):
            _ = node.value
        with pytest.raises(HistoryFaultError):
            h.snapshot()
    for action in (h.begin, h.undo, h.redo):
        with pytest.raises(HistoryFaultError):
            action()


def complete(h, token, entry):
    return h.commit() if entry == "explicit" else token._scope_commit()


@pytest.mark.parametrize("entry", ("explicit", "scope"))
@pytest.mark.parametrize(
    "stage", ("hidden_begin", "changed_then_failure", "residual_count")
)
def test_outer_completion_requires_exact_nesting_closure(monkeypatch, entry, stage):
    h, node, old = initialized()
    token = h.begin()
    node.value = 7
    backend_type = type(h._backend)
    original = backend_type.commit
    failure = LookupError("unexpected nesting then failure")

    def fail(backend, key):
        if stage != "residual_count":
            backend.begin(key)
        if stage == "changed_then_failure":
            raise failure
        result = original(backend, key)
        if stage == "residual_count":
            backend.begin_count = 1
        return result

    monkeypatch.setattr(backend_type, "commit", fail)
    with pytest.raises(HistoryFaultError) as caught:
        complete(h, token, entry)
    assert caught.value.__cause__ is (
        failure if stage == "changed_then_failure" else None
    )
    assert h.last_completion is token.completion
    assert_faulted(h, node, old, 7 if stage == "residual_count" else 0)
    if stage == "residual_count":
        assert token.completion.publication_complete and token.completion.finalized
    else:
        assert token.completion is None


@pytest.mark.parametrize("entry", ("explicit", "scope"))
@pytest.mark.parametrize(
    "change", ("selection", "overlay", "state", "count", "return", "backend_key")
)
@pytest.mark.parametrize("fails", (False, True))
def test_inner_completion_preserves_full_original_authority(
    monkeypatch, entry, change, fails
):
    h, node, old = initialized()
    token = h.begin()
    assert h.begin() is token
    node.value = 7
    backend_type = type(h._backend)
    original = backend_type.commit
    failure = LookupError("unexpected inner transition")

    def corrupt(backend, key):
        result = original(backend, key)
        if change == "selection":
            h._selection = replace(h._selection)
        elif change == "overlay":
            h._edit = replace(h._edit)
        elif change == "state":
            h._state = Editing()
        elif change == "count":
            backend.begin_count += 2
        elif change == "return":
            result = token.tx_id
        elif change == "backend_key":
            backend.tx_key = object()
        if fails:
            raise failure
        return result

    monkeypatch.setattr(backend_type, "commit", corrupt)
    with pytest.raises(HistoryFaultError) as caught:
        complete(h, token, entry)
    assert caught.value.__cause__ is (failure if fails else None)
    assert h.last_completion is None and token.completion is None
    assert_faulted(h, node, old, confirmed=change != "selection")


@pytest.mark.parametrize("operation", ("commit", "rollback"))
@pytest.mark.parametrize("fails", (False, True))
def test_idle_completion_cannot_acquire_an_unowned_token(monkeypatch, operation, fails):
    h, node, old = initialized()
    failure = LookupError("acquired without completion authority")

    def acquire(backend, key):
        backend.begin(key)
        if fails:
            raise failure
        return None

    monkeypatch.setattr(type(h._backend), operation, acquire)
    with pytest.raises(HistoryFaultError) as caught:
        getattr(h, operation)()
    assert caught.value.__cause__ is (failure if fails else None)
    assert h._backend.active_transaction is not None and h.last_completion is None
    assert_faulted(h, node, old)


@pytest.mark.parametrize("method", ("commit", "rollback"))
def test_stale_scope_requires_unchanged_replacement_ownership(monkeypatch, method):
    h, node, old = initialized()
    stale = h.begin()
    h.rollback()
    replacement = h.begin()
    node.value = 7
    backend_type = type(h._backend)
    name = "_" + method + "_scope"
    original = getattr(backend_type, name)

    def hidden_begin(backend, token):
        backend.begin()
        return original(backend, token)

    monkeypatch.setattr(backend_type, name, hidden_begin)
    with pytest.raises(HistoryFaultError):
        getattr(stale, "_scope_" + method)()
    assert (
        h._backend.active_transaction is replacement and replacement.completion is None
    )
    assert_faulted(h, node, old)


@pytest.mark.parametrize(
    "change",
    (
        "token_id",
        "token_key",
        "evidence_id",
        "evidence_key",
        "backend_key",
        "return",
        "state",
        "prepared",
    ),
)
def test_terminal_completion_matches_original_token_and_evidence(monkeypatch, change):
    h, node, old = initialized()
    token = h.begin()
    node.value = 7
    backend_type = type(h._backend)
    original = backend_type.commit

    def corrupt(backend, key):
        result = original(backend, key)
        if change == "token_id":
            token.tx_id += 100
        elif change == "token_key":
            token.tx_key = object()
        elif change == "evidence_id":
            token._completion = replace(token.completion, tx_id=token.tx_id + 100)
        elif change == "evidence_key":
            token._completion = replace(token.completion, tx_key=object())
        elif change == "backend_key":
            backend.tx_key = object()
        elif change == "return":
            result += 100
        elif change == "state":
            h._state = Editing()
        elif change == "prepared":
            h._prepared = object()
        return result

    monkeypatch.setattr(backend_type, "commit", corrupt)
    with pytest.raises(HistoryFaultError):
        h.commit()
    assert h.last_completion is token.completion and token.completion.finalized
    assert_faulted(h, node, old, 7)


@pytest.mark.parametrize("operation", ("commit", "rollback"))
@pytest.mark.parametrize("joined", (False, True))
@pytest.mark.parametrize("alter_key", (False, True))
def test_backend_failure_requires_unchanged_authority(
    monkeypatch, operation, joined, alter_key
):
    h, node, old = initialized()
    token = h.begin()
    if joined:
        h.begin()
    node.value = 7
    owner = h._edit
    state = h._state
    failure = LookupError("before any backend transition")

    def reject(backend, key):
        if alter_key:
            backend.tx_key = object()
        raise failure

    monkeypatch.setattr(type(h._backend), operation, reject)
    with pytest.raises(HistoryFaultError if alter_key else LookupError) as caught:
        getattr(h, operation)()
    if alter_key:
        assert caught.value.__cause__ is failure
        assert_faulted(h, node, old)
        return
    assert caught.value is failure and h._edit is owner and h._state is state
    assert h.active_transaction_for() is token and token.completion is None
    assert h._backend.begin_count == (2 if joined else 1) and node.value == 7
    monkeypatch.undo()
    h.rollback()
    assert node.value == old.node(node.node_id).get("value") == 0


@pytest.mark.parametrize("target", ("token_id", "nesting"))
def test_operation_authority_rejects_scalar_protocol_before_equality(target):
    from yidl_undoable.undoable_markers import MISSING

    invoked = []

    class EqualityTrap:
        def __eq__(self, other):
            invoked.append(True)
            h.rollback()
            return True

    def corrupt():
        if target == "token_id":
            token.tx_id = EqualityTrap()
        else:
            h._backend.begin_count = EqualityTrap()
        return 5

    @undoable
    class Provider:
        value: int = managed(default=0)
        delayed: int = lazy(default_factory=corrupt)

    h = UndoRedoManager()
    node = Provider(transaction_manager=h)
    h.initialize(node)
    old = h.snapshot()
    token = h.begin()
    node.value = 7
    with pytest.raises(HistoryFaultError):
        _ = node.delayed
    assert not invoked and node._u_state.values["delayed"] is MISSING
    assert_faulted(h, node, old)


def test_terminal_cleanup_cannot_revive_diagnosed_operation_fault():
    mode = ["pure"]

    def freeze(value):
        if mode[0] == "corrupt":
            h._state = Editing()
        return value

    @undoable
    class Convertible:
        value: int = managed(default=0, freeze=freeze)

    h = UndoRedoManager()
    node = Convertible(transaction_manager=h)
    h.initialize(node)
    old = h.snapshot()
    token = h.begin()
    node.value = 7
    mode[0] = "corrupt"
    with pytest.raises(HistoryFaultError):
        h.commit()
    assert token.completion.discard_complete and token.completion.finalized
    assert h.last_completion is token.completion
    assert_faulted(h, node, old)

import pytest
from yidl_undoable import *
from yidl_undoable import transaction_yidl as runtime
from yidl_lifecycle.transaction_yidl import LifecycleTransaction


@undoable
class Model:
    value: int = managed(default=0)


SETUP_CASES = (
    (False, "backend_return"),
    (False, "overlay"),
    (False, "backend_bind"),
    (False, "wrapper_bind"),
    (True, "backend_return"),
    (True, "backend_bind"),
    (True, "wrapper_bind"),
)


@pytest.mark.parametrize("joined,stage", SETUP_CASES)
@pytest.mark.parametrize("abort", ("clean", "before", "after"))
def test_complete_begin_setup_failure_closes_or_faults(
    monkeypatch, joined, stage, abort
):
    h = UndoRedoManager()
    node = Model(transaction_manager=h)
    h.initialize(node)
    snapshot = h.snapshot()
    old_scope = h.begin() if joined else None
    if joined:
        node.value = 7
    setup_failure = (
        MemoryError("overlay allocation") if stage == "overlay" else RuntimeError(stage)
    )
    abort_failure = RuntimeError("abort failure")
    backend_type = type(h._backend)
    original_begin, original_abort = backend_type.begin, backend_type.rollback
    original_bind = LifecycleTransaction.bind_scope
    binds = [0]
    if stage == "backend_return":

        def fail_begin(backend, key):
            original_begin(backend, key)
            raise setup_failure

        monkeypatch.setattr(backend_type, "begin", fail_begin)
    elif stage == "overlay":

        def fail_overlay(*args, **kwargs):
            raise setup_failure

        monkeypatch.setattr(runtime, "EditOverlay", fail_overlay)
    else:

        def fail_bind(token, **kwargs):
            binds[0] += 1
            if binds[0] == (1 if stage == "backend_bind" else 2):
                raise setup_failure
            return original_bind(token, **kwargs)

        monkeypatch.setattr(LifecycleTransaction, "bind_scope", fail_bind)
    if abort != "clean":

        def fail_abort(backend, key):
            if abort == "after":
                original_abort(backend, key)
            raise abort_failure

        monkeypatch.setattr(backend_type, "rollback", fail_abort)
    expected = type(setup_failure) if abort == "clean" else HistoryFaultError
    with pytest.raises(expected) as caught:
        h.begin()
    assert h._edit is None and h._prepared is None
    assert snapshot.node(node.node_id).get("value") == node.value == 0
    if abort == "clean":
        assert caught.value is setup_failure
        assert h.active_transaction_for() is None and h._backend.begin_count == 0
        assert h.frame_count == 1
        monkeypatch.undo()
        with h.begin():
            node.value = 9
        assert node.value == node.current.value == 9
        assert h.frame_count == 2 and h.active_transaction_for() is None
        assert h._backend.begin_count == 0
        if old_scope is not None:
            with pytest.raises(RuntimeError, match="stale"):
                old_scope.__exit__(None, None, None)
            assert h.frame_count == 2
    else:
        assert isinstance(caught.value.__cause__, BaseExceptionGroup)
        assert caught.value.__cause__.exceptions == (setup_failure, abort_failure)
        if abort == "after":
            assert h.last_completion is not None and h.last_completion.finalized
        for action in (h.begin, h.undo, h.redo):
            with pytest.raises(HistoryFaultError):
                action()


def test_unexpected_begin_nesting_is_an_ownership_fault_after_clean_abort(monkeypatch):
    h = UndoRedoManager()
    node = Model(transaction_manager=h)
    h.initialize(node)
    backend_type = type(h._backend)
    original = backend_type.begin

    def add_hidden_begin(backend, key):
        token = original(backend, key)
        backend.begin_count += 1
        return token

    monkeypatch.setattr(backend_type, "begin", add_hidden_begin)
    with pytest.raises(HistoryFaultError):
        h.begin()
    assert h._edit is None and h.active_transaction_for() is None
    assert h.snapshot().node(node.node_id).get("value") == 0
    monkeypatch.undo()
    with pytest.raises(HistoryFaultError):
        h.begin()


def test_failed_begin_abort_with_changed_selection_is_unconfirmed(monkeypatch):
    h = UndoRedoManager()
    node = Model(transaction_manager=h)
    h.initialize(node)
    old = h.snapshot()
    setup_failure, abort_failure = MemoryError("allocation"), RuntimeError("corruption")
    original_abort = type(h._backend).rollback

    def fail_overlay(*args, **kwargs):
        raise setup_failure

    def corrupt_abort(backend, key):
        original_abort(backend, key)
        h._selection = None
        raise abort_failure

    monkeypatch.setattr(runtime, "EditOverlay", fail_overlay)
    monkeypatch.setattr(type(h._backend), "rollback", corrupt_abort)
    with pytest.raises(HistoryFaultError) as caught:
        h.begin()
    assert caught.value.__cause__.exceptions == (setup_failure, abort_failure)
    assert h._edit is None and old.node(node.node_id).get("value") == 0
    for action in (lambda: node.value, h.snapshot, h.begin):
        with pytest.raises(HistoryFaultError):
            action()

import pytest
from yidl_undoable import *


@undoable
class Model:
    value: int = managed(default=0)


@pytest.mark.parametrize("bookkeeping", (True, False))
def test_apply_failure_after_selection_install_faults(bookkeeping):
    h = UndoRedoManager()
    x = Model(transaction_manager=h)
    h.initialize(x)
    token = h.begin()
    x.value = 7
    original = h._aggregate._apply_prepared_commit_tx_by_key
    failure = RuntimeError("failure after selection install")

    def fail(key, token_id):
        if bookkeeping:
            original(key, token_id)
        else:
            h._selection = h._prepared.selection
        raise failure

    h._aggregate._apply_prepared_commit_tx_by_key = fail
    with pytest.raises(HistoryFaultError) as caught:
        h.commit()
    assert caught.value.__cause__ is failure
    assert h.last_completion is token.completion
    assert (
        token.completion.publication_started
        and not token.completion.publication_complete
    )
    assert token.completion.discard_complete
    assert h._edit is None
    if bookkeeping:
        assert x.value == 7 and h.snapshot().node(x.node_id).get("value") == 7
    else:
        with pytest.raises(HistoryFaultError):
            _ = x.value
        with pytest.raises(HistoryFaultError):
            h.snapshot()
    for action in (h.begin, h.undo, h.redo):
        with pytest.raises(HistoryFaultError):
            action()


@pytest.mark.parametrize("abort_closes", (False, True))
def test_failed_enlist_abort_failure_detaches_overlay_and_faults(
    monkeypatch, abort_closes
):
    h = UndoRedoManager()
    x = Model(transaction_manager=h)
    h.initialize(x)
    old = h.snapshot()
    enlist_failure = RuntimeError("synthetic enlist failure")
    abort_failure = RuntimeError("synthetic abort failure")
    backend_type = type(h._backend)
    original_abort = backend_type.rollback

    def fail_enlist(*args):
        raise enlist_failure

    def fail_abort(backend, key):
        if abort_closes:
            original_abort(backend, key)
        raise abort_failure

    monkeypatch.setattr(backend_type, "enlist", fail_enlist)
    monkeypatch.setattr(backend_type, "rollback", fail_abort)
    with pytest.raises(HistoryFaultError) as caught:
        h.begin()
    assert h._edit is None
    cause = caught.value.__cause__
    assert isinstance(cause, BaseExceptionGroup)
    assert cause.exceptions == (enlist_failure, abort_failure)
    assert old.node(x.node_id).get("value") == x.value == 0
    assert h.snapshot().node(x.node_id).get("value") == 0
    if abort_closes:
        assert h.last_completion is not None and h.last_completion.finalized
    for action in (h.begin, h.undo, h.redo):
        with pytest.raises(HistoryFaultError):
            action()

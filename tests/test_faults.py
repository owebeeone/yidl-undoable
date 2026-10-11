import pytest
from yidl_undoable import undoable, managed, UndoRedoManager, HistoryFaultError


@undoable
class Model:
    value: int = managed(default=0)


def test_backend_cleanup_failure_preserves_confirmed_publication():
    h = UndoRedoManager()
    x = Model(transaction_manager=h)
    h.initialize(x)
    token = h.begin()
    x.value = 1

    def fail(key, token_id):
        raise RuntimeError("synthetic cleanup failure")

    h._aggregate._after_commit_tx_by_key = fail
    with pytest.raises(HistoryFaultError):
        h.commit()
    assert token.completion.publication_complete
    assert not token.completion.after_actions_complete
    assert h.snapshot().node(x.node_id).get("value") == 1
    assert x.value == 1
    with pytest.raises(HistoryFaultError):
        h.begin()
    with pytest.raises(HistoryFaultError):
        h.undo()


def test_backend_ownership_loss_does_not_claim_rollback():
    h = UndoRedoManager()
    x = Model(transaction_manager=h)
    h.initialize(x)
    token = h.begin()

    def lose(key, token_id):
        h._backend.active_transaction = None

    h._aggregate._prepare_commit_tx_by_key = lose
    with pytest.raises(HistoryFaultError):
        h.commit()
    assert not token.completion.ownership_preserved
    assert h.snapshot().node(x.node_id).get("value") == 0


def test_unconfirmed_selection_blocks_live_data_and_snapshot():
    h = UndoRedoManager()
    x = Model(transaction_manager=h)
    h.initialize(x)
    h.begin()

    def corrupt(key, token_id):
        h._selection = None
        raise RuntimeError("synthetic selection corruption")

    h._aggregate._apply_prepared_commit_tx_by_key = corrupt
    with pytest.raises(HistoryFaultError):
        h.commit()
    with pytest.raises(HistoryFaultError):
        _ = x.value
    with pytest.raises(HistoryFaultError):
        h.snapshot()
    with pytest.raises(HistoryFaultError):
        Model(transaction_manager=h)

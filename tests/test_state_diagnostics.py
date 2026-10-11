import pytest
from yidl_undoable import *


@undoable
class Model:
    value: int = managed(default=0)


def test_policy_and_key_are_fixed_configuration():
    h = UndoRedoManager()
    with pytest.raises(AttributeError):
        h.absent_policy = ReadLastVisible()
    with pytest.raises(AttributeError):
        h.tx_key = "other"


def test_uninitialized_diagnostics_are_contextual():
    h = UndoRedoManager()
    for read in (
        lambda: h.cursor,
        lambda: h.frame_id,
        lambda: h.frame_count,
        lambda: h.roots,
        lambda: h.current_roots,
    ):
        with pytest.raises(RuntimeError, match="initialized"):
            read()


def test_failed_begin_enlistment_leaves_no_edit(monkeypatch):
    h = UndoRedoManager()
    x = Model(transaction_manager=h)
    h.initialize(x)

    def fail(*args):
        raise RuntimeError("synthetic enlistment")

    monkeypatch.setattr(type(h._backend), "enlist", fail)
    with pytest.raises(RuntimeError, match="synthetic"):
        h.begin()
    assert h._edit is None and h.active_transaction_for() is None
    assert x.value == 0
    monkeypatch.undo()
    with h.begin():
        x.value = 1
    assert x.value == 1

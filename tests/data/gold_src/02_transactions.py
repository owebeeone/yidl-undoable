import pytest
from yidl_undoable import *


@undoable
class Item:
    value: int = managed(default=1)
    sequence: tuple = managed(default=(1,), thaw=list, freeze=tuple)
    plain: int = field(default=0)


h = UndoRedoManager()
a = Item(transaction_manager=h)
h.initialize(a)
with pytest.raises(TransactionRequiredError):
    a.value = 2
with h.begin() as token:
    assert h.active_transaction_for() is token
    a.value = 2
    a.plain = 7
    assert a.value == a.working.value == 2 and a.current.value == 1
    assert a.sequence == (1,)
    working = a.working.sequence
    assert working is a.working.sequence
    working.append(2)
    assert a.sequence is working
assert a.value == 2 and a.sequence == (1, 2)
working.append(99)
assert a.sequence == (1, 2)
h.begin()
a.value = 3
a.plain = 8
assert h.rollback() == 2
assert a.value == 2 and a.plain == 8
with pytest.raises(ValueError):
    with h.begin():
        a.value = 9
        raise ValueError("body")
assert a.value == 2
outer = h.begin()
assert h.begin() is outer
a.value = 4
assert h.commit() is None and h.frame_count == 2
assert h.commit() == outer.tx_id and h.frame_count == 3
outer = h.begin()
h.begin()
h.rollback()
replacement = h.begin()
with pytest.raises(RuntimeError):
    outer.__exit__(None, None, None)
assert h.active_transaction_for() is replacement
h.rollback()
with pytest.raises(RuntimeError):
    h.begin("wrong")

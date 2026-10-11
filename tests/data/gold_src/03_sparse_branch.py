import pytest
from yidl_undoable import *


@undoable
class Pair:
    a: int = managed(default=0)
    b: int = managed(default=0)
    items: tuple = managed(default=(), thaw=list, freeze=tuple)


h = UndoRedoManager()
x = Pair(transaction_manager=h)
h.initialize(x)
assert not h.can_undo() and not h.undo() and not h.redo()
with h.begin() as t:
    x.a = 1
    assert not h.can_undo() and not h.can_redo()
    with pytest.raises(RuntimeError):
        h.undo()
with h.begin():
    x.b = 2
assert h.frame_count == 3
assert h.undo() and x.a == 1 and x.b == 0
assert h.redo() and x.b == 2
assert h.undo()
h.begin()
x.a = 99
h.rollback()
assert h.can_redo() and x.a == 1
with h.begin() as branch_token:
    x.a = 3
assert x.b == 0 and h.frame_count == 3 and h.frame_id == 3
assert h.cursor == 2 and branch_token.tx_id != h.frame_id
assert not h.can_redo()
assert h.undo() and x.a == 1 and x.b == 0
assert h.redo() and x.a == 3 and x.b == 0
with h.begin():
    assert x.working.items == []
assert h.frame_count == 4
versions = h._selection.epoch.nodes[x.node_id].fields["items"].frame_ids
assert versions == (0, 4)
with h.begin():
    pass
assert h.frame_count == 5

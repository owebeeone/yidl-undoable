import pytest
from yidl_undoable import *


@undoable
class Node:
    number: int = managed(default=0)
    children: tuple = managed(default=())
    resource: object = field(default="resource")


h = UndoRedoManager(absent_policy=ReadLastVisible())
c = Node(number=1, transaction_manager=h)
a = Node(children=(c,), transaction_manager=h)
b = Node(children=(c,), transaction_manager=h)
h.initialize(a, b)
old = h.snapshot()
assert old.roots[0].get("children")[0] is old.roots[1].get("children")[0]
with pytest.raises(AttributeError):
    old.node(c.node_id).get("resource")
with pytest.raises(AttributeError):
    old.node(c.node_id).get("unknown")
with h.begin():
    c.number = 99
    h.remove_root(a)
    b.children = ()
assert not a.present and not c.present
assert a.children[0].number == 1
assert c.number == 1
with h.begin():
    h.add_root(c)
    c.number = 2
assert c.number == 2 and a.children[0].number == 1
assert a.children[0]._u_pin is not None
with h.begin():
    with pytest.raises(TransactionRequiredError):
        a.children[0].number = 4
    new = Node(number=3, transaction_manager=h)
    h.add_root(new)
future = h.snapshot()
assert future.node(new.node_id).get("number") == 3
assert h.undo()
with h.begin():
    c.number = 5
assert c.number == 5 and future.node(new.node_id).get("number") == 3
with h.begin():
    with pytest.raises(UnavailableNodeError):
        h.add_root(new)
with pytest.raises(ObjectAbsentError):
    h.snapshot().node(new.node_id)
assert old.node(c.node_id).get("number") == 1
strict = UndoRedoManager()
s = Node(transaction_manager=strict)
strict.initialize(s)
with strict.begin():
    strict.remove_root(s)
with pytest.raises(ObjectAbsentError):
    _ = s.number
assert s.resource == "resource" and not s.present
with strict.begin():
    strict.add_root(s)
assert s.number == 0
# Snapshot during edit selects committed roots and values.
with h.begin():
    c.number = 8
    during = h.snapshot()
    assert during.node(c.node_id).get("number") == 5

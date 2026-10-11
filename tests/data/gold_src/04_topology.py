import pytest
from yidl_undoable import *


@undoable
class Node:
    label: str = managed(default="old")
    children: tuple = managed(default=(), thaw=list, freeze=tuple)


h = UndoRedoManager()
c = Node(transaction_manager=h)
a = Node(children=(c,), transaction_manager=h)
b = Node(children=(c,), transaction_manager=h)
h.initialize(a, b)
assert c.present and a.children[0] == b.children[0]
with h.begin():
    c.label = "new"
    assert a.current.children[0].label == "old"
    assert a.children[0].label == b.working.children[0].label == "new"
    assert a.current.children[0]._u_view == "current"
    assert b.working.children[0]._u_view == "working"
assert c.label == "new"
with h.begin():
    a.working.children.clear()
    assert c.present
    b.working.children.clear()
    assert not c.present
    child = Node(label="provisional", transaction_manager=h)
    child.label = "attached"
    assert not child.present
    a.working.children.append(child)
    assert child.present
assert a.children[0].label == "attached" and not c.present
with h.begin():
    h.add_root(c)
    c.label = "restored"
    h.remove_root(a)
    h.remove_root(b)
assert h.roots == (c,)
assert h.undo() and a.present and b.present and not c.present
assert h.redo() and c.label == "restored"
with h.begin():
    h.remove_root(c)
assert h.roots == ()
with h.begin():
    h.add_root(c)
assert c.present
h.begin()
provisional = Node(transaction_manager=h)
h.rollback()
with h.begin():
    with pytest.raises(UnavailableNodeError):
        h.add_root(provisional)
foreign = UndoRedoManager()
f = Node(transaction_manager=foreign)
foreign.initialize(f)
with pytest.raises(ForeignManagerError):
    with h.begin():
        c.children = (f,)
assert c.children == ()
with pytest.raises(GraphCycleError):
    with h.begin():
        c.children = (c,)
assert c.children == ()
# Initialization traverses shared nodes and refuses cycles without publishing.
setup = UndoRedoManager()
x = Node(transaction_manager=setup)
y = Node(children=(x,), transaction_manager=setup)
x._u_state.values["children"] = (y,)
with pytest.raises(GraphCycleError):
    setup.initialize(x)
assert setup._selection is None
x._u_state.values["children"] = ()
setup.initialize(x, y)

from types import MappingProxyType
from yidl_undoable import *


@undoable
class Node:
    value: int = managed(default=0)
    children: frozenset = managed(default=frozenset())
    nested: object = managed(default=None)


h = UndoRedoManager()
child = Node(transaction_manager=h)
root = Node(
    children=frozenset((child,)),
    nested=MappingProxyType({"aliases": (child, frozenset((child,)))}),
    transaction_manager=h,
)
h.initialize(root)
snapshot = h.snapshot()
pinned = snapshot.node(child.node_id)
members = snapshot.node(root.node_id).get("children")
assert pinned in members and next(iter(members)) is pinned
assert {pinned: "member"}[next(iter(members))] == "member"
aliases = snapshot.node(root.node_id).get("nested")["aliases"]
assert aliases[0] is pinned and next(iter(aliases[1])) is pinned
assert h.snapshot().node(child.node_id) != pinned
with h.begin():
    child.value = 1
old = h.snapshot()
assert h.undo()
with h.begin():
    root.children = frozenset()
    root.nested = None
assert old.node(child.node_id).get("value") == 1
assert pinned.get("value") == 0 and pinned in members

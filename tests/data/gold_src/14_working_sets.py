from yidl_undoable import *


@undoable
class Node:
    value: tuple = managed(default=(), thaw=list, freeze=tuple)
    children: frozenset = managed(default=frozenset(), thaw=set, freeze=frozenset)
    nested: tuple = managed(
        default=(), freeze=lambda value: tuple(frozenset(part) for part in value)
    )


h = UndoRedoManager()
child = Node(transaction_manager=h)
other = Node(transaction_manager=h)
parent = Node(children=frozenset((child,)), transaction_manager=h)
h.initialize(parent, other)
h.begin()
escaped = parent.working.children
ordinary = next(iter(parent.children))
assert ordinary is child.default and ordinary.value == ()
assert (child.node_id, "value") not in h._edit.touched
assert next(iter(escaped)) is child.working
assert next(iter(parent.current.children)) is child.current
parent.children = {child.current, other.default}
pending = h._edit.touched[(parent.node_id, "children")]
assert parent.working.children is pending
assert pending == {child, other} and all(node._u_view == "working" for node in pending)
assert all(node._u_view == "default" for node in parent.children)
assert all(node._u_view == "working" for node in pending)
parent.nested = ({child.current},)
assert next(iter(parent.working.nested[0])) is child.working
assert next(iter(parent.nested[0])) is child.default
child.working.value.append("nested")
h.commit()
pending.clear()
escaped.clear()
assert parent.children == frozenset((child, other))
assert child.value == ("nested",)
assert next(iter(parent.current.nested[0])) is child.current
assert h.undo() and child.value == ()

"""Shared nested identities, committed reads and snapshots through branching."""

from yidl_undoable import UndoRedoManager, managed, undoable


@undoable
class Node:
    label: str = managed(default="")
    children: tuple["Node", ...] = managed(default=(), thaw=list, freeze=tuple)


history = UndoRedoManager()
child = Node(label="before", transaction_manager=history)
parent = Node(children=(child,), transaction_manager=history)
history.initialize(parent)
with history.begin():
    parent.working.children[0].label = "after"
    assert parent.current.children[0].label == "before"
snapshot = history.snapshot()
assert history.undo() and parent.children[0].label == "before"
with history.begin():
    child.label = "branch"
assert snapshot.roots[0].get("children")[0].get("label") == "after"
assert parent.children[0].label == "branch"
print(parent.children[0].label, snapshot.frame_id)

"""Runnable companion to docs/Snapshots.md."""

from yidl_undoable import UndoRedoManager, managed, undoable

@undoable
class Document:
    text: str = managed(default="zero")

history = UndoRedoManager()
document = Document(transaction_manager=history)
history.initialize(document)
with history.begin():
    document.text = "one"
pinned = history.snapshot()
old_document = pinned.node(document.node_id)
assert history.undo()
with history.begin():
    document.text = "another branch"
assert old_document.get("text") == "one"
assert document.text == "another branch" and not history.can_redo()

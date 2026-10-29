"""Runnable companion to docs/Concepts.md."""

from yidl_undoable import UndoRedoManager, field, local_store, managed, undoable

@undoable
class Note:
    text: str = managed(default="original")
    label: str = field(default="draft")
    cache: dict = local_store(default_factory=dict)

history = UndoRedoManager()
note = Note(transaction_manager=history)
history.initialize(note)
history.begin()
note.text = "pending"
note.label = "reviewed"
note.cache["width"] = 80
history.rollback()
assert note.text == "original"
assert note.label == "reviewed" and note.cache == {"width": 80}


saved_current = note.current
with history.begin():
    note.text = "new"
    assert note.text == note.default.text == note.working.text == "new"
    assert note.current.text == "original"
assert saved_current.text == "new"
assert history.undo() and saved_current.text == "original"


assert history.can_redo()
with history.begin():
    note.text = "another direction"
assert not history.can_redo()
assert history.frame_count == 2

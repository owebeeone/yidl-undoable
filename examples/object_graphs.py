"""Runnable companion to docs/ObjectGraphs.md."""

from yidl_undoable import UndoRedoManager, ObjectAbsentError, managed, undoable

@undoable
class Item:
    text: str = managed(default="first")

@undoable
class Document:
    items: tuple[Item, ...] = managed(default=(), thaw=list, freeze=tuple)

history = UndoRedoManager()
child = Item(transaction_manager=history)
document = Document(items=(child,), transaction_manager=history)
history.initialize(document)
with history.begin():
    document.working.items.clear()
assert not child.present
try:
    child.text
except ObjectAbsentError:
    pass
else:
    raise AssertionError("absent managed read should fail")
assert history.undo() and child.present and child.text == "first"


with history.begin():
    second = Item(text="second", transaction_manager=history)
    document.working.items.append(second)
assert len(document.items) == 2
assert history.undo() and len(document.items) == 1
assert history.redo() and document.items[1].text == "second"


other = UndoRedoManager()
a = Item(text="A", transaction_manager=other)
b = Item(text="B", transaction_manager=other)
c = Item(text="C", transaction_manager=other)
other.initialize(a, b, c)
assert other.roots == (a, b, c)
with other.begin():
    other.remove_root(b)
assert other.undo() and b.present

"""Run with an installed yidl-undoable package: python examples/first_use.py."""

from yidl_undoable import UndoRedoManager, const, local_store, managed, undoable


@undoable
class Document:
    name: str = const(default="document")
    items: tuple[str, ...] = managed(default=(), thaw=list, freeze=tuple)
    cache: dict[str, object] = local_store(default_factory=dict)


history = UndoRedoManager()
document = Document(transaction_manager=history)
history.initialize(document)
with history.begin():
    document.working.items.append("first")
assert history.undo() and document.items == ()
assert history.redo() and document.items == ("first",)
print(document.name, document.items)

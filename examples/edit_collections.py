"""Runnable companion to docs/Collections.md."""

from yidl_undoable import UndoRedoManager, managed, undoable

@undoable
class ShoppingList:
    items: tuple[str, ...] = managed(default=(), thaw=list, freeze=tuple)

history = UndoRedoManager()
shopping = ShoppingList(transaction_manager=history)
history.initialize(shopping)
with history.begin():
    working_items = shopping.working.items
    working_items.append("bread")
    working_items.append("milk")
    assert shopping.current.items == ()
assert shopping.items == ("bread", "milk")
assert history.undo() and shopping.items == ()
assert history.redo() and shopping.items == ("bread", "milk")


working_items.append("too late")
assert shopping.items == ("bread", "milk")

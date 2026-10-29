# Your first undo

Use Undoable when several model changes should form one reversible edit. Start
with a single managed value, then add collections and children as needed.

## Installation

```sh
python -m pip install yidl-undoable
```

The package targets CPython 3.12–3.15. It depends on YIDL, Astichi, Lifecycle and
YIDL Cache. This is not a claim that every OS/Python combination has dependency
wheels: Astichi 1.1.3 lacks a Windows CPython 3.15 wheel, and that source-build
route is not qualified here. Use an available dependency-wheel combination.
Development checkout verification and published-package qualification are separate;
see [contributor guidance](../CONTRIBUTING.md).

## Declare a model and its baseline

```python
from yidl_undoable import UndoRedoManager, managed, undoable

@undoable
class Document:
    title: str = managed(default="Draft")

history = UndoRedoManager()
document = Document(transaction_manager=history)
history.initialize(document)
assert document.title == "Draft"
assert history.cursor == 0 and not history.can_undo()
```

`managed` means the value belongs to transactional history. Construction associates
the object with a manager; `initialize` selects one or more roots and freezes their
starting managed graph as frame zero. Call it once, after setup construction.
All roots and managed descendants must belong to the same manager.

## Commit, undo and redo

```python
with history.begin():
    document.title = "Ready"
assert document.title == "Ready"
assert history.undo() and document.title == "Draft"
assert history.redo() and document.title == "Ready"
```

A normal outer scope exit commits one frame. Managed setters are available only
while editing; outside a transaction they raise `TransactionRequiredError`.
`undo()` and `redo()` return `False` when there is no step in that direction.
Navigation is unavailable during an edit.

## Discard an unfinished edit

```python
try:
    with history.begin():
        document.title = "Discard me"
        raise ValueError("cancel the edit")
except ValueError:
    pass
assert document.title == "Ready"
```

An exceptional scope exit rolls back the joined edit. Rollback creates no frame;
undo navigates a frame that was already committed. For explicit completion use
`history.begin()`, then `history.commit()` or `history.rollback()`.

What happens if you undo, then commit a different title? The new frame replaces
the redo tail. See [frames and views](Concepts.md), then
[edit collections](Collections.md).

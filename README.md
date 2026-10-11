# YIDL Undoable

Proposed generated data classes with Lifecycle-style transactions and frame-based
undo/redo. Committed fields use sparse ordered histories; constants and management
storage remain outside history.

This repository currently contains the design, not an implemented package.

- [Detailed design](dev-docs/UndoableDesign.md)
- [Current checkpoint and review status](dev-docs/CurrentProgramCheckpoint.md)
- [Developer documents](dev-docs/README.md)

## Proposed first use

Names below describe the intended API and are not available to import yet.

```python
from yidl_undoable import UndoRedoManager, const, local_store, managed, undoable


@undoable
class Document:
    name: str = const(default="document")
    items: tuple[str, ...] = managed(default=(), thaw=list, freeze=tuple)
    cache: dict[str, object] = local_store(default_factory=dict)


history = UndoRedoManager()
document = Document(transaction_manager=history)
history.initialize(document)

history.begin()
try:
    document.working.items.append("first")
except BaseException:
    history.rollback()
    raise
else:
    history.commit()

assert history.undo()
assert document.items == ()
assert history.redo()
assert document.items == ("first",)
```

The manager controls the selected frame. `rollback()` discards a pending edit;
`undo()` selects a previous committed frame. Successful ordinary context-manager
exit commits, and exceptional exit rolls back, following Lifecycle.

Undo restores managed model data. It does not rewind caches, file descriptors,
external resources, or side effects.

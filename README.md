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

Unmarked annotated fields are plain and nontransactional. Use `managed` for data
that rollback and undo must restore; plain fields and management storage survive
both operations unchanged.

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

## Nested objects and committed reads

The relationship itself must be managed to belong to history:

```python
@undoable
class Node:
    label: str = managed(default="")
    children: tuple["Node", ...] = managed(default=(), thaw=list, freeze=tuple)


tree_history = UndoRedoManager()
child = Node(label="before", transaction_manager=tree_history)
parent = Node(children=(child,), transaction_manager=tree_history)
tree_history.initialize(parent)

with tree_history.begin():
    parent.working.children[0].label = "after"
    assert parent.current.children[0].label == "before"
    assert parent.working.children[0].label == "after"

assert tree_history.undo()
assert parent.children[0].label == "before"
assert tree_history.redo()
assert parent.children[0].label == "after"
```

Current and working views propagate to their children. Nonversioned references
do not establish historical membership. Holding a live view follows the selected
frame; use a snapshot to retain historical managed data.

# Manage nested objects

Roots define the entry points to a frame. Traversal follows managed fields,
including node references inside supported containers. Ordinary fields and caches
do not establish membership. A manager can have multiple roots; their graph is
committed and navigated together.

```python
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
```

The Python child handle still exists after removal. Its managed presence and reads
follow the selected frame. By default an absent managed read raises; management
fields remain accessible. `UndoRedoManager(absent_policy=ReadLastVisible())` instead
permits reads from the last visible surviving frame at or before the cursor,
with descendants pinned read-only to that fallback. Neither policy permits absent
managed writes.

## Create and attach during an edit

```python
with history.begin():
    second = Item(text="second", transaction_manager=history)
    document.working.items.append(second)
assert len(document.items) == 2
assert history.undo() and len(document.items) == 1
assert history.redo() and document.items[1].text == "second"
```

After initialization, construction requires a transaction. New objects are
provisional until attached by a managed edge or `add_root`; unattached provisional
objects are not published. Aliases are allowed; cycles and cross-manager edges
are rejected. This is an acyclic graph, not necessarily a strict tree.

## Several roots

```python
other = UndoRedoManager()
a = Item(text="A", transaction_manager=other)
b = Item(text="B", transaction_manager=other)
c = Item(text="C", transaction_manager=other)
other.initialize(a, b, c)
assert other.roots == (a, b, c)
with other.begin():
    other.remove_root(b)
assert other.undo() and b.present
```

Call `initialize(*roots)` once. Later use `add_root`/`remove_root` inside an edit.
The proposed `undoable_leaf` helper is not implemented. Objects excluded from the
initial graph, aborted creations, or objects existing only in a future frame at an
earlier cursor have no usable baseline there; they cannot simply be resurrected.
See [snapshots](Snapshots.md) for intentional historical reads.

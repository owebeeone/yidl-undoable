# Frames, fields and views

A manager owns one transaction key, a set of roots and one history cursor. A
frame records the roots and committed managed graph visible at that step. Field
histories are sparse: unchanged values can be shared with earlier frames.

## Choose what history owns

```python
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
```

Only `text` is versioned. Unmarked annotations also use ordinary `field` storage.
`const` prevents reference replacement, but does not freeze mutable contents.
Lazy and local storage are shared across frames. See the [field table](API.md#fields)
before deciding what belongs to your logical model.

## Live views follow the cursor

```python
saved_current = note.current
with history.begin():
    note.text = "new"
    assert note.text == note.default.text == note.working.text == "new"
    assert note.current.text == "original"
assert saved_current.text == "new"
assert history.undo() and saved_current.text == "original"
```

| View | During editing | Outside editing |
| --- | --- | --- |
| Ordinary handle / `.default` | Pending managed values if touched | Selected committed values |
| `.current` | Committed values, managed setters reject | Selected committed values |
| `.working` | Pending values; may thaw on first read | Committed values |

These are live handles, not snapshots. Keeping `.current` does not preserve old
values. [Snapshots](Snapshots.md) pin committed managed data instead.

## A new edit replaces redo

```python
assert history.can_redo()
with history.begin():
    note.text = "another direction"
assert not history.can_redo()
assert history.frame_count == 2
```

`cursor` counts positions in the surviving history. `frame_id` is a separately
allocated increasing ID; after branching it need not equal the cursor.
Every successful outer commit creates a frame, including a no-op edit.
There is currently no retention limit or disk-backed history.

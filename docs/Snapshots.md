# Keep snapshots

A live handle follows history navigation. A snapshot instead retains committed
managed data from one frame, even after new edits discard that frame's branch.
It does not capture ordinary fields, caches, resources or application methods.

```python
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
```

`FrameSnapshot.roots` contains data-only `SnapshotNode` handles. Use
`.node(node_id)` to locate a member and `.get(field_name)` to read a managed field.
Nested references become snapshot nodes and aliases retain identity within the
same snapshot. Unknown/nonmanaged fields raise `AttributeError`; missing nodes
raise `ObjectAbsentError`. There are no setters or application methods.

Snapshot node identity is scoped to the snapshot and node ID; it is unaffected
by optional facade logical comparisons. Taking a snapshot during editing captures
the selected committed frame, not pending values. Snapshots retain their epoch in
memory, so keeping many snapshots can retain abandoned history. They are not a
disk serialization format.

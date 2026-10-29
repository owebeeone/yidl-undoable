# Compare models

By default, handles compare by shared node-state identity, including across views.
Optional logical comparison reads fields instead. Choose it per class and choose
participation on each field declaration.

```python
from yidl_undoable import UndoRedoManager, field, managed, undoable

@undoable(eq=True, order=True)
class Score:
    points: int = managed(default=0)
    label: str = field(default="", compare=False)

history = UndoRedoManager()
a = Score(points=1, label="A", transaction_manager=history)
b = Score(points=2, label="B", transaction_manager=history)
history.initialize(a, b)
assert a < b
with history.begin():
    a.points = 2
assert a == b
assert a != a.current  # Different generated facade classes.
```

`eq=False, order=False` are Undoable's defaults. `order=True` requires `eq=True`.
Logical comparisons require the exact same facade class: ordinary/current/working
are distinct, as are different model classes. Enabled facades are unhashable.
Comparison can trigger the normal lazy, working-thaw or absence behavior; it is
not an atomic snapshot of multiple field reads.

Eligible ordinary, const, lazy/static, binding and managed fields default to
`compare=True`. Initvar/classvar/transient/local fields are excluded.
`compare=False` belongs beside the field, not in a decorator mapping.

`managed(write_compare="value")` is a separate choice: it controls whether a
managed setter can skip an equal write; `"identity"` skips only the same reference.
During value-write detection, facade equality temporarily uses historical
node-state identity, including equality invoked inside callbacks, to preserve the
existing history contract. Ordering and hashing never change. For full edge cases
and legacy `compare="value"|"identity"`, see [the reference](API.md#optional-logical-comparisons).

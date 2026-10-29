# Edit collections

Keep stable committed values and expose an editable working form only during a
transaction. `thaw` prepares that form; `freeze` converts it back for publication.

```python
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
```

A working read thaws once per edit; repeated reads return the installed working
container. Reading it can mark a field touched even if you do not mutate it.
Ordinary reads do not implicitly thaw. Replacing a whole managed value through
an ordinary setter is also valid during a transaction.

## Escaped working containers

```python
working_items.append("too late")
assert shopping.items == ("bread", "milk")
```

Completion detaches the working container. It remains a Python object, but later
changes to it do not edit committed history. Do not keep it as the application's
current editable model.

Managed stable values include exact built-in scalars, recursive tuples and
frozensets, supported immutable mappings, and Undoable node references. Arbitrary
mutable/custom objects are not made stable merely by annotation. Supply a
conversion into the supported stable surface; otherwise freezing raises
`FrozenValueError`. Converters must be pure and separate working data from stable
data. See [initialization callbacks](Initialization.md#callback-argument-summary)
and [nested objects](ObjectGraphs.md).

# Initialize dependent values

Factory parameter names identify providers. Express the dependency where the
field is declared; you do not need a post-construction sequence of assignments.
Explicit constructor values bypass that field's default factory.

```python
from yidl_undoable import UndoRedoManager, initvar, lazy, managed, undoable

@undoable
class Rectangle:
    area: int = managed(default_factory=lambda width, height: width * height)
    width: int = managed(default=3)
    height: int = managed(default=4)
    scale: int = initvar(default=2)
    scaled_area: int = lazy(default_factory=lambda area, scale: area * scale)

history = UndoRedoManager()
rectangle = Rectangle(width=5, transaction_manager=history)
history.initialize(rectangle)
assert rectangle.area == 20 and rectangle.scaled_area == 40
assert not hasattr(rectangle, "scale")
```

Dependencies resolve even when declared later. Initvars are not public facade
fields; Undoable retains them privately for later factory use. A lazy dependency
can be materialized when needed by construction. Unknown named providers,
recursive dependencies and required unset lazy providers produce contextual errors.
Factories compute initial values; they are not reactive formulas. Changing
`width` later does not automatically recompute `area` or an already-read lazy value.

## Callback argument summary

| User function | Arguments it receives | Name significance |
| --- | --- | --- |
| Construction `default_factory` | Named field/initvar/classvar providers; `cls` is the generated model class | Names select providers; opt-in `self` requires `allow_self_factory=True` |
| Lazy `default_factory` on first read | Named providers read through the accessing facade; retained initvars; `cls` is the generated model | `self`, when enabled, is the accessing facade |
| Transient `working_default_factory` | The same named-provider machinery on the active accessing facade | No special `current`/`working` provider names; use opt-in `self.current`/`self.working` |
| `local_store(default_factory=...)` | No arguments | Must be zero-argument |
| `thaw` / `freeze` | One positional value | The parameter name is your choice; no injection |
| `@validate_commit(key)` method | Bound `self`, reading the candidate | No field or key argument injection |

Lambdas and named functions obey the same rules. During construction, opt-in
`self` can read only resolved baselines; it cannot safely bypass dependency ordering
or mutate the partially constructed node. After construction, access-time factories
can resolve other providers under the same callback fence. These rules are specific
to Undoable; do not import Lifecycle's special transient-provider rules by analogy.

`lazy`/`static` is shared nonversioned first-read storage. It is write-once unless
`mutable=True`; an unset lazy read fails, and a failed factory leaves the target
unset for a later pure retry. It does not rewind when history changes.

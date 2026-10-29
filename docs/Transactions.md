# Group and validate edits

One successful outer transaction becomes one undo step, even when it edits several
fields or objects. Begin and complete through the manager that owns those objects.

```python
from yidl_undoable import (
    DEFAULT_TRANSACTION, UndoRedoManager, managed, undoable, validate_commit,
)

@undoable
class Range:
    start: int = managed(default=0)
    end: int = managed(default=10)

    @validate_commit(DEFAULT_TRANSACTION)
    def valid_range(self):
        return self.start <= self.end

history = UndoRedoManager()
span = Range(transaction_manager=history)
history.initialize(span)
history.begin()
span.start = 20
try:
    history.validate()
except BaseExceptionGroup:
    span.end = 30
else:
    raise AssertionError("expected invalid preview")
assert history.active_transaction_for() is not None
history.commit()
assert (span.start, span.end) == (20, 30)
assert history.undo() and (span.start, span.end) == (0, 10)
```

`validate()` checks a frozen preview and leaves the edit open, so you can repair
it. Commit validates again. A final preparation/validation failure aborts the edit,
publishes nothing and preserves redo. An initialization failure is retryable.

Undoable validates each reachable node in its complete rooted candidate, including
untouched nodes, before publishing it. This differs from Lifecycle's participant
validation: Undoable enlists one aggregate history coordinator. Do not assume that
only an individually changed node's validators run. Candidate managed reads through
all views see frozen candidate values and never thaw.

Validators return exactly `False` or raise to reject; other return values accept.
They receive `self` only, with no field-name injection. Factories, converters and
validators must be pure: same-manager transactional reentry is rejected, and
external effects cannot be rolled back.

## Joined nesting is not a savepoint

```python
with history.begin():
    span.start = 1
    with history.begin():
        span.end = 2
assert (span.start, span.end) == (1, 2)
assert history.undo() and (span.start, span.end) == (0, 10)
```

An inner commit discharges a join; only the outer commit publishes. Rollback at
any depth aborts the whole joined edit. Do not manually complete a token and then
expect its context manager to complete the same edit again.

A manager can use a custom hashable key. Declare its managed/transient fields and
validators with that same key and pass the key explicitly to manager operations.
One manager does not offer multiple independent histories or multi-key atomic edits.
The [API reference](API.md#manager-operations) covers completion and fault diagnostics.

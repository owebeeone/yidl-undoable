"""Runnable companion to docs/Transactions.md."""

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


with history.begin():
    span.start = 1
    with history.begin():
        span.end = 2
assert (span.start, span.end) == (1, 2)
assert history.undo() and (span.start, span.end) == (0, 10)

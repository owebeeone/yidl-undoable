"""Synchronous historical write equality with expiring copied-context markers."""

from contextvars import ContextVar
from dataclasses import dataclass


@dataclass(slots=True)
class _HistoricalWriteScope:
    active: bool = True


_historical_write_scope: ContextVar[_HistoricalWriteScope | None] = ContextVar(
    "yidl_undoable_historical_write_scope", default=None
)


def _historical_write_equal(old, value):
    marker = _HistoricalWriteScope()
    token = _historical_write_scope.set(marker)
    try:
        return bool(old == value)
    finally:
        marker.active = False
        _historical_write_scope.reset(token)

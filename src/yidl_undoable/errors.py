"""Contextual public errors for schema, history and transaction operations."""

# Reusing the marker factories also preserves their immediate declaration errors.
from yidl_lifecycle.lifecycle_markers import (
    LifecycleDefinitionError as UndoableDefinitionError,
)


class TransactionRequiredError(RuntimeError):
    pass


class ObjectAbsentError(RuntimeError):
    pass


class UnavailableNodeError(RuntimeError):
    pass


class ForeignManagerError(RuntimeError):
    pass


class GraphCycleError(RuntimeError):
    pass


class FrozenValueError(TypeError):
    pass


class ReentrantOperationError(RuntimeError):
    pass


class HistoryFaultError(RuntimeError):
    pass

"""Generated historical application models and their transaction coordinator."""

from .undoable import undoable
from .transaction_yidl import UndoRedoManager, DEFAULT_TRANSACTION
from .undoable_markers import (
    binding,
    classvar,
    const,
    field,
    initvar,
    lazy,
    local_store,
    managed,
    static,
    transient,
    validate_commit,
)
from .errors import (
    UndoableDefinitionError,
    TransactionRequiredError,
    ObjectAbsentError,
    UnavailableNodeError,
    ForeignManagerError,
    GraphCycleError,
    FrozenValueError,
    ReentrantOperationError,
    HistoryFaultError,
)
from .policies import AbsentReadPolicy, RaiseAbsent, ReadLastVisible
from .snapshots import FrameSnapshot, SnapshotNode

__all__ = [
    "undoable",
    "UndoRedoManager",
    "DEFAULT_TRANSACTION",
    "AbsentReadPolicy",
    "RaiseAbsent",
    "ReadLastVisible",
    "FrameSnapshot",
    "SnapshotNode",
    "binding",
    "classvar",
    "const",
    "field",
    "initvar",
    "lazy",
    "local_store",
    "managed",
    "static",
    "transient",
    "validate_commit",
    "UndoableDefinitionError",
    "TransactionRequiredError",
    "ObjectAbsentError",
    "UnavailableNodeError",
    "ForeignManagerError",
    "GraphCycleError",
    "FrozenValueError",
    "ReentrantOperationError",
    "HistoryFaultError",
]

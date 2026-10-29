"""Fixed runtime captures for generated field-specific accessor bodies."""

from dataclasses import dataclass

from .bindings import map_binding, scalar_binding
from .callbacks import require_mutation
from .candidates import CandidateRead
from .comparison_captures import ComparisonCaptures
from .errors import TransactionRequiredError, UndoableDefinitionError
from .undoable_markers import MISSING


@dataclass(frozen=True, slots=True)
class AccessorCaptures(ComparisonCaptures):
    definition_error: object = UndoableDefinitionError
    transaction_error: object = TransactionRequiredError
    mutation_guard: object = require_mutation
    candidate_type: object = CandidateRead
    scalar_binding: object = scalar_binding
    map_binding: object = map_binding
    missing: object = MISSING

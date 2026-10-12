"""Before/after deletion removes field-local policy and provider availability."""

import pytest
from yidl_undoable import *


@undoable(eq=True, order=True)
class Before:
    value: int = managed(default=2, compare=True, write_compare="identity")
    note: str = field(default="one", compare=False)


@undoable(eq=True, order=True)
class After:
    value: int = managed(default=2, compare=True, write_compare="identity")


@undoable(eq=True)
class Excluded:
    value: int = managed(default=2, compare=False, write_compare="value")
    label: str = const(default="stable")


for model in (Before, After, Excluded):
    h = UndoRedoManager()
    a = model(transaction_manager=h)
    b = model(transaction_manager=h)
    h.initialize(a, b)
    assert a == b
    with h.begin():
        a.value = 3
    assert (a != b) is (model is not Excluded)
    if model is not Excluded:
        assert b < a
assert (
    "note" in Before.__undoable_schema__.logical
    and "note" not in After.__undoable_schema__.logical
)
assert "note" not in After.__undoable_schema__.by_name
assert After.__undoable_schema__.by_name["value"]["compare"] == "identity"
with pytest.raises(UndoableDefinitionError, match="unknown provider removed"):

    @undoable(eq=True)
    class MissingProvider:
        result: int = lazy(default_factory=lambda removed: removed)

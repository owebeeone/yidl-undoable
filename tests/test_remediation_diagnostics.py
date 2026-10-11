import pytest
from yidl_undoable import *


@pytest.mark.parametrize("recursive", (False, True))
def test_unusable_lazy_constructor_dependency_is_contextual_and_unregistered(recursive):
    marker = lazy(default_factory=lambda target: target) if recursive else lazy()

    @undoable
    class Model:
        target: object = const(default_factory=lambda source: source)
        source: object = marker

    h = UndoRedoManager()
    with pytest.raises(UndoableDefinitionError, match="source|recursive"):
        Model(transaction_manager=h)
    assert h._nodes == {} and h._selection is None

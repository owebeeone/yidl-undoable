import pytest
from yidl_undoable.history import FieldHistory
from yidl_undoable import UnavailableNodeError


def test_predecessor_and_trim_boundary():
    h = FieldHistory((3, 8), ("a", "b"))
    with pytest.raises(UnavailableNodeError):
        h.at(2)
    assert h.at(3) == h.at(6) == "a"
    assert h.trim(6) == FieldHistory((3,), ("a",))
    assert h.trim(2) == FieldHistory()

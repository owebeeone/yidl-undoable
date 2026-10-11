from types import MappingProxyType
import pytest
from yidl_undoable import *


@undoable
class Node:
    value: tuple = managed(default=(), thaw=list, freeze=tuple)
    untouched: tuple = managed(default=("baseline",), thaw=list, freeze=tuple)
    children: tuple = managed(default=())
    nested: object = managed(default=None)


h = UndoRedoManager()
child = Node(transaction_manager=h)
h.initialize(child)
with h.begin():
    child.working.value.append("pending")
    current_parent = Node(
        children=(child.current,),
        nested=MappingProxyType(
            {"aliases": (child.current, frozenset((child.default,)))}
        ),
        transaction_manager=h,
    )
    default_parent = Node(children=(child.default,), transaction_manager=h)
    for parent in (current_parent, default_parent):
        for attached in (False, True):
            assert parent.children[0] is child.default
            assert parent.default.children[0].value == ["pending"]
            assert parent.children[0].untouched == ("baseline",)
            assert (child.node_id, "untouched") not in h._edit.touched
            assert parent.working.children[0] is child.working
            with pytest.raises(ObjectAbsentError):
                _ = parent.current.children
            if not attached:
                h.add_root(parent)
    nested = current_parent.nested["aliases"]
    assert nested[0] is child.default and next(iter(nested[1])) is child.default
    working_nested = current_parent.working.nested["aliases"]
    assert (
        working_nested[0] is child.working
        and next(iter(working_nested[1])) is child.working
    )
    current_parent.working.children[0].untouched.append("nested")
assert current_parent.children[0] is child.default and child.value == ("pending",)
assert default_parent.current.children[0] is child.current
assert child.untouched == ("baseline", "nested")

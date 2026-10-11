import pytest
from yidl_undoable import *

h = UndoRedoManager()
a = None
attempt = ["pure"]


def converter(value):
    if attempt[0] == "rollback":
        h.rollback()
    elif attempt[0] == "begin":
        h.begin()
    return list(value)


@undoable
class Node:
    value: int = managed(default=0)
    items: tuple = managed(default=(), thaw=converter, freeze=tuple)


x = Node(transaction_manager=h)
h.initialize(x)
token = h.begin()
x.value = 1
attempt[0] = "rollback"
with pytest.raises(ReentrantOperationError):
    _ = x.working.items
assert h.active_transaction_for() is token and x.value == 1
assert (x.node_id, "items") not in h._edit.touched
attempt[0] = "pure"
assert x.working.items == []
h.rollback()


class EqualAttack:
    def __eq__(self, other):
        h.rollback()
        h.begin()
        return False


h.begin()
with pytest.raises(ReentrantOperationError):
    x.value = EqualAttack()
assert x.value == 0
h.rollback()


class Truth:
    def __bool__(self):
        h.rollback()
        return False


class TruthAttack:
    def __eq__(self, other):
        return Truth()


h.begin()
with pytest.raises(ReentrantOperationError):
    x.value = TruthAttack()
assert x.value == 0
h.rollback()

scratch_mode = ["scope"]
scope = None


def scratch_factory():
    if scratch_mode[0] == "scope":
        scope.__exit__(None, None, None)
    return []


@undoable
class Scratch:
    value: int = managed(default=0)
    scratch: list = transient(
        default_factory=list, working_default_factory=scratch_factory
    )


s = Scratch(transaction_manager=(hs := UndoRedoManager()))
hs.initialize(s)
scope = hs.begin()
with pytest.raises(ReentrantOperationError):
    _ = s.scratch
assert hs.active_transaction_for() is scope and not hs._edit.transient
scratch_mode[0] = "pure"
assert s.scratch == []
hs.rollback()

lazy_mode = ["begin"]


def lazy_factory():
    if lazy_mode[0] == "begin":
        hl.begin()
    elif lazy_mode[0] == "undo":
        hl.undo()
    return {"value": 1}


@undoable
class Lazy:
    value: int = managed(default=0)
    delayed: object = lazy(default_factory=lazy_factory)


hl = UndoRedoManager()
l = Lazy(transaction_manager=hl)
hl.initialize(l)
for mode, view in [("begin", l), ("undo", l.current)]:
    lazy_mode[0] = mode
    with pytest.raises(ReentrantOperationError):
        _ = view.delayed
    assert hl.active_transaction_for() is None and hl.frame_count == 1
lazy_mode[0] = "pure"
assert l.working.delayed is l.current.delayed is l.delayed
assert hl.frame_count == 1

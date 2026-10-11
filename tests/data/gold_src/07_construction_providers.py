import pytest
from yidl_undoable import *

seen = []


def derive(base):
    return base * 2


def self_derive(self):
    seen.append((self.base, self.default.base, self.current.base, self.working.base))
    return self.base + 1


@undoable
class Constructed:
    # Out of dependency order proves normalized provider ordering.
    doubled: int = managed(default_factory=derive)
    base: int = managed(default=3)
    derived: int = managed(default_factory=self_derive, allow_self_factory=True)


h = UndoRedoManager()
x = Constructed(transaction_manager=h)
assert x.base == 3 and x.doubled == 6 and x.derived == 4
assert seen == [(3, 3, 3, 3)] and h._selection is None
h.initialize(x)
with h.begin():
    y = Constructed(base=7, transaction_manager=h)
    assert (y.base, y.doubled, y.derived) == (7, 14, 8)
    assert seen[-1] == (7, 7, 7, 7)
    h.add_root(y)
assert y.derived == 8


@undoable
class Unresolved:
    first: int = managed(
        default_factory=lambda self: self.later, allow_self_factory=True
    )
    later: int = managed(default=4)


count = len(h._nodes)
with h.begin():
    with pytest.raises(UndoableDefinitionError, match="unresolved"):
        Unresolved(transaction_manager=h)
    assert len(h._nodes) == count
assert h.roots == (x, y)


@undoable
class Recursive:
    a: int = managed(default_factory=lambda b: b)
    b: int = managed(default_factory=lambda a: a)


with h.begin():
    with pytest.raises(UndoableDefinitionError, match="recursive"):
        Recursive(transaction_manager=h)
    assert len(h._nodes) == count


# Self assignment during constructor cannot edit a partially registered node.
def writes(self):
    self.base = 9
    return 1


@undoable
class ConstructorWrite:
    base: int = managed(default=1)
    bad: int = managed(default_factory=writes, allow_self_factory=True)


with h.begin():
    with pytest.raises(ReentrantOperationError):
        ConstructorWrite(transaction_manager=h)
    assert len(h._nodes) == count

"""Additional accepted boundary stories without duplicating canonical success paths."""

import pytest
from types import MappingProxyType
from yidl_undoable import *

mode = ["attack"]


def freeze(value):
    if mode[0] == "attack":
        h.initialize(root)
    return tuple(value)


@undoable
class Node:
    values: tuple = managed(default=(), thaw=list, freeze=freeze)
    membership: frozenset = managed(default=frozenset({"a"}))
    edges: object = managed(default=MappingProxyType({}))


h = UndoRedoManager()
root = Node(transaction_manager=h)
with pytest.raises(ReentrantOperationError):
    h.initialize(root)
assert h._selection is None
mode[0] = "pure"
h.initialize(root)
with h.begin():
    child = Node(transaction_manager=h)
    root.edges = MappingProxyType({"nested": (child,)})
assert root.edges["nested"][0].present
assert root.current.edges["nested"][0]._u_view == "current"
assert root.working.edges["nested"][0]._u_view == "working"
assert root.membership == frozenset({"a"})
# Inner exceptional scope closes the joined edit; the stale outer exceptional exit
# preserves the exact body exception and cannot close a replacement token.
original = ValueError("original body")
outer = h.begin()
inner = h.begin()
with pytest.raises(ValueError) as caught:
    with inner:
        raise original
assert caught.value is original and h.active_transaction_for() is None
replacement = h.begin()
assert outer.__exit__(ValueError, original, None) is False
assert h.active_transaction_for() is replacement
h.rollback()
# An uninitialized omitted node never gains a baseline merely by Python retention.
setup = UndoRedoManager()
present = Node(transaction_manager=setup)
omitted = Node(transaction_manager=setup)
setup.initialize(present)
with setup.begin():
    with pytest.raises(UnavailableNodeError):
        setup.add_root(omitted)
# Construction while healthy idle after initialize needs an edit.
with pytest.raises(TransactionRequiredError):
    Node(transaction_manager=setup)
# Fresh idle lazy materializations through each mode share one result per node.
calls = []


def lazy_value():
    calls.append(1)
    return object()


@undoable
class Lazy:
    data: int = managed(default=0)
    once: object = lazy(default_factory=lazy_value)


lh = UndoRedoManager()
models = [Lazy(transaction_manager=lh) for _ in range(3)]
lh.initialize(*models)
for node, view in zip(models, ("default", "current", "working")):
    initial = getattr(node, view).once
    assert node.once is node.current.once is node.working.once is initial
assert len(calls) == 3 and lh.frame_count == 1 and lh.active_transaction_for() is None

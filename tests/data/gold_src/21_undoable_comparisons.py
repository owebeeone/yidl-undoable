"""Logical comparison contrasts fields, views, revisions and disabled identity."""

import pytest
from yidl_undoable import *

calls = []


def stamp(seed):
    calls.append(seed)
    return seed


@undoable(eq=True, order=True)
class Quote:
    seed: int = initvar(default=3, compare=False)
    shared: int = classvar(default=9, compare=False)
    sku: str = const(default="A")
    price: int = managed(default=2, compare=True, write_compare="value")
    note: str = field(default="", compare=False)
    stamp: int = lazy(default_factory=stamp)
    resource: object = binding(default=None)
    scratch: list = transient(default_factory=list, compare=False)
    cache: dict = local_store(default_factory=dict, compare=False)


h = UndoRedoManager()
a = Quote(note="one", transaction_manager=h)
b = Quote(note="two", transaction_manager=h)
h.initialize(a, b)
assert calls == []
assert a == b and calls == [3, 3]
assert a.current == b.current and a.working == b.working
assert a.__eq__(a.current) is NotImplemented
assert a.current.__eq__(a.working) is NotImplemented
for item in (a, a.current, a.working):
    with pytest.raises(TypeError):
        hash(item)
a.cache["local"] = "changed"
a.scratch.append("discarded")
assert a == b
old = a._u_state.facade("current", (h._selection.epoch, h.cursor))
with h.begin():
    a.price = 5
    assert a > b and a.working > b.working and a.current == b.current
    assert h.frame_count == 1
assert old.price == 2 and a.current.price == 5 and not (old < b.current)
assert old == b.current and h.undo() and a == b and h.redo() and a > b
snapshot = h.snapshot()
assert snapshot.node(a.node_id) == snapshot.node(a.node_id)
assert hash(snapshot.node(a.node_id))


@undoable
class Identity:
    price: int = managed(default=2)


plain_history = UndoRedoManager()
x = Identity(transaction_manager=plain_history)
y = Identity(transaction_manager=plain_history)
plain_history.initialize(x, y)
assert x != y and x == x.current == x.working and hash(x) == hash(x.current)
assert a.__eq__(x) is NotImplemented


@undoable()
class EmptyDisabled:
    pass


@undoable(eq=False, order=False)
class ExplicitDisabled:
    pass


for model in (EmptyDisabled, ExplicitDisabled):
    instance = model(transaction_manager=UndoRedoManager())
    assert instance == instance.current and hash(instance)


@undoable(eq=True)
class Child(Quote):
    price: int = managed(default=4, compare=False, write_compare="identity")
    extra: int = field(default=8)


children = UndoRedoManager()
c = Child(price=4, transaction_manager=children)
d = Child(price=6, transaction_manager=children)
children.initialize(c, d)
assert c == d and c.__eq__(a) is NotImplemented
assert Child.__undoable_schema__.by_name["price"]["compare"] == "identity"
assert Child.__undoable_schema__.by_name["price"]["logical_compare"] is False

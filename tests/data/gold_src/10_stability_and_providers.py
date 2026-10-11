import pytest
from types import MappingProxyType
from yidl_undoable import *


@undoable
class Node:
    value: int = managed(default=0)
    children: tuple = managed(default=(), thaw=list, freeze=tuple)
    mapping: object = managed(default=MappingProxyType({}))


h = UndoRedoManager()
c = Node(transaction_manager=h)
r = Node(children=(c,), transaction_manager=h)
h.initialize(r)
with h.begin():
    working = r.working.children
    assert working[0]._u_view == "working"
    assert r.children[0]._u_view == "default"
    working.append(c.current)
    assert r.working.children is working
    assert working[1]._u_view == "working"
    assert all(x._u_view == "default" for x in r.children)
    c.value = 3
    assert r.current.children[0].value == 0
assert r.children == (c, c)
working.append(c)
assert len(r.children) == 2
# A setter comparison never initiates thawing merely to skip an equal value.
with h.begin():
    r.working.children = r.children
    assert (r.node_id, "children") not in h._edit.touched
    assert r.working.children[0]._u_view == "working"


# Provisional construction is allowed inside a pure provider, with shared ownership.
def make_child(self):
    return (Node(value=self.value, transaction_manager=self.transaction_manager),)


@undoable
class Parent:
    value: int = managed(default=4)
    children: tuple = managed(default_factory=make_child, allow_self_factory=True)


setup = UndoRedoManager()
p = Parent(transaction_manager=setup)
setup.initialize(p)
assert p.children[0].value == 4
with setup.begin():
    q = Parent(value=8, transaction_manager=setup)
    setup.add_root(q)
assert q.children[0].value == 8
# Nested lazy providers share a fence; recursive materialization is contextual.
lazy_calls = []


def first():
    lazy_calls.append(1)
    return 5


@undoable
class Providers:
    x: int = managed(default=0)
    a: int = lazy(default_factory=first)
    b: int = lazy(default_factory=lambda a: a + 1)
    recursive: int = lazy(
        default_factory=lambda self: self.recursive, allow_self_factory=True
    )


ph = UndoRedoManager()
pv = Providers(transaction_manager=ph)
ph.initialize(pv)
assert pv.current.b == 6 and pv.working.a == 5 and lazy_calls == [1]
with pytest.raises(UndoableDefinitionError, match="recursive"):
    _ = pv.recursive
# Recursive working providers fail without an overlay and can retry pure.
mode = ["recursive"]


def transient_provider(self):
    return self.scratch if mode[0] == "recursive" else []


@undoable
class Scratch:
    x: int = managed(default=0)
    scratch: list = transient(
        default_factory=list,
        working_default_factory=transient_provider,
        allow_self_factory=True,
    )


sh = UndoRedoManager()
s = Scratch(transaction_manager=sh)
sh.initialize(s)
with sh.begin():
    with pytest.raises(UndoableDefinitionError, match="recursive"):
        _ = s.scratch
    assert not sh._edit.transient
    mode[0] = "pure"
    assert s.scratch == []
assert s.scratch == [] and sh.frame_count == 2
assert sh._selection.epoch.nodes[s.node_id].fields["x"].frame_ids == (0,)

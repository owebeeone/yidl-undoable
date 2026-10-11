from yidl_undoable import *

calls = []


def source():
    calls.append(1)
    return 7


@undoable
class Forward:
    source: int = lazy(default_factory=source)
    constant: int = const(default_factory=lambda source: source)
    value: int = managed(default_factory=lambda source: source)


@undoable
class Reverse:
    value: int = managed(default_factory=lambda source: source)
    constant: int = const(default_factory=lambda source: source)
    source: int = lazy(default_factory=source)


h = UndoRedoManager()
one, two = Forward(transaction_manager=h), Reverse(transaction_manager=h)
assert one.constant == one.value == two.constant == two.value == 7
assert len(calls) == 2
h.initialize(one, two)
with h.begin():
    three = Reverse(transaction_manager=h)
    assert three.constant == three.value == three.working.value == 7
    h.add_root(three)
assert len(calls) == 3
for node in (one, two, three):
    assert node.source == node.current.source == node.working.source == 7
assert len(calls) == 3

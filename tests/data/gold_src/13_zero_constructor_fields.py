from inspect import signature, Parameter
from yidl_undoable import *


@undoable
class Empty:
    pass


@undoable
class ScratchOnly:
    cache: dict = local_store(default_factory=dict)


@undoable
class ClassOnly:
    label: str = classvar(default="node")


@undoable
class NoInputs:
    value: int = managed(default=0, init=False)


h = UndoRedoManager()
nodes = [
    kind(transaction_manager=h) for kind in (Empty, ScratchOnly, ClassOnly, NoInputs)
]
h.initialize(*nodes)
for kind in (Empty, ScratchOnly, ClassOnly, NoInputs):
    params = signature(kind).parameters
    assert tuple(params) == ("transaction_manager",)
    assert params["transaction_manager"].kind is Parameter.KEYWORD_ONLY
    assert params["transaction_manager"].default is Parameter.empty
assert all(node.present for node in nodes)
nodes[1].cache["entry"] = 1
assert nodes[1].current.cache is nodes[1].working.cache
assert nodes[2].label == "node"
with h.begin():
    nodes[3].value = 7
assert nodes[3].value == 7
assert h.undo() and nodes[3].value == 0 and nodes[1].cache == {"entry": 1}

"""Live annotations accompany unchanged construction and history behavior."""

from inspect import Parameter, signature

from yidl_undoable import UndoRedoManager, const, initvar, managed, undoable
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY


class Payload:
    pass


token = Payload()
calls = []


def make_label(seed):
    calls.append(seed)
    return seed.upper()


@undoable
class Model:
    required: str = const()
    payload: Payload = const(default=token)
    seed: str = initvar(default="node")
    label: str = managed(default_factory=make_label)
    count: int = managed(default=2)


params = signature(Model).parameters
assert params["payload"].annotation is Payload
assert params["required"].default is Parameter.empty
assert params["label"].default is _HAS_DEFAULT_FACTORY
assert Model.__undoable_schema__.by_name["payload"]["default_value"] is token
assert Model.__undoable_schema__.by_name["label"]["default_factory"] is make_label
history = UndoRedoManager()
node = Model(required="root", transaction_manager=history)
assert node.required == "root" and node.payload is token
assert node.label == "NODE" and node.count == 2 and calls == ["node"]
history.initialize(node)
with history.begin():
    node.count = 3
    assert node.current.count == 2 and node.working.count == 3
assert history.undo() and node.count == 2
assert history.redo() and node.count == 3
with history.begin():
    other = Model(required="other", label="explicit", transaction_manager=history)
    history.add_root(other)
assert other.label == "explicit" and calls == ["node"]

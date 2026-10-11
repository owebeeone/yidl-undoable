import pytest
from yidl_undoable import *
from yidl_lifecycle.bindings import BindingBase

calls = []


def scratch(seed):
    return [seed]


def compute(seed):
    calls.append(seed)
    return {"computed": seed}


@undoable
class Fields:
    seed: int = initvar(default=3)
    constant: list = const(default_factory=list)
    plain: int = field(default=0)
    resource: object = binding(default=None)
    cache: dict = local_store(default_factory=dict)
    delayed: dict = lazy(default_factory=compute)
    replaceable: int = lazy(default=5, mutable=True)
    temporary: list = transient(default_factory=list, working_default_factory=scratch)
    value: int = managed(default=0)
    class_value: int = classvar(default=9)


h = UndoRedoManager()
a = Fields(transaction_manager=h)
b = Fields(seed=7, transaction_manager=h)
h.initialize(a, b)
resource = BindingBase()
assert a.constant is not b.constant and a.cache is not b.cache
assert a.delayed == {"computed": 3}
assert a.current.delayed is a.working.delayed is a.delayed and calls == [3]
assert h.frame_count == 1 and h.active_transaction_for() is None
with pytest.raises(AttributeError):
    a.delayed = {}
a.replaceable = 6
assert a.current.replaceable == 6
with pytest.raises(AttributeError):
    a.constant = []
a.constant.append("shared")
with h.begin():
    baseline = a.current.temporary
    assert baseline == []
    assert a.temporary == [3]
    assert a.working.temporary is a.temporary
    a.temporary.append("discard")
    a.plain = 8
    a.resource = resource
    a.cache["x"] = 1
    a.value = 8
    h.remove_root(b)
    b.temporary = ["removed"]
assert a.temporary == baseline == [] and b.temporary == []
assert (
    a.constant == ["shared"]
    and a.resource is resource
    and not resource.is_accepted
    and not resource.is_closed
)
assert h.undo() and a.value == 0 and a.plain == 8 and a.cache == {"x": 1}
assert a.temporary == [] and a.replaceable == 6
with pytest.raises(TransactionRequiredError):
    a.temporary = []
with h.begin():
    with pytest.raises(TransactionRequiredError):
        a.current.temporary = []
    a.working.temporary = ["fresh"]
assert a.temporary == []
assert a.class_value == b.class_value == 9
assert not hasattr(a, "seed")


@undoable
class Sub(Fields):
    value: int = managed(default=10)
    extra: str = managed(default="extra")


sub_history = UndoRedoManager()
s = Sub(transaction_manager=sub_history)
sub_history.initialize(s)
assert s.value == 10 and s.extra == "extra" and s.class_value == 9
with sub_history.begin():
    s.value = 12
assert sub_history.undo() and s.value == 10
assert (
    Sub.__undoable_schema__.by_name["value"]["field_id"]
    == Fields.__undoable_schema__.by_name["value"]["field_id"]
)
custom = UndoRedoManager(tx_key="custom")


@undoable
class Custom:
    value: int = managed("custom", default=0)


x = Custom(transaction_manager=custom)
custom.initialize(x)
with custom.begin("custom"):
    x.value = 1
assert x.value == 1
with pytest.raises(RuntimeError):
    custom.begin()

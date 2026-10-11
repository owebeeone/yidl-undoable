import pytest
from yidl_undoable import *
from types import MappingProxyType


@undoable
class Checked:
    value: int = managed(default=0)
    items: tuple = managed(default=(), thaw=list, freeze=tuple)
    valid: bool = field(default=True)
    seen: list = local_store(default_factory=list)
    attack: object = field(default=None)

    @validate_commit(DEFAULT_TRANSACTION)
    def check(self):
        self.seen.append(
            (self.value, self.current.value, self.working.value, type(self.items))
        )
        if self.attack is not None:
            self.attack()
        if not self.valid:
            raise ValueError(f"invalid {self.node_id}")
        return self.value >= 0


h = UndoRedoManager()
a = Checked(transaction_manager=h)
b = Checked(transaction_manager=h)
h.initialize(a, b)
assert a.seen == [(0, 0, 0, tuple)]
with h.begin():
    a.value = 1
    b.value = 2
assert a.seen[-1] == (1, 1, 1, tuple)
assert h.undo()
h.begin()
a.value = 5
b.value = -1
with pytest.raises(BaseExceptionGroup):
    h.validate()
assert h.active_transaction_for() is not None and a.value == 5
b.value = 3
h.validate()
assert h.frame_id == 0 and h.frame_count == 2
b.valid = False
with pytest.raises(BaseExceptionGroup):
    h.commit()
assert h.active_transaction_for() is None and a.value == b.value == 0 and h.can_redo()
b.valid = True
assert h.redo() and (a.value, b.value) == (1, 2)
assert h.undo()
h.begin()
a.value = 7
b.attack = lambda: h.begin()
with pytest.raises(BaseExceptionGroup):
    h.commit()
assert a.value == 0 and h.can_redo()
b.attack = None


# Freeze of a later node fails without publication of an earlier prepared field.
def freeze(value):
    if value == "bad":
        raise ValueError("bad freeze")
    return value


@undoable
class Frozen:
    data: object = managed(default=0, freeze=freeze)


hf = UndoRedoManager()
one = Frozen(transaction_manager=hf)
two = Frozen(transaction_manager=hf)
hf.initialize(one, two)
old = hf.snapshot()
hf.begin()
one.data = 10
two.data = "bad"
with pytest.raises(ValueError):
    hf.commit()
assert one.data == two.data == 0 and hf.frame_count == 1
assert old.node(one.node_id).get("data") == 0
hf.begin()
one.data = []
with pytest.raises(FrozenValueError):
    hf.commit()
assert one.data == 0
# Read-only mapping freezes own a private immutable copy.
backing = {"x": (1,)}


@undoable
class MappingNode:
    mapping: object = managed(default=MappingProxyType(backing))


hm = UndoRedoManager()
m = MappingNode(transaction_manager=hm)
hm.initialize(m)
backing["x"] = (9,)
assert m.mapping["x"] == (1,)
# Failed initialization preserves setup and can retry pure validation.
hi = UndoRedoManager()
i = Checked(valid=False, transaction_manager=hi)
with pytest.raises(BaseExceptionGroup):
    hi.initialize(i)
assert hi._selection is None
i.valid = True
hi.initialize(i)

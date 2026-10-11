import pytest
from yidl_undoable import *

mode = ["pure"]
scope = None


def provider(self, value):
    if mode[0] == "scope":
        scope.__exit__(None, None, None)
    elif mode[0] == "write":
        self.value = 99
    return value * 2


@undoable
class Model:
    value: int = managed(default=0)
    scratch: int = transient(default=0)
    sourced: int = transient(
        default=0, working_default_factory=provider, allow_self_factory=True
    )
    seen: list = local_store(default_factory=list)

    @validate_commit(DEFAULT_TRANSACTION)
    def check(self):
        self.seen.append(
            (
                self.scratch,
                self.default.scratch,
                self.current.scratch,
                self.working.scratch,
                self.sourced,
            )
        )
        return self.scratch >= 0


h = UndoRedoManager()
x = Model(transaction_manager=h)
h.initialize(x)
with h.begin():
    x.value = 1
    x.scratch = 1
assert x.seen[-1] == (1, 1, 0, 1, 2)
assert x.scratch == x.sourced == 0
assert h.undo()
h.begin()
x.value = 5
x.scratch = -1
with pytest.raises(BaseExceptionGroup):
    h.validate()
assert x.seen[-1] == (-1, -1, 0, -1, 10)
assert h.active_transaction_for() is not None and x.value == 5
x.scratch = 1
h.validate()
x.scratch = -1
with pytest.raises(BaseExceptionGroup):
    h.commit()
assert x.value == 0 and x.scratch == 0 and h.can_redo()
for attack in ("scope", "write"):
    scope = h.begin()
    x.value = 3
    mode[0] = attack
    with pytest.raises(BaseExceptionGroup) as caught:
        h.validate()
    assert isinstance(caught.value.exceptions[0], ReentrantOperationError)
    assert h.active_transaction_for() is scope and x.value == 3
    assert (x.node_id, "sourced") not in h._edit.transient
    mode[0] = "pure"
    h.validate()
    assert x.seen[-1] == (0, 0, 0, 0, 6)
    h.rollback()
with h.begin():
    x.value = 4
    x.scratch = 2
assert x.value == 4 and x.scratch == x.sourced == 0

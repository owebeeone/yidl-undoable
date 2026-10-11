import pytest
from yidl_undoable import *


class Truth:
    def __init__(self, result):
        self.result = result

    def __bool__(self):
        return self.result


class Key:
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return Truth(isinstance(other, Key) and self.name == other.name)

    def __ne__(self, other):
        return Truth(not bool(self == other))

    def __repr__(self):
        return self.name


key, alias, wrong = Key("edit"), Key("edit"), Key("wrong")


@undoable
class Model:
    value: int = managed(key, default=0)
    temporary: int = transient(key, default=0)

    @validate_commit(key)
    def valid(self):
        active = self.transaction_manager.active_transaction_for(alias)
        return active is None or active.tx_key is key


h = UndoRedoManager(tx_key=key)
node = Model(transaction_manager=h)
h.initialize(node)
with h.begin(alias) as token:
    assert token.tx_key is key and h.tx_key is key
    node.value = 7
    with h.begin(key) as joined:
        assert joined is token
        node.temporary = 3
    assert h.active_transaction_for(alias) is token and h.frame_count == 1
    h.validate(alias)
    with pytest.raises(RuntimeError, match="unknown transaction key"):
        h.commit(wrong)
    assert h.active_transaction_for(key) is token and node.value == 7
assert h.frame_count == 2 and node.value == 7 and node.temporary == 0
with pytest.raises(ValueError, match="body"):
    with h.begin(alias):
        node.value = 9
        with h.begin(key):
            raise ValueError("body")
assert node.value == 7 and h.active_transaction_for(key) is None
old = h.begin(alias)
h.rollback(key)
replacement = h.begin(key)
with pytest.raises(RuntimeError, match="stale"):
    old.__exit__(None, None, None)
assert old.__exit__(ValueError, ValueError("stale body"), None) is False
assert h.active_transaction_for(alias) is replacement
replacement.__exit__(None, None, None)
assert h.frame_count == 3 and node.value == 7

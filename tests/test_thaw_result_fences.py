from collections.abc import Mapping
from types import MappingProxyType
import pytest
from yidl_undoable import *


@pytest.mark.parametrize("provisional", (False, True))
@pytest.mark.parametrize("attack", ("rollback", "replace", "scope", "raise"))
def test_thaw_result_projection_retains_original_edit(provisional, attack):
    mode = [attack]

    class ResultMap(Mapping):
        def __iter__(self):
            action, mode[0] = mode[0], "pure"
            if action == "raise":
                raise LookupError("result traversal")
            if action == "scope":
                token.__exit__(None, None, None)
            elif action == "replace":
                h.rollback()
                h.begin()
            elif action == "rollback":
                h.rollback()
            return iter(("value",))

        def __len__(self):
            return 1

        def __getitem__(self, key):
            return 1

    @undoable
    class Node:
        pending: int = managed(default=0)
        target: object = managed(
            default=MappingProxyType({}),
            thaw=lambda value: MappingProxyType(ResultMap()),
            freeze=MappingProxyType,
        )

    h = UndoRedoManager()
    root = Node(transaction_manager=h)
    h.initialize(root)
    token = h.begin()
    root.pending = 7
    target = Node(transaction_manager=h) if provisional else root
    expected = LookupError if attack == "raise" else ReentrantOperationError
    with pytest.raises(expected):
        _ = target.working.target
    assert h.active_transaction_for() is token and token.completion is None
    assert root.pending == 7 and h._backend.begin_count == 1 and h.frame_count == 1
    assert (target.node_id, "target") not in h._edit.touched
    first = target.working.target
    assert first == {"value": 1} and target.working.target is first
    if provisional:
        h.add_root(target)
    h.commit()
    assert root.pending == 7 and target.target == {"value": 1}

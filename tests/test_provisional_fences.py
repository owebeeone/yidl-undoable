from collections.abc import Mapping
from types import MappingProxyType
import pytest
from yidl_undoable import *


@pytest.mark.parametrize("view", ("default", "working"))
@pytest.mark.parametrize("attack", ("rollback", "undo", "begin", "scope", "replace"))
def test_provisional_proxy_projection_owns_original_edit(view, attack):
    mode = [attack]

    class ProviderMap(Mapping):
        def __iter__(self):
            action, mode[0] = mode[0], "pure"
            if action == "scope":
                token.__exit__(None, None, None)
            elif action == "replace":
                h.rollback()
                h.begin()
            elif action != "pure":
                getattr(h, action)()
            return iter(("value",))

        def __len__(self):
            return 1

        def __getitem__(self, key):
            return 1

    @undoable
    class Node:
        value: object = managed(
            default=MappingProxyType({}), thaw=dict, freeze=MappingProxyType
        )

    h = UndoRedoManager()
    root = Node(transaction_manager=h)
    h.initialize(root)
    token = h.begin()
    root.value = MappingProxyType({"pending": 9})
    child = Node(value=MappingProxyType(ProviderMap()), transaction_manager=h)
    with pytest.raises(ReentrantOperationError):
        _ = getattr(child, view).value
    assert h.active_transaction_for() is token and token.completion is None
    assert root.value == {"pending": 9} and h.frame_count == 1
    assert (child.node_id, "value") not in h._edit.touched
    assert getattr(child, view).value == {"value": 1}
    assert ((child.node_id, "value") in h._edit.touched) is (view == "working")
    h.add_root(child)
    h.commit()
    assert root.value == {"pending": 9} and child.value == {"value": 1}

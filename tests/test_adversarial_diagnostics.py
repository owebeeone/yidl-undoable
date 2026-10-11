"""Diagnostics and synthetic failures that are awkward as successful goldens."""

import pytest
from types import MappingProxyType
from yidl_undoable import *


def test_validator_failures_are_grouped_with_node_context():
    @undoable
    class Model:
        value: int = managed(default=0)

        @validate_commit(DEFAULT_TRANSACTION)
        def reject(self):
            raise LookupError("rejected")

    h = UndoRedoManager()
    a, b = Model(transaction_manager=h), Model(transaction_manager=h)
    with pytest.raises(BaseExceptionGroup) as caught:
        h.initialize(a, b)
    assert len(caught.value.exceptions) == 2
    for node, error in zip((a, b), caught.value.exceptions):
        assert isinstance(error, LookupError)
        assert f"node {node.node_id}" in "\n".join(error.__notes__)
    assert h._selection is None


def test_pending_mapping_proxy_traversal_cannot_complete_its_edit():
    from collections.abc import Mapping

    class ProviderMap(Mapping):
        def __iter__(self):
            h.rollback()
            return iter(("value",))

        def __len__(self):
            return 1

        def __getitem__(self, key):
            return 1

    @undoable
    class Model:
        value: object = managed(
            default=None,
            thaw=lambda _: MappingProxyType(ProviderMap()),
            freeze=lambda _: None,
        )

    h = UndoRedoManager()
    node = Model(transaction_manager=h)
    h.initialize(node)
    token = h.begin()
    _ = node.working.value
    with pytest.raises(ReentrantOperationError):
        _ = node.value
    assert h.active_transaction_for() is token
    h.rollback()


def test_invalid_mapping_node_key_and_container_cycle():
    @undoable
    class Model:
        value: object = managed(default=None, freeze=lambda value: value)

    h = UndoRedoManager()
    node = Model(transaction_manager=h)
    node._u_state.values["value"] = MappingProxyType({node: 1})
    with pytest.raises(FrozenValueError, match="keys"):
        h.initialize(node)
    node._u_state.values["value"] = None
    h.initialize(node)
    recursive = []
    recursive.append(recursive)
    h.begin()
    node.value = recursive
    with pytest.raises(FrozenValueError):
        h.commit()
    assert node.value is None and h.frame_count == 1


def test_callback_detects_private_backend_replacement_without_installing_result():
    mode = ["attack"]

    def factory():
        if mode[0] == "attack":
            h._backend.begin()
        return 5

    @undoable
    class Model:
        value: int = managed(default=0)
        delayed: int = lazy(default_factory=factory)

    h = UndoRedoManager()
    node = Model(transaction_manager=h)
    h.initialize(node)
    with pytest.raises(HistoryFaultError):
        _ = node.delayed
    from yidl_undoable.undoable_markers import MISSING

    assert node._u_state.values["delayed"] is MISSING
    with pytest.raises(HistoryFaultError):
        h.begin()


def test_mapping_proxy_backing_callbacks_are_fenced_before_publication():
    from collections.abc import Mapping

    class ProviderMap(Mapping):
        def __iter__(self):
            h.begin()
            return iter(("value",))

        def __len__(self):
            return 1

        def __getitem__(self, key):
            return 1

    @undoable
    class Model:
        value: object = managed(default=MappingProxyType(ProviderMap()))

    h = UndoRedoManager()
    node = Model(transaction_manager=h)
    with pytest.raises(ReentrantOperationError):
        h.initialize(node)
    assert h._selection is None

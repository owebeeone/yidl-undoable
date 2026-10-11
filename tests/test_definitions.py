import pytest
from yidl_undoable import *
from yidl_lifecycle.lifecycle_markers import (
    owned,
    before_commit,
    commit_order_key,
    LifecycleDefinitionError,
)
from yidl_lifecycle.bindings import BindingBase


@pytest.mark.parametrize(
    "name",
    ["current", "working", "default", "node_id", "present", "_u_state", "_y_storage"],
)
def test_reserved(name):
    with pytest.raises(UndoableDefinitionError, match="reserved"):
        undoable(
            type(
                "Reserved",
                (),
                {"__annotations__": {name: int}, name: managed(default=0)},
            )
        )


@pytest.mark.parametrize("marker", [owned(default=None)])
def test_unsupported_field(marker):
    with pytest.raises(UndoableDefinitionError, match="unsupported"):
        undoable(
            type(
                "Unsupported",
                (),
                {"__annotations__": {"resource": object}, "resource": marker},
            )
        )


@pytest.mark.parametrize("decorator", [before_commit, commit_order_key])
def test_unsupported_hook(decorator):
    @decorator(DEFAULT_TRANSACTION)
    def hook(self):
        return ()

    with pytest.raises(UndoableDefinitionError, match="unsupported"):
        undoable(type("Unsupported", (), {"hook": hook}))


def test_local_store_has_no_named_providers():
    with pytest.raises(UndoableDefinitionError, match="zero-argument"):

        @undoable
        class Bad:
            seed: int = initvar(default=1)
            scratch: list = local_store(default_factory=lambda seed: [seed])


def test_binding_rejects_wrong_resource_types():
    @undoable
    class Bound:
        resource: object = binding(default=None)
        resources: dict[str, BindingBase] = binding(default_factory=dict)

    h = UndoRedoManager()
    with pytest.raises(TypeError, match="BindingBase"):
        Bound(resource="wrong", transaction_manager=h)
    assert not h._nodes
    x = Bound(transaction_manager=h)
    with pytest.raises(TypeError, match="BindingBase"):
        x.resource = object()
    with pytest.raises(TypeError, match="BindingBase"):
        x.resources = {"wrong": object()}


def test_required_and_constructor_only_visibility():
    @undoable
    class Input:
        required: int = managed()
        seed: int = initvar(default=1)

    h = UndoRedoManager()
    with pytest.raises(TypeError):
        Input(transaction_manager=h)
    x = Input(required=1, transaction_manager=h)
    with pytest.raises(AttributeError):
        _ = x.seed


def test_incompatible_inheritance_and_multiple_bases():
    @undoable
    class Base:
        value: int = managed(default=0)

    @undoable
    class Other:
        other: int = managed(default=0)

    with pytest.raises(UndoableDefinitionError, match="incompatible"):

        @undoable
        class Changed(Base):
            value: int = field(default=0)

    with pytest.raises(UndoableDefinitionError, match="multiple"):
        undoable(type("Multiple", (Base, Other), {}))


def test_custom_object_with_similar_internal_name_is_rejected_without_probe():
    class Impostor:
        @property
        def _u_state(self):
            raise AssertionError("must not introspect custom object")

    @undoable
    class Container:
        value: object = managed(default=None)

    h = UndoRedoManager()
    x = Container(value=Impostor(), transaction_manager=h)
    with pytest.raises(FrozenValueError):
        h.initialize(x)


def test_reused_marker_errors_are_public_definition_errors():
    with pytest.raises(UndoableDefinitionError):
        managed(default=1, default_factory=int)
    with pytest.raises(UndoableDefinitionError):
        local_store(init=True)


def test_decoration_target_and_generated_context():
    with pytest.raises(TypeError, match="classes"):
        undoable(1)
    with pytest.raises(UndoableDefinitionError, match="AST"):
        undoable(
            type(
                "bad-name",
                (),
                {"__annotations__": {"value": int}, "value": managed(default=0)},
            )
        )

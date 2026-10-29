"""Reuse canonical behavior; separately check the accessor specialization seam."""

import ast
import dis
import importlib
import runpy

import pytest
import yidl_undoable
from canonical_support import STORIES
from yidl_undoable.specialized import undoable


@pytest.mark.parametrize(
    "story",
    sorted(p for p in STORIES.glob("*.py") if p.stem != "11_layers"),
    ids=lambda p: p.stem,
)
def test_specialized_canonical_behavior(monkeypatch, story):
    monkeypatch.setattr(yidl_undoable, "undoable", undoable)
    monkeypatch.setattr(
        importlib.import_module("yidl_undoable.undoable"), "undoable", undoable
    )
    runpy.run_path(str(story), run_name="__specialized_canonical__")


def test_specialized_source_has_direct_accessors_and_selected_policies():
    from yidl_undoable import (
        field,
        managed,
        lazy,
        transient,
        binding,
        local_store,
        const,
    )
    from yidl_lifecycle.bindings import BindingBase

    @undoable
    class Selected:
        plain: int = field(default=1)
        constant: int = const(default=2)
        cache: dict = local_store(default_factory=dict)
        value: int = managed(default=3)
        frozen: tuple = managed(default=(), freeze=tuple, thaw=list)
        fixed_lazy: int = lazy(default=4)
        factory_lazy: int = lazy(default_factory=int)
        unset_lazy: int = lazy(mutable=True)
        scratch: list = transient(default_factory=list)
        factory_scratch: list = transient(
            default_factory=list, working_default_factory=list
        )
        resource: object = binding(default=None)
        resources: dict[str, BindingBase] = binding(default_factory=dict)

    tree = ast.parse(Selected.__undoable_source__)
    classes = [node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    assert len(classes) == 3
    forbidden = {
        "_u_baseline",
        "_u_read_plain",
        "_u_write_plain",
        "_u_read_const",
        "_u_write_const",
        "_u_read_binding",
        "_u_write_scalar_binding",
        "_u_write_map_binding",
        "_u_read_managed",
        "_u_write_managed",
        "_u_read_current_managed",
        "_u_read_working_managed",
        "_u_read_thaw_managed",
        "_u_write_current_managed",
        "_u_materialize_static",
        "_u_read_factory_static",
        "_u_read_default_static",
        "_u_read_unset_static",
        "_u_write_once_static",
        "_u_write_mutable_static",
        "_u_read_transient",
        "_u_read_factory_transient",
        "_u_read_baseline_transient",
        "_u_write_transient",
    }
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if isinstance(node.func.value, ast.Name) and node.func.value.id == "self":
                assert node.func.attr not in forbidden
    assert "allow_thaw=True" in Selected.__undoable_source__
    assert "state.values['plain']" in Selected.__undoable_source__
    for view in Selected.__undoable_views__.values():
        for descriptor in view.__dict__.values():
            if isinstance(descriptor, property):
                for function in (descriptor.fget, descriptor.fset):
                    if function is not None:
                        assert not any(
                            instruction.opname == "LOAD_GLOBAL"
                            and instruction.argval
                            in {"state", "value", "fact", "result"}
                            for instruction in dis.get_instructions(function)
                        )


@pytest.mark.parametrize("options", [{"eq": 1}, {"order": True}, {"order": "yes"}])
def test_specialized_rejects_invalid_options(options):
    from yidl_undoable import UndoableDefinitionError

    with pytest.raises(UndoableDefinitionError):
        undoable(**options)


@pytest.mark.parametrize(
    "name",
    (
        "require_mutation",
        "scalar_binding",
        "map_binding",
        "MISSING",
        "CandidateRead",
        "UndoableDefinitionError",
        "TransactionRequiredError",
        "_u_capture_0",
    ),
)
def test_public_class_names_do_not_shadow_accessor_captures(name):
    from yidl_lifecycle.bindings import BindingBase
    from yidl_undoable import (
        UndoRedoManager,
        TransactionRequiredError,
        UndoableDefinitionError,
        binding,
        field,
        lazy,
        managed,
        transient,
    )
    from yidl_undoable.bindings import scalar_binding, map_binding
    from yidl_undoable.callbacks import require_mutation
    from yidl_undoable.candidates import CandidateRead
    from yidl_undoable.specialized import AccessorCaptures
    from yidl_undoable.undoable_markers import MISSING

    model = undoable(
        type(
            name,
            (),
            {
                "__annotations__": {
                    "plain": int,
                    "value": int,
                    "memo": int,
                    "scratch": list,
                    "resource": object,
                    "resources": dict[str, BindingBase],
                },
                "plain": field(default=1),
                "value": managed(default=1),
                "memo": lazy(default_factory=int),
                "scratch": transient(default_factory=list),
                "resource": binding(default=None),
                "resources": binding(default_factory=dict),
            },
        )
    )
    captures = [
        value
        for value in model.__dict__["value"].fget.__globals__.values()
        if isinstance(value, AccessorCaptures)
    ]
    assert captures and all(value is captures[0] for value in captures)
    capsule = captures[0]
    assert capsule.mutation_guard is require_mutation
    assert capsule.scalar_binding is scalar_binding
    assert capsule.map_binding is map_binding
    assert capsule.missing is MISSING
    assert capsule.candidate_type is CandidateRead
    assert capsule.definition_error is UndoableDefinitionError
    assert capsule.transaction_error is TransactionRequiredError

    history = UndoRedoManager()
    node = model(transaction_manager=history)
    history.initialize(node)
    assert node.memo == 0
    with pytest.raises(AttributeError, match="already initialized"):
        node.memo = 1
    with history.begin():
        node.value = 2
        assert node.scratch == []
        node.resource = None
        node.resources = {}
        with pytest.raises(TransactionRequiredError, match="read-only"):
            node.current.value = 3
    with pytest.raises(TypeError, match="BindingBase"):
        node.resource = object()
    with pytest.raises(TypeError, match="BindingBase"):
        node.resources = {"invalid": object()}
    del node._u_state.values["plain"]
    with pytest.raises(UndoableDefinitionError, match="unresolved constructor field"):
        _ = node.plain

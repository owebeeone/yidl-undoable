"""Each inheritable concept compiles typed facts and builds executable models."""

from pathlib import Path
from types import ModuleType
import ast
import yidl_undoable
from yidl.concept_parser import compile_yidl_files
from yidl.generation.data_def_sys import emit_concept_runtime_source
from yidl_undoable import *
from yidl_undoable.facades import RuntimeFacade
from yidl_undoable.undoable_harvester import harvest_undoable_definition
from yidl_undoable.undoable import build_composable
from yidl_undoable.regenerate_undoable_base import generation_sources

resources = Path(yidl_undoable.__file__).parent / "yidl"
sources = generation_sources(resources)
features = [
    ("core", "UndoableCore", {"plain": field(default=1)}),
    (
        "const_static",
        "UndoableConstStatic",
        {"constant": const(default=2), "delayed": lazy(default=3)},
    ),
    ("managed", "UndoableManaged", {"value": managed(default=4)}),
    (
        "default_factories",
        "UndoableDefaultFactories",
        {"items": managed(default_factory=tuple)},
    ),
    (
        "transient",
        "UndoableTransient",
        {"scratch": transient(default_factory=list, working_default_factory=list)},
    ),
    ("binding", "UndoableBinding", {"resource": binding(default=None)}),
    ("local_store", "UndoableLocalStore", {"cache": local_store(default_factory=dict)}),
    ("views", "UndoableViews", {}),
    ("base", "UndoableBase", {}),
]
markers = {}
LAYER_SOURCES = []
for layer, concept_name, additions in features:
    markers.update(additions)
    declaration = type(
        "LayerNode",
        (),
        {"__annotations__": {name: object for name in markers}, **markers},
    )
    schema = harvest_undoable_definition(declaration)
    compiled = compile_yidl_files(sources, f"undoable/undoable_{layer}.yidl")
    concept = compiled.concepts[concept_name]
    runtime_source = emit_concept_runtime_source(
        concept.plan.build_data_definition(),
        resources=concept.resources,
        assembly_plan=concept,
    )
    module = ModuleType(f"layer_{layer}")
    exec(compile(runtime_source, f"<{layer}>", "exec"), module.__dict__)
    composable = build_composable(schema, generation_module=module)
    tree = composable.to_executable_ast()
    executable = {"__name__": "canonical_layers"}
    exec(compile(tree, f"<LayerNode.{layer}>", "exec"), executable)
    base = type("LayerBase", (RuntimeFacade, declaration), {"__slots__": ()})
    model = executable["build_undoable_class"](base, schema=schema)
    h = UndoRedoManager()
    x = model(transaction_manager=h)
    h.initialize(x)
    assert x.plain == 1
    if "constant" in markers:
        assert x.constant == 2 and x.delayed == 3
    if "value" in markers:
        assert x.value == 4
    if "cache" in markers:
        assert x.cache == {}
    if layer in ("views", "base"):
        with h.begin():
            x.value = 8
            assert x.current.value == 4 and x.working.value == 8
        assert h.undo() and x.value == 4
    LAYER_SOURCES.append((layer, ast.unparse(tree) + "\n"))

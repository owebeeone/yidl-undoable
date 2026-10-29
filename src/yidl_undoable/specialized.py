"""Opt-in experimental YIDL field-specific accessor implementation.

The normal decorator now uses a shipped builder for this same concept. This
explicit experimental adapter still compiles the authored extension once per
process for regeneration/probe coverage; both use the same class-build adapter. Comparison resources retain the existing pinned regeneration authority.
"""

from functools import lru_cache
from pathlib import Path
from types import ModuleType

from .errors import UndoableDefinitionError
from .accessor_captures import AccessorCaptures
from .undoable import _decorate


@lru_cache(maxsize=1)
def generation_module():
    from yidl.concept_parser import compile_yidl_files
    from yidl.generation.data_def_sys import emit_concept_runtime_source
    from .regenerate_undoable_base import generation_sources

    root = Path(__file__).parent / "yidl"
    sources = generation_sources(root)
    sources["undoable/experimental/specialized.yidl"] = (
        root / "experimental" / "specialized.yidl"
    ).read_text(encoding="utf-8")
    compiled = compile_yidl_files(sources, "undoable/experimental/specialized.yidl")
    concept = compiled.concepts["SpecializedUndoable"]
    source = emit_concept_runtime_source(
        concept.plan.build_data_definition(),
        resources=concept.resources,
        assembly_plan=concept,
    )
    module = ModuleType("yidl_undoable._experimental_specialized")
    exec(compile(source, "<undoable.specialized.builder>", "exec"), module.__dict__)
    module.build_UndoableModule = module.build_SpecializedModule
    return module


def undoable(cls=None, /, *, eq=False, order=False):
    """Experimental counterpart of :func:`yidl_undoable.undoable`."""
    for name, value in (("eq", eq), ("order", order)):
        if type(value) is not bool:
            raise UndoableDefinitionError(f"{name} must be an exact bool")
    if order and not eq:
        raise UndoableDefinitionError("order requires eq=True")

    def decorate(declaration):
        return _decorate(
            declaration,
            eq=eq,
            order=order,
            generation_module=generation_module(),
            capture_type=AccessorCaptures,
        )

    return decorate if cls is None else decorate(cls)

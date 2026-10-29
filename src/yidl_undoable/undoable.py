"""Typed YIDL facts -> generated container -> Astichi AST -> executable builder."""

import ast
import sys
from .undoable_harvester import harvest_undoable_definition
from .facades import RuntimeFacade
from .errors import UndoableDefinitionError
from .write_comparison_context import _historical_write_scope
from .comparison_captures import capture_ids
from .accessor_captures import AccessorCaptures
from .code_cache import compiled_builder, source_from_code, with_source
from yidl_cache import CompilationContext

RECORDS = {
    "field": "PlainField",
    "initvar": "InitVarField",
    "classvar": "ClassVarField",
    "const": "ConstField",
    "static": "StaticField",
    "managed": "ManagedField",
    "binding": "BindingField",
    "transient": "TransientField",
    "local_store": "LocalStoreField",
}


def build_composable(schema, *, generation_module=None):
    if generation_module is None:
        from . import _generated_specialized_base as generation_module
    generated = generation_module
    builder = generated.new_builder()
    aliases = capture_ids(schema.name)
    builder.add(
        generated.ClassesCollection,
        generated.UndoableClass(
            class_id=aliases[0],
            class_name=schema.name,
            current_class_name=schema.name + "_Current",
            working_class_name=schema.name + "_Working",
            restore_identity=schema.restore_identity,
            restore_order=schema.restore_order,
        ),
    )
    for fact in schema.fields:
        record = getattr(generated, RECORDS[fact["field_kind"]])
        kwargs = {name: fact[name] for name in record.__slots__ if name in fact}
        kwargs["is_lazy"] = fact["field_kind"] == "static"
        builder.add(generated.FieldsCollection, record(**kwargs))
        for view in ("current", "working"):
            builder.add(
                generated.AccessViewsCollection,
                generated.FieldView(
                    field_id=fact["field_id"],
                    field_name=fact["field_name"],
                    field_order=fact["field_order"],
                    field_kind=fact["field_kind"],
                    has_thaw=fact["has_thaw"],
                    view=view,
                ),
            )
    if not hasattr(generated, "ComparisonClassesCollection"):
        if schema.eq or schema.order:
            raise UndoableDefinitionError(
                "selected consumer layer has no comparison surface"
            )
        return generated.build_UndoableModule(generated.build_container(builder))
    logical = [fact for fact in schema.fields if fact["logical_compare"]]
    for view_order, view in enumerate(("default", "current", "working")):
        owner = aliases[view_order + 1]
        builder.add(
            generated.ComparisonClassesCollection,
            generated.ComparisonClass(
                cmp_class_id=owner,
                cmp_class_order=view_order,
                cmp_eq=schema.eq,
                cmp_order=schema.order,
                cmp_hash_none=schema.eq,
                use_tuple_equality=sys.version_info[:2] == (3, 12),
                has_compare_operands=bool(logical),
            ),
        )
        for index, fact in enumerate(logical):
            builder.add(
                generated.ComparisonOperandsCollection,
                generated.ComparisonOperand(
                    cmp_operand_id=owner + "." + fact["field_name"],
                    cmp_owner=owner,
                    cmp_operand_order=view_order * len(logical) + index,
                    cmp_read_path=fact["field_name"],
                    cmp_hash_included=False,
                    cmp_last=index == len(logical) - 1,
                ),
            )
    return generated.build_UndoableModule(generated.build_container(builder))


def _decorate(
    cls, *, eq, order, generation_module=None, capture_type=AccessorCaptures
):
    if not isinstance(cls, type):
        raise TypeError("@undoable can only decorate classes")
    if eq:
        for base in cls.__mro__:
            if (
                base in (object, RuntimeFacade)
                or "__undoable_schema__" in base.__dict__
            ):
                continue
            for name in (
                "__eq__",
                "__hash__",
                *(("__lt__", "__le__", "__gt__", "__ge__") if order else ()),
            ):
                if name in base.__dict__:
                    raise UndoableDefinitionError(
                        f"{cls.__qualname__}: conflicting {name}"
                    )
    schema = harvest_undoable_definition(cls, eq=eq, order=order)
    try:
        compilation = CompilationContext(filename=f"<undoable.{cls.__qualname__}>")

        def produce():
            composable = build_composable(schema, generation_module=generation_module)
            module = composable.to_executable_ast()
            source = ast.unparse(module) + "\n"
            code = compile(
                module, compilation.filename, "exec", flags=compilation.flags,
                dont_inherit=compilation.dont_inherit, optimize=compilation.optimize,
            )
            return with_source(code, source)

        code = (
            compiled_builder(schema, cls, compilation, produce)
            if generation_module is None else produce()
        )
        source = source_from_code(code)
        namespace = {
            "__name__": cls.__module__,
            **dict.fromkeys(
                capture_ids(schema.name),
                capture_type(
                    _historical_write_scope,
                    RuntimeFacade.__eq__,
                    RuntimeFacade.__hash__,
                    object.__lt__,
                    object.__le__,
                    object.__gt__,
                    object.__ge__,
                ),
            ),
        }
        exec(code, namespace)
    except Exception as exc:
        raise UndoableDefinitionError(
            f"{cls.__qualname__}: Undoable AST generation/execution failed: {exc}"
        ) from exc
    base = (
        cls
        if issubclass(cls, RuntimeFacade)
        else type(f"{cls.__name__}_UserBase", (RuntimeFacade, cls), {"__slots__": ()})
    )
    result = namespace["build_undoable_class"](base, schema=schema)
    result.__module__, result.__qualname__ = cls.__module__, cls.__qualname__
    result.__undoable_source__ = source
    return result


def undoable(cls=None, /, *, eq=False, order=False):
    for name, value in (("eq", eq), ("order", order)):
        if type(value) is not bool:
            raise UndoableDefinitionError(f"{name} must be an exact bool")
    if order and not eq:
        raise UndoableDefinitionError("order requires eq=True")

    def decorate(declaration):
        return _decorate(declaration, eq=eq, order=order)

    return decorate if cls is None else decorate(cls)

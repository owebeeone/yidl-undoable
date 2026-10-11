"""Typed YIDL facts -> generated container -> Astichi AST -> executable builder."""

import ast
from .undoable_harvester import harvest_undoable_definition
from .facades import RuntimeFacade
from .errors import UndoableDefinitionError
from . import _generated_undoable_base as generated

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


def build_composable(schema, *, generation_module=generated):
    generated = generation_module
    builder = generated.new_builder()
    builder.add(
        generated.ClassesCollection,
        generated.UndoableClass(
            class_id=schema.name,
            class_name=schema.name,
            current_class_name=schema.name + "_Current",
            working_class_name=schema.name + "_Working",
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
    return generated.build_UndoableModule(generated.build_container(builder))


def undoable(cls):
    if not isinstance(cls, type):
        raise TypeError("@undoable can only decorate classes")
    schema = harvest_undoable_definition(cls)
    try:
        composable = build_composable(schema)
        module = composable.to_executable_ast()
        source = ast.unparse(module) + "\n"
        namespace = {"__name__": cls.__module__}
        exec(compile(module, f"<undoable.{cls.__qualname__}>", "exec"), namespace)
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

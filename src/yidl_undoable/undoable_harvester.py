"""Translate Lifecycle normalized declarations, preserving our own inheritance."""

from dataclasses import dataclass
from inspect import get_annotations
from types import MappingProxyType
from yidl_lifecycle.lifecycle_harvester import harvest_lifecycle_definition
from yidl_lifecycle.lifecycle_markers import (
    LifecycleDefinitionError,
    LifecycleMarker,
    field,
    transaction_method_markers,
)
from .errors import UndoableDefinitionError
from .undoable_markers import UndoableMarker

RESERVED = {
    "default",
    "current",
    "working",
    "present",
    "node_id",
    "transaction_manager",
    "__undoable_schema__",
    "__undoable_source__",
}
SUPPORTED = {
    "managed",
    "const",
    "field",
    "binding",
    "local_store",
    "static",
    "transient",
    "initvar",
    "classvar",
}


@dataclass(frozen=True, slots=True)
class Schema:
    name: str
    fields: tuple
    validators: tuple
    markers: object
    annotations: object
    logical: object
    eq: bool = False
    order: bool = False
    restore_identity: bool = False
    restore_order: bool = False

    @property
    def by_name(self):
        return MappingProxyType({f["field_name"]: f for f in self.fields})


def harvest_undoable_definition(cls, *, eq=False, order=False):
    bases = [b for b in cls.__bases__ if hasattr(b, "__undoable_schema__")]
    if len(bases) > 1:
        raise UndoableDefinitionError(
            f"{cls.__name__}: multiple generated bases unsupported"
        )
    markers, annotations, logical = {}, {}, {}
    inherited = bases[0].__undoable_schema__ if bases else None
    if inherited:
        markers.update(inherited.markers)
        annotations.update(inherited.annotations)
        logical.update(inherited.logical)
    local = get_annotations(cls, eval_str=False)
    for name, annotation in local.items():
        if name in RESERVED or name.startswith(("_u_", "_y_", "__undoable_")):
            raise UndoableDefinitionError(f"{cls.__name__}.{name}: reserved field name")
        raw = cls.__dict__.get(name, field())
        if isinstance(raw, UndoableMarker):
            marker, included = raw.marker, raw.logical_compare
        else:
            marker = raw if isinstance(raw, LifecycleMarker) else field(default=raw)
            included = marker.kind not in {
                "initvar",
                "classvar",
                "transient",
                "local_store",
            }
        logical[name] = included
        if marker.kind not in SUPPORTED:
            raise UndoableDefinitionError(
                f"{cls.__name__}.{name}: unsupported {marker.kind}"
            )
        if name in markers:
            old = markers[name]
            if old.kind != marker.kind or old.tx_key != marker.tx_key:
                raise UndoableDefinitionError(
                    f"{cls.__name__}.{name}: incompatible kind/key override"
                )
        markers[name], annotations[name] = marker, annotation
    body = dict(markers)
    body["__annotations__"] = annotations
    body["__module__"] = cls.__module__
    validators = {} if not inherited else dict(inherited.validators)
    for name, value in cls.__dict__.items():
        if name in RESERVED or name.startswith(("_u_", "__undoable_")):
            if name not in {"__undoable_schema__", "__undoable_source__"}:
                raise UndoableDefinitionError(f"{cls.__name__}.{name}: reserved name")
        for marker in transaction_method_markers(value):
            if marker.kind != "validate_commit":
                raise UndoableDefinitionError(
                    f"{cls.__name__}.{name}: unsupported hook {marker.kind}"
                )
            validators[name] = marker.tx_key
            body[name] = value
    # A synthetic declaration class intentionally has NO Undoable generated bases.
    declaration = type(cls.__name__, (), body)
    declaration.__qualname__ = cls.__qualname__
    try:
        harvested = harvest_lifecycle_definition(declaration)
    except LifecycleDefinitionError as exc:
        raise UndoableDefinitionError(str(exc)) from exc
    facts = [
        dict(f, logical_compare=logical[f["field_name"]]) for f in harvested.field_facts
    ]
    if inherited:
        old = inherited.by_name
        for fact in facts:
            if fact["field_name"] in old:
                fact["field_id"] = old[fact["field_name"]]["field_id"]
    names = {f["field_name"] for f in facts}
    for fact in facts:
        if fact["field_kind"] == "local_store" and fact["default_factory_param_names"]:
            raise UndoableDefinitionError(
                f"{cls.__name__}.{fact['field_name']}: local_store requires a zero-argument factory"
            )
        for role in (
            "default_factory_param_names",
            "working_default_factory_param_names",
        ):
            for provider in fact[role]:
                if provider == "self" and not fact["allow_self_factory"]:
                    raise UndoableDefinitionError(
                        f"{cls.__name__}.{fact['field_name']}: self factory requires allow_self_factory"
                    )
                if provider not in names | {"self", "cls"}:
                    raise UndoableDefinitionError(
                        f"{cls.__name__}.{fact['field_name']}: unknown provider {provider}"
                    )
    return Schema(
        cls.__name__,
        tuple(MappingProxyType(f) for f in facts),
        tuple(validators.items()),
        MappingProxyType(markers),
        MappingProxyType(annotations),
        MappingProxyType(logical),
        eq,
        order,
        bool(inherited and inherited.eq and not eq),
        bool(inherited and inherited.order and not order),
    )

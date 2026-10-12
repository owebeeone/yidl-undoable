"""Undoable field-local comparison controls over unchanged Lifecycle markers."""

from dataclasses import dataclass
from yidl_lifecycle import lifecycle_markers as lifecycle
from yidl_lifecycle.transaction_yidl import DEFAULT_TRANSACTION

MISSING = lifecycle.MISSING
_HAS_DEFAULT_FACTORY = lifecycle._HAS_DEFAULT_FACTORY
LifecycleMarker = lifecycle.LifecycleMarker
validate_commit = lifecycle.validate_commit


@dataclass(frozen=True, slots=True)
class UndoableMarker:
    marker: LifecycleMarker
    logical_compare: bool
    write_compare_explicit: bool = False


def _declaration(factory, *args, compare=MISSING, write_compare=MISSING, **options):
    managed_kind = factory is lifecycle.managed
    excluded = factory in (
        lifecycle.initvar,
        lifecycle.classvar,
        lifecycle.transient,
        lifecycle.local_store,
    )
    explicit_write = write_compare is not MISSING
    legacy = managed_kind and type(compare) is str and compare in ("value", "identity")
    if explicit_write and not managed_kind:
        raise lifecycle.LifecycleDefinitionError(
            "write_compare is only supported for managed fields"
        )
    if legacy and explicit_write:
        raise lifecycle.LifecycleDefinitionError(
            "legacy compare conflicts with explicit write_compare"
        )
    if compare is MISSING:
        logical = not excluded
    elif legacy:
        logical = True
    elif type(compare) is not bool:
        raise lifecycle.LifecycleDefinitionError("compare must be an exact bool")
    else:
        logical = compare
    if excluded and logical:
        raise lifecycle.LifecycleDefinitionError(
            "compare=True is excluded for this field family"
        )
    if managed_kind:
        policy = (
            compare
            if legacy
            else "value" if write_compare is MISSING else write_compare
        )
        if type(policy) is not str or policy not in ("value", "identity"):
            raise lifecycle.LifecycleDefinitionError(
                "write_compare must be value or identity"
            )
        options["compare"] = policy
    return UndoableMarker(factory(*args, **options), logical, explicit_write)


def field(**options):
    return _declaration(lifecycle.field, **options)


def const(**options):
    return _declaration(lifecycle.const, **options)


def lazy(**options):
    return _declaration(lifecycle.lazy, **options)


static = lazy


def binding(**options):
    return _declaration(lifecycle.binding, **options)


def initvar(**options):
    return _declaration(lifecycle.initvar, **options)


def classvar(**options):
    return _declaration(lifecycle.classvar, **options)


def transient(tx_key=DEFAULT_TRANSACTION, **options):
    return _declaration(lifecycle.transient, tx_key, **options)


def local_store(**options):
    return _declaration(lifecycle.local_store, **options)


def managed(tx_key=DEFAULT_TRANSACTION, **options):
    return _declaration(lifecycle.managed, tx_key, **options)


__all__ = [
    "MISSING",
    "binding",
    "classvar",
    "const",
    "field",
    "initvar",
    "lazy",
    "local_store",
    "managed",
    "static",
    "transient",
    "validate_commit",
]

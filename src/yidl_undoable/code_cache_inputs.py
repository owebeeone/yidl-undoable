"""Audited model-builder identity, excluding runtime values and annotations.

Generated constructor annotations read the freshly bound schema. Keys, defaults,
factories, conversions and validator methods are also used through that schema
or the fresh user base, never embedded as code literals. Derived code-selection
facts (including optionality and binding shape) remain in the identity.
"""

import hashlib
import json
import os

from yidl_cache import CacheIdentityError

_RUNTIME = {
    "default_value", "default_factory", "working_default_factory", "freeze",
    "thaw", "annotation", "tx_key_key",
}
_STRUCTURAL = {
    "field_id", "field_owner", "field_name", "field_order", "field_kind",
    "binding_shape", "compare", "mutable", "init", "has_default",
    "default_value_param_name", "has_default_factory", "allow_self_factory",
    "default_factory_param_names", "default_factory_param_name",
    "has_working_default_factory", "working_default_factory_param_names",
    "working_default_factory_param_name", "value_slot_name", "current_slot_name",
    "working_slot_name", "staged_slot_name", "has_freeze", "freeze_param_name",
    "has_thaw", "thaw_param_name", "has_optional_none", "logical_compare",
}


def _literal(value, depth=0):
    if depth > 16:
        raise CacheIdentityError("Undoable cache input nesting exceeds limit")
    if value is None or type(value) is bool:
        return value
    if type(value) is int and value.bit_length() <= 64:
        return value
    if type(value) is str and len(value) <= 65536:
        return value
    if type(value) is tuple and len(value) <= 20000:
        return [_literal(item, depth + 1) for item in value]
    raise CacheIdentityError("unsupported Undoable generation input")


def generation_digest(schema):
    if len(schema.fields) > 20000:
        raise CacheIdentityError("Undoable field count exceeds cache limit")
    fields = []
    for fact in schema.fields:
        if fact.keys() != _STRUCTURAL | _RUNTIME:
            raise CacheIdentityError("unknown Undoable field schema")
        fields.append([[name, _literal(fact[name])] for name in sorted(_STRUCTURAL)])
    payload = {
        "name": _literal(schema.name), "fields": fields,
        "eq": _literal(schema.eq), "order": _literal(schema.order),
        "restore_identity": _literal(schema.restore_identity),
        "restore_order": _literal(schema.restore_order),
        "engine_environment": sorted(
            (name, value) for name, value in os.environ.items()
            if name.startswith("ASTICHI_")
        ),
    }
    encoded = json.dumps(payload, sort_keys=True, ensure_ascii=True).encode("ascii")
    if len(encoded) > 1024 * 1024:
        raise CacheIdentityError("Undoable generation inputs exceed cache limit")
    return hashlib.sha256(encoded).hexdigest()

"""Nonversioned binding type parity, without resource acceptance/ownership hooks."""

from collections.abc import Mapping
from yidl_lifecycle.bindings import BindingBase, BindingDict


def scalar_binding(name, value):
    if value is not None and not isinstance(value, BindingBase):
        raise TypeError(f"{name}: binding expects BindingBase or None")
    return value


def map_binding(name, value):
    if value is None:
        return None
    if not isinstance(value, Mapping):
        raise TypeError(f"{name}: binding expects a mapping or None")
    result = value if isinstance(value, BindingDict) else BindingDict(value)
    for key, item in result.items():
        if not isinstance(item, BindingBase):
            raise TypeError(
                f"{name}: binding expects BindingBase values at key {key!r}"
            )
    return result

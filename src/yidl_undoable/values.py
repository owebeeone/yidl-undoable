"""Stable values and internal node edges, independent of facades and epochs."""

from dataclasses import dataclass
from collections.abc import Mapping
from types import MappingProxyType
from .errors import FrozenValueError, ForeignManagerError


@dataclass(frozen=True, slots=True)
class NodeRef:
    node_id: int


def normalize(value, manager, path="value", ancestors=None):
    ancestors = set() if ancestors is None else ancestors
    from .facades import RuntimeFacade

    if isinstance(value, RuntimeFacade):
        state = value._u_state
        if state.manager is not manager:
            raise ForeignManagerError(
                f"{path}: managed edge belongs to another manager"
            )
        manager._available(state)
        return NodeRef(state.node_id)
    if isinstance(value, NodeRef):
        manager._available(manager._nodes[value.node_id])
        return value
    if type(value) in (type(None), bool, int, float, complex, str, bytes):
        return value
    if type(value) not in (tuple, frozenset, MappingProxyType):
        raise FrozenValueError(
            f"{path}: unsupported stable value {type(value).__name__}; declare freeze"
        )
    if id(value) in ancestors:
        raise FrozenValueError(f"{path}: container cycle")
    ancestors.add(id(value))
    try:
        if isinstance(value, Mapping):
            result = {}
            for key, item in value.items():
                normalized_key = normalize(key, manager, path + ".key", ancestors)
                if any(refs(normalized_key)):
                    raise FrozenValueError(f"{path}: mapping keys cannot contain nodes")
                result[normalized_key] = normalize(item, manager, path, ancestors)
            return MappingProxyType(result)
        items = (normalize(item, manager, path, ancestors) for item in value)
        return tuple(items) if type(value) is tuple else frozenset(items)
    finally:
        ancestors.remove(id(value))


def refs(value):
    from .facades import RuntimeFacade

    if isinstance(value, NodeRef):
        yield value.node_id
    elif isinstance(value, Mapping):
        for item in value.values():
            yield from refs(item)
    elif isinstance(value, (tuple, frozenset, list, set)):
        for item in value:
            yield from refs(item)
    elif isinstance(value, RuntimeFacade):
        yield value._u_state.node_id


def decode(value, resolve):
    if isinstance(value, NodeRef):
        return resolve(value.node_id)
    if isinstance(value, Mapping):
        return MappingProxyType(
            {key: decode(item, resolve) for key, item in value.items()}
        )
    if type(value) is tuple:
        return tuple(decode(item, resolve) for item in value)
    if type(value) is frozenset:
        return frozenset(decode(item, resolve) for item in value)
    return value


def project_working(value, manager, view, *, in_place=False, ancestors=None):
    """Project live child handles while preserving the owned working container."""
    from .facades import RuntimeFacade

    ancestors = set() if ancestors is None else ancestors
    if isinstance(value, RuntimeFacade):
        manager._available(value._u_state)
        return value._u_state.facade(view)
    if isinstance(value, NodeRef):
        return manager._nodes[value.node_id].facade(view)
    if type(value) not in (tuple, list, dict, set, frozenset, MappingProxyType):
        return value
    if id(value) in ancestors:
        raise FrozenValueError("working container cycle")
    ancestors.add(id(value))
    try:
        if type(value) in (dict, MappingProxyType):
            items = {
                key: project_working(
                    item, manager, view, in_place=in_place, ancestors=ancestors
                )
                for key, item in value.items()
            }
            unchanged = all(items[key] is item for key, item in value.items())
            if unchanged:
                return value
            if in_place and type(value) is dict:
                value.update(items)
                return value
            return items if type(value) is dict else MappingProxyType(items)
        items = [
            project_working(item, manager, view, in_place=in_place, ancestors=ancestors)
            for item in value
        ]
        if all(a is b for a, b in zip(items, value)):
            return value
        if in_place and type(value) is list:
            value[:] = items
            return value
        if in_place and type(value) is set:
            value.clear()
            value.update(items)
            return value
        if type(value) is tuple:
            return tuple(items)
        if type(value) is frozenset:
            return frozenset(items)
        if type(value) is set:
            return set(items)
        return items
    finally:
        ancestors.remove(id(value))

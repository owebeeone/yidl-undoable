"""Reachability is recomputed from escaped working containers on every query."""

from collections.abc import Mapping
from .values import NodeRef
from .errors import GraphCycleError, FrozenValueError


def edges(value, manager, ancestors=None):
    ancestors = set() if ancestors is None else ancestors
    from .facades import RuntimeFacade

    if isinstance(value, RuntimeFacade):
        manager._available(value._u_state)
        yield value.node_id
    elif isinstance(value, NodeRef):
        manager._available(manager._nodes[value.node_id])
        yield value.node_id
    elif isinstance(value, (tuple, frozenset, list, dict, set, Mapping)):
        if id(value) in ancestors:
            raise FrozenValueError("working container cycle")
        ancestors.add(id(value))
        try:
            items = value.values() if isinstance(value, Mapping) else value
            for item in items:
                yield from edges(item, manager, ancestors)
        finally:
            ancestors.remove(id(value))


def traverse(roots, values_for, manager, *, reject_cycles):
    present, visiting = set(), set()

    def visit(node_id):
        if node_id in visiting:
            if reject_cycles:
                raise GraphCycleError(f"managed graph cycle at node {node_id}")
            return
        if node_id in present:
            return
        manager._available(manager._nodes[node_id])
        visiting.add(node_id)
        for value in values_for(node_id).values():
            for child in edges(value, manager):
                visit(child)
        visiting.remove(node_id)
        present.add(node_id)

    for node_id in roots:
        visit(node_id)
    return frozenset(present)

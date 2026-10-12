"""Historical write identity despite enabled structural child comparisons."""

import pytest
from yidl_undoable import *


@undoable(eq=True, order=True)
class Child:
    value: int = managed(default=2)


@undoable
class Parent:
    children: tuple = managed(default=())


h = UndoRedoManager()
first = Child(transaction_manager=h)
second = Child(transaction_manager=h)
root = Parent(children=(first,), transaction_manager=h)
h.initialize(root, first, second)
assert first == second
with h.begin():
    root.children = (second,)
    assert (root.node_id, "children") in h._edit.touched
    assert root.children[0].node_id == second.node_id
assert root.children[0].node_id == second.node_id and first == second
assert h.undo() and root.children[0].node_id == first.node_id
assert h.redo() and root.children[0].node_id == second.node_id

MODELS = []
for enabled in (False, True):
    for logical in (False, True):
        for spelling in (
            "legacy_value",
            "legacy_identity",
            "new_value",
            "new_identity",
        ):
            policy = "identity" if "identity" in spelling else "value"
            declaration = (
                managed(default=(), compare=policy)
                if spelling.startswith("legacy")
                else managed(default=(), compare=logical, write_compare=policy)
            )
            model = undoable(
                type(
                    f"Parent_{enabled}_{logical}_{spelling}",
                    (),
                    {"__annotations__": {"children": tuple}, "children": declaration},
                ),
                eq=enabled,
            )
            MODELS.append(model)
            manager = UndoRedoManager()
            left = Child(transaction_manager=manager)
            right = Child(transaction_manager=manager)
            parent = model(children=(left,), transaction_manager=manager)
            manager.initialize(parent, right)
            with manager.begin():
                parent.children = (right,)
                assert (parent.node_id, "children") in manager._edit.touched
            assert parent.children[0].node_id == right.node_id
            fact = model.__undoable_schema__.by_name["children"]
            assert fact["compare"] == policy and fact["logical_compare"] is (
                True if spelling.startswith("legacy") else logical
            )
LAYER_SOURCES = [(model.__name__, model.__undoable_source__) for model in MODELS]

"""Supported names retain public creation hooks, all views and historical writes."""

import builtins
from contextvars import copy_context
from yidl_undoable import undoable, managed, UndoRedoManager
from yidl_undoable.facades import RuntimeFacade
from yidl_undoable.write_comparison_context import _historical_write_scope

NAMES = (
    "_u_historical_write_scope",
    "_u_historical_eq",
    "_u_historical_hash",
    "_u_object_lt",
    "_u_object_le",
    "_u_object_gt",
    "_u_object_ge",
    "_u_capture_0",
    "_u_capture_0_default",
    "_u_capture_0_current",
    "_u_capture_0_working",
)
LAYER_SOURCES = []
for name in NAMES:
    events = []

    class Meta(builtins.type):
        def __new__(mcls, name, bases, namespace):
            events.append(("meta", name))
            return super().__new__(mcls, name, bases, namespace)

    class Hooks(metaclass=Meta):
        def __init_subclass__(cls):
            events.append(("hook", cls.__name__))

    declaration = builtins.type(
        name,
        (Hooks,),
        {
            "__module__": __name__,
            "__annotations__": {"value": int, "ignored": int},
            "value": managed(default=2),
            "ignored": managed(default=9, compare=False),
        },
    )
    events.clear()
    model = undoable(declaration, eq=True, order=True)
    creation = [name + "_UserBase", name, name + "_Current", name + "_Working"]
    assert [value for kind, value in events if kind == "meta"] == creation
    assert [value for kind, value in events if kind == "hook"] == creation

    @undoable
    class Parent:
        children: tuple = managed(default=())

    manager = UndoRedoManager()
    a, b = model(transaction_manager=manager), model(transaction_manager=manager)
    parent = Parent(children=(a,), transaction_manager=manager)
    manager.initialize(parent, a, b)
    assert a == b and not (a < a) and a <= b
    assert a.current == b.current and a.working == b.working
    assert not (a == a.current)
    context = copy_context()
    manager.begin()
    try:
        parent.children = (b,)
        assert parent.children[0].node_id == b.node_id
        assert context.run(lambda: a == b)
        assert _historical_write_scope.get() is None
    finally:
        manager.rollback()
    child = undoable(
        builtins.type(name, (model,), {"__module__": __name__, "__annotations__": {}})
    )
    identity_manager = UndoRedoManager()
    first, second = child(transaction_manager=identity_manager), child(
        transaction_manager=identity_manager
    )
    identity_manager.initialize(first, second)
    assert (
        first != second
        and first == first.current
        and hash(first) == hash(first.current)
    )
    assert first.__lt__(second) is NotImplemented
    LAYER_SOURCES.extend(
        [
            (name, model.__undoable_source__),
            (name + "_Disabled", child.__undoable_source__),
        ]
    )

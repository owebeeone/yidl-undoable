"""Test-first closure capture name failures; canonical protocols live in story24."""

import builtins
import pytest
from yidl_undoable import undoable, managed


@pytest.mark.parametrize("name", ("_u_historical_write_scope", "_u_historical_eq"))
def test_original_names_do_not_become_prelude_closure_dependencies(name):
    from yidl_undoable.comparison_captures import ComparisonCaptures
    from yidl_undoable.facades import RuntimeFacade
    from yidl_undoable.write_comparison_context import _historical_write_scope

    model = undoable(
        builtins.type(
            name, (), {"__annotations__": {"value": int}, "value": managed(default=2)}
        ),
        eq=True,
    )
    for view in model.__undoable_views__.values():
        method = view.__dict__["__eq__"]
        assert name not in method.__code__.co_freevars
        capsules = [
            value
            for value in method.__globals__.values()
            if isinstance(value, ComparisonCaptures)
        ]
        assert capsules and all(value is capsules[0] for value in capsules)
        capsule = capsules[0]
        assert capsule.scope is _historical_write_scope
        assert (
            capsule.equal is RuntimeFacade.__eq__
            and capsule.hash_function is RuntimeFacade.__hash__
        )
        assert (
            capsule.less,
            capsule.less_equal,
            capsule.greater,
            capsule.greater_equal,
        ) == (object.__lt__, object.__le__, object.__gt__, object.__ge__)


@pytest.mark.parametrize(
    "name",
    (
        "_u_historical_hash",
        "_u_object_lt",
        "_u_object_le",
        "_u_object_gt",
        "_u_object_ge",
    ),
)
def test_capture_names_do_not_break_disabled_inheritance_resets(name):
    @undoable(eq=True, order=True)
    class Base:
        value: int = managed(default=2)

    model = undoable(builtins.type(name, (Base,), {"__annotations__": {}}))
    from yidl_undoable.facades import RuntimeFacade

    assert model.__eq__ is RuntimeFacade.__eq__
    assert model.__hash__ is RuntimeFacade.__hash__
    assert all(
        getattr(model, key) is getattr(object, key)
        for key in ("__lt__", "__le__", "__gt__", "__ge__")
    )

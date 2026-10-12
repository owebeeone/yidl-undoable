"""Test-first Undoable option, declaration and logical/write policy boundaries."""

import pytest
from yidl_undoable import (
    undoable,
    managed,
    field,
    const,
    lazy,
    binding,
    initvar,
    classvar,
    transient,
    local_store,
    UndoableDefinitionError,
)
from yidl_lifecycle import lifecycle_markers as lifecycle


@pytest.mark.parametrize("option", ("eq", "order"))
@pytest.mark.parametrize("value", (0, 1, None, "true", object()))
def test_options_are_exact_booleans(option, value):
    with pytest.raises(UndoableDefinitionError, match=option + ".*bool"):
        undoable(type("Bad", (), {}), **{option: value})


@pytest.mark.parametrize("options", ({"order": True}, {"eq": False, "order": True}))
def test_order_requires_explicit_enabled_equality(options):
    with pytest.raises(UndoableDefinitionError, match="order.*eq"):
        undoable(type("Bad", (), {}), **options)


@pytest.mark.parametrize("factory", (field, const, lazy, binding, managed))
@pytest.mark.parametrize("invalid", (0, 1, None, "other"))
def test_eligible_logical_compare_is_exact_bool(factory, invalid):
    with pytest.raises(UndoableDefinitionError, match="compare.*bool"):
        factory(compare=invalid)


@pytest.mark.parametrize("factory", (initvar, classvar, transient, local_store))
def test_excluded_family_rejects_explicit_logical_true(factory):
    with pytest.raises(UndoableDefinitionError, match="compare.*excluded"):
        factory(compare=True)
    factory(compare=False)


@pytest.mark.parametrize(
    "factory", (field, const, lazy, binding, initvar, classvar, transient, local_store)
)
def test_write_policy_only_belongs_to_managed(factory):
    with pytest.raises(UndoableDefinitionError, match="write_compare.*managed"):
        factory(write_compare="value")


@pytest.mark.parametrize("policy", (None, True, 0, "other"))
def test_invalid_managed_write_policy(policy):
    with pytest.raises(UndoableDefinitionError, match="write_compare"):
        managed(write_compare=policy)


@pytest.mark.parametrize("legacy", ("value", "identity"))
@pytest.mark.parametrize("explicit", ("value", "identity"))
def test_legacy_plus_explicit_write_policy_conflicts(legacy, explicit):
    with pytest.raises(UndoableDefinitionError, match="legacy.*write_compare"):
        managed(compare=legacy, write_compare=explicit)


@pytest.mark.parametrize(
    "name", ("__eq__", "__lt__", "__le__", "__gt__", "__ge__", "__hash__")
)
def test_enabled_comparisons_reject_conflicting_custom_methods(name):
    declaration = type("Custom", (), {name: lambda self, other=None: True})
    with pytest.raises(UndoableDefinitionError, match=name):
        undoable(declaration, eq=True, order=True)


def test_direct_lifecycle_markers_stay_valid_with_original_write_policy():
    class Declaration:
        value: int = lifecycle.managed(compare="identity", default=2)
        cache: list = lifecycle.local_store(default_factory=list)

    Model = undoable(Declaration, eq=True)
    facts = Model.__undoable_schema__.by_name
    assert (
        facts["value"]["compare"] == "identity"
        and facts["value"]["logical_compare"] is True
    )
    assert facts["cache"]["logical_compare"] is False
    assert lifecycle.managed(compare="identity").compare == "identity"


def test_disabled_child_restores_identity_instead_of_inheriting_structural_methods():
    from yidl_undoable import UndoRedoManager

    @undoable(eq=True, order=True)
    class Base:
        value: int = managed(default=2)

    @undoable
    class Disabled(Base):
        pass

    h = UndoRedoManager()
    a = Disabled(transaction_manager=h)
    b = Disabled(transaction_manager=h)
    h.initialize(a, b)
    assert a != b and a == a.current and hash(a) == hash(a.current)
    with pytest.raises(TypeError):
        a < b


def test_order_disabled_child_does_not_inherit_generated_ordering():
    from yidl_undoable import UndoRedoManager

    @undoable(eq=True, order=True)
    class Base:
        value: int = managed(default=2)

    @undoable(eq=True)
    class Child(Base):
        pass

    h = UndoRedoManager()
    a = Child(transaction_manager=h)
    b = Child(value=3, transaction_manager=h)
    h.initialize(a, b)
    assert a != b
    with pytest.raises(TypeError):
        a < b

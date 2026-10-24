"""Constructor metadata preserves runtime objects without evaluating strings.

Keep this module free of future annotations so live types reach generation.
"""

from inspect import Parameter, signature

import pytest

from yidl_undoable import (
    binding,
    classvar,
    const,
    field,
    initvar,
    lazy,
    local_store,
    managed,
    transient,
    undoable,
)
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY


class Payload:
    pass


@pytest.mark.parametrize(
    "marker", [field, const, managed, transient, binding, initvar, lazy]
)
@pytest.mark.parametrize("mode", ["required", "default", "factory"])
def test_effective_field_annotations_keep_live_type_identity(marker, mode):
    token = Payload()
    options = {
        "required": {},
        "default": {"default": token},
        "factory": {"default_factory": Payload},
    }[mode]

    @undoable
    class Model:
        anchor: int = managed(default=2)
        value: Payload = marker(**options)

    assert Model.__init__.__annotations__ == {"anchor": int, "value": Payload}
    params = signature(Model).parameters
    assert tuple(params) == ("transaction_manager", "anchor", "value")
    assert params["anchor"].annotation is int
    assert params["value"].annotation is Payload
    assert all(p.kind is Parameter.KEYWORD_ONLY for p in params.values())
    expected_default = (
        Parameter.empty
        if mode == "required" and marker is not lazy
        else _HAS_DEFAULT_FACTORY
    )
    assert params["value"].default is expected_default
    assert params["transaction_manager"].annotation is Parameter.empty
    assert params["transaction_manager"].default is Parameter.empty
    assert signature(Model.__init__).parameters["self"].annotation is Parameter.empty
    assert signature(Model).return_annotation is Parameter.empty


def test_inherited_overridden_and_excluded_field_annotations():
    @undoable
    class Base:
        inherited: Payload = const()
        changed: int = managed(default=1)
        removed: int = managed(default=2)

    @undoable
    class Child(Base):
        changed: float = managed(default=1.5)
        removed: int = managed(default=3, init=False)
        seed: "UnresolvedSeed" = initvar(default=None)
        hidden: Payload = const(default=None, init=False)
        label: str = classvar(default="child")
        scratch: dict = local_store(default_factory=dict)

    expected = {"inherited": Payload, "changed": float, "seed": "UnresolvedSeed"}
    assert Child.__init__.__annotations__ == expected
    params = signature(Child).parameters
    assert tuple(params) == ("transaction_manager", *expected)
    assert all(
        params[name].annotation is annotation for name, annotation in expected.items()
    )
    assert Base.__init__.__annotations__ == {
        "inherited": Payload,
        "changed": int,
        "removed": int,
    }
    assert Child.__undoable_schema__.annotations["hidden"] is Payload
    assert Child.__dict__.get("__annotations__", {}) == {}


def test_explicit_and_postponed_strings_stay_unevaluated():
    namespace = {}
    exec(
        compile(
            "from __future__ import annotations\n"
            "from yidl_undoable import undoable, managed\n"
            "@undoable\n"
            "class Model:\n"
            "    value: MissingPayload = managed()\n"
            "    other: 'ExplicitPayload' = managed(default=None)\n",
            "<postponed-undoable-annotations>",
            "exec",
            dont_inherit=True,
        ),
        namespace,
    )
    model = namespace["Model"]
    expected = {"value": "MissingPayload", "other": "'ExplicitPayload'"}
    assert model.__init__.__annotations__ == expected
    assert {
        name: parameter.annotation
        for name, parameter in signature(model).parameters.items()
        if name != "transaction_manager"
    } == expected


def test_zero_constructor_fields_have_no_invented_annotations():
    @undoable
    class Model:
        hidden: int = managed(default=0, init=False)
        cache: dict = local_store(default_factory=dict)
        label: str = classvar(default="node")

    assert Model.__init__.__annotations__ == {}
    assert tuple(signature(Model).parameters) == ("transaction_manager",)


def test_mutable_lazy_annotation_uses_the_same_runtime_path():
    @undoable
    class Model:
        value: int = lazy(default_factory=int, mutable=True)

    assert Model.__init__.__annotations__ == {"value": int}
    assert signature(Model).parameters["value"].annotation is int
    assert signature(Model).parameters["value"].default is _HAS_DEFAULT_FACTORY

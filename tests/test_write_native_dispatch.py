"""Test-first native operand/dispatch traces through custom-freeze managed values."""

from collections.abc import Mapping
from types import MappingProxyType
import pytest
from yidl_undoable import undoable, managed, UndoRedoManager


class NativePayload:
    def __init__(self, payload):
        self.payload = payload

    def __eq__(self, other):
        return self.payload == other.payload


def write_native_pair(old, new):
    @undoable(eq=True)
    class Parent:
        value: object = managed(
            default=None,
            compare=False,
            freeze=lambda value: None,
            thaw=lambda baseline: old,
        )

    manager = UndoRedoManager()
    parent = Parent(transaction_manager=manager)
    manager.initialize(parent)
    manager.begin()
    assert parent.working.value is old
    parent.value = new
    actual = manager._edit.touched[parent.node_id, "value"] is old
    manager.rollback()
    return actual


@pytest.mark.parametrize("direction", (False, True))
def test_acceptoriginal_gets_identical_inner_list_in_both_directions(direction):
    @undoable(eq=True)
    class Child:
        value: int = managed(default=2)

    manager = UndoRedoManager()
    child = Child(transaction_manager=manager)
    manager.initialize(child)
    inner = [child]
    trace = []

    class AcceptOriginal:
        def __eq__(self, other):
            trace.append(other is inner)
            return other is inner

    left, right = (AcceptOriginal(),), (inner,)
    if direction:
        left, right = right, left
    assert bool(left == right) is True and trace == [True]
    trace.clear()
    assert write_native_pair(NativePayload(left), NativePayload(right)) is True
    assert trace == [True]


@pytest.mark.parametrize("container", (tuple, list))
@pytest.mark.parametrize("direction", (False, True))
@pytest.mark.parametrize("result", ("true", "false", "truth", "raise"))
def test_native_unequal_length_prefix_callbacks(container, direction, result):
    trace = []

    class Truth:
        def __bool__(self):
            trace.append("truth")
            return True

    failure = ValueError("prefix")

    class Prefix:
        def __eq__(self, other):
            trace.append("eq")
            if result == "raise":
                raise failure
            return Truth() if result == "truth" else result == "true"

    left, right = container((Prefix(),)), container((object(), object()))
    if direction:
        left, right = right, left
    try:
        expected = bool(left == right)
    except ValueError as caught:
        assert caught is failure
        expected = failure
    expected_trace = trace[:]
    trace.clear()
    if expected is failure:
        with pytest.raises(ValueError) as caught:
            write_native_pair(NativePayload(left), NativePayload(right))
        assert caught.value is failure
    else:
        assert write_native_pair(NativePayload(left), NativePayload(right)) is expected
    assert trace == expected_trace


@pytest.mark.parametrize("keys", ("shared", "distinct", "collision", "key-error"))
def test_native_dictionary_cached_hashes_order_and_key_errors(keys):
    trace = []
    ready = [False]
    failure = ValueError("key")

    class Key:
        def __init__(self, value):
            self.value = value

        def __hash__(self):
            if ready[0]:
                raise AssertionError("rehash after preparation")
            return 7

        def __eq__(self, other):
            trace.append(("key", self.value, other.value))
            if keys == "key-error":
                raise failure
            return self.value == other.value

    class Value:
        def __init__(self, value):
            self.value = value

        def __eq__(self, other):
            trace.append(("value", self.value, other.value))
            return self.value == other.value

    shared = Key("a")
    left = {shared: Value(1)}
    right = {shared if keys == "shared" else Key("a"): Value(1)}
    if keys == "collision":
        left[Key("b")] = Value(2)
        right[Key("b")] = Value(3)
    trace.clear()
    ready[0] = True
    try:
        expected = bool(left == right)
    except ValueError as caught:
        assert caught is failure
        expected = failure
    expected_trace = trace[:]
    trace.clear()
    if expected is failure:
        with pytest.raises(ValueError) as caught:
            write_native_pair(NativePayload(left), NativePayload(right))
        assert caught.value is failure
    else:
        assert write_native_pair(NativePayload(left), NativePayload(right)) is expected
    assert trace == expected_trace


@pytest.mark.parametrize(
    "shapes", ("dict-proxy", "proxy-dict", "proxy-proxy", "custom-proxy")
)
def test_native_proxy_forwarding_preserves_original_callback_operands(shapes):
    trace = []

    class Value:
        def __eq__(self, other):
            trace.append(("value", other is original))
            return other is original

    original = ["original"]
    left = {"key": Value()}
    right = {"key": original}
    backing = left

    class Custom(Mapping):
        def __iter__(self):
            return iter(backing)

        def __len__(self):
            return len(backing)

        def __getitem__(self, key):
            return backing[key]

        def __eq__(self, other):
            trace.append(("mapping", other is right))
            return backing == other

    if shapes == "custom-proxy":
        left = MappingProxyType(Custom())
    elif shapes.startswith("proxy"):
        left = MappingProxyType(left)
    if shapes.endswith("proxy"):
        right = MappingProxyType(right)
    expected = bool(left == right)
    expected_trace = trace[:]
    trace.clear()
    assert write_native_pair(NativePayload(left), NativePayload(right)) is expected
    assert trace == expected_trace


def test_native_container_identity_shortcuts_keep_nonreflexive_elements():
    trace = []

    class Nonreflexive:
        def __eq__(self, other):
            trace.append("eq")
            return False

    value = Nonreflexive()
    for container in (tuple, list):
        left, right = container((value,)), container((value,))
        assert bool(left == right) is True
        assert write_native_pair(NativePayload(left), NativePayload(right)) is True
    assert trace == []


@pytest.mark.parametrize("shape", ("tuple", "list", "nested-dict", "proxy"))
def test_nested_equal_structural_leaves_match_original_runtime_facade_oracle(shape):
    from yidl_undoable.facades import RuntimeFacade

    @undoable(eq=True)
    class Child:
        value: int = managed(default=2)

    manager = UndoRedoManager()
    a = Child(transaction_manager=manager)
    b = Child(transaction_manager=manager)
    manager.initialize(a, b)

    def build(value):
        if shape == "tuple":
            return (value,)
        if shape == "list":
            return [value]
        if shape == "nested-dict":
            return {"nested": [(value,)]}
        return MappingProxyType({"nested": (value,)})

    raw = []
    for original in (a, b):
        item = object.__new__(RuntimeFacade)
        item._u_state = original._u_state
        item._u_view = "default"
        item._u_pin = None
        raw.append(item)
    expected = bool(build(raw[0]) == build(raw[1]))
    assert expected is False and bool(build(a) == build(b)) is True
    assert (
        write_native_pair(NativePayload(build(a)), NativePayload(build(b))) is expected
    )


def test_nested_dictionary_and_set_dispatch_keep_original_opaque_values():
    trace = []
    hashed = [False]

    class Key:
        def __hash__(self):
            if hashed[0]:
                raise AssertionError("extra nested hash")
            return 11

        def __eq__(self, other):
            trace.append("key")
            return True

    left = {"nested": {Key()}, "dict": {"inner": [1, 2]}}
    right = {"nested": {Key()}, "dict": {"inner": [1, 2]}}
    hashed[0] = True
    expected = bool(left == right)
    expected_trace = trace[:]
    trace.clear()
    assert write_native_pair(NativePayload(left), NativePayload(right)) is expected
    assert trace == expected_trace

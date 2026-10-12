"""Test-first callback/fence/context lifetime at the native write boundary."""

from contextvars import Context, copy_context
import asyncio
from dataclasses import fields
import threading
import pytest
from yidl_undoable import (
    undoable,
    managed,
    UndoRedoManager,
    ReentrantOperationError,
    HistoryFaultError,
)
from yidl_undoable.facades import RuntimeFacade


def models():
    @undoable(eq=True, order=True)
    class Child:
        value: int = managed(default=2)

    working = [None]

    @undoable
    class Parent:
        value: object = managed(
            default=None, freeze=lambda value: None, thaw=lambda value: working[0]
        )

    manager = UndoRedoManager()
    a = Child(transaction_manager=manager)
    b = Child(transaction_manager=manager)
    parent = Parent(transaction_manager=manager)
    manager.initialize(parent, a, b)
    manager._test_working = working
    return manager, a, b, parent


def scope_module():
    from yidl_undoable import write_comparison_context

    return write_comparison_context


def stage_callback(callback):
    manager, a, b, parent = models()
    manager.begin()

    # Existing custom thaw installs the opaque original as owned working value.
    class Old:
        def __eq__(self, other):
            return callback(manager, a, b, other)

    old = Old()
    manager._test_working[0] = old
    assert parent.working.value is old
    return manager, a, b, parent, old


def test_opaque_callback_uses_historical_identity_inside_existing_fence():
    observations = []

    def callback(manager, a, b, other):
        observations.append(
            (a == b, a == a.current, a.__eq__(object()), manager._callback_depth)
        )
        return False

    manager, a, b, parent, old = stage_callback(callback)
    parent.value = object()
    assert observations == [(False, True, False, 1)]
    assert a == b and scope_module()._historical_write_scope.get() is None
    manager.rollback()


@pytest.mark.parametrize(
    "failure", (ValueError("equality"), KeyboardInterrupt("cancel"))
)
def test_equality_exception_closes_marker_and_preserves_identity_notes(failure):
    captured = []

    def callback(manager, a, b, other):
        captured.append(copy_context())
        raise failure

    manager, a, b, parent, old = stage_callback(callback)
    with pytest.raises(type(failure)) as caught:
        parent.value = object()
    assert caught.value is failure and any(
        "comparison" in note for note in failure.__notes__
    )
    module = scope_module()
    marker = captured[0].get(module._historical_write_scope)
    assert marker.active is False and module._historical_write_scope.get() is None
    assert captured[0].run(lambda: a == b) and a == b
    manager.rollback()


def test_truth_conversion_exception_and_result_use_native_bool():
    captured = []
    events = []
    original = TypeError("truth")

    class Result:
        def __bool__(self):
            events.append("bool")
            raise original

    def callback(manager, a, b, other):
        captured.append(copy_context())
        return Result()

    manager, a, b, parent, old = stage_callback(callback)
    with pytest.raises(TypeError) as caught:
        parent.value = object()
    assert caught.value is original and events == ["bool"]
    module = scope_module()
    assert captured[0].get(module._historical_write_scope).active is False and a == b
    manager.rollback()


@pytest.mark.parametrize("action", ("begin", "rollback", "undo", "write"))
def test_context_never_bypasses_manager_mutation_fence(action):
    captured = []

    def callback(manager, a, b, other):
        captured.append(copy_context())
        if action == "write":
            a.value = 9
        else:
            getattr(manager, action)()

    manager, a, b, parent, old = stage_callback(callback)
    token = manager.active_transaction_for()
    with pytest.raises(ReentrantOperationError):
        parent.value = object()
    assert (
        manager.active_transaction_for() is token
        and a == b
        and manager._callback_depth == 0
    )
    module = scope_module()
    assert captured[0].get(module._historical_write_scope).active is False
    manager.rollback()


def test_ownership_fault_closes_scope_before_fence_faults_manager():
    captured = []

    def callback(manager, a, b, other):
        captured.append(copy_context())
        manager._edit = None
        return False

    manager, a, b, parent, old = stage_callback(callback)
    with pytest.raises(HistoryFaultError):
        parent.value = object()
    module = scope_module()
    assert captured[0].get(module._historical_write_scope).active is False
    assert module._historical_write_scope.get() is None and manager._callback_depth == 0


def test_nested_scopes_restore_outer_and_closed_inner_context_cannot_reactivate():
    manager, a, b, parent = models()
    module = scope_module()
    captured = []
    events = []

    class Inner:
        def __eq__(self, other):
            captured.append(copy_context())
            events.append(a == b)
            return True

    class Outer:
        def __eq__(self, other):
            outer = module._historical_write_scope.get()
            captured.append(copy_context())
            assert module._historical_write_equal(Inner(), object())
            assert module._historical_write_scope.get() is outer and outer.active
            assert captured[-1].run(lambda: a == b) is True
            events.append(a == b)
            return True

    assert module._historical_write_equal(Outer(), object())
    assert events == [False, False] and all(
        context.run(lambda: a == b) for context in captured
    )
    markers = [context.get(module._historical_write_scope) for context in captured]
    assert len({id(marker) for marker in markers}) == 2
    assert [field.name for field in fields(markers[0])] == ["active"]
    assert markers[0].__slots__ == ("active",) and all(
        marker.active is False for marker in markers
    )
    assert module._historical_write_scope.get() is None


def test_copied_and_empty_explicit_thread_contexts_expire_after_scope():
    manager, a, b, parent = models()
    module = scope_module()
    observations = []
    captured = []

    def run(context):
        thread = threading.Thread(
            target=lambda: observations.append(context.run(lambda: a == b))
        )
        thread.start()
        thread.join(5)
        assert not thread.is_alive()

    class Value:
        def __eq__(self, other):
            captured.append(copy_context())
            run(Context())
            run(copy_context())
            return True

    assert module._historical_write_equal(Value(), object())
    run(captured[0])
    assert observations == [True, False, True]


def test_async_context_copies_before_and_after_closed_marker():
    async def scenario():
        manager, a, b, parent = models()
        module = scope_module()
        observations = []
        tasks = []

        async def later():
            observations.append(a == b)

        class Value:
            def __eq__(self, other):
                tasks.append(asyncio.create_task(later()))
                observations.append(copy_context().run(lambda: a == b))
                return True

        assert module._historical_write_equal(Value(), object())
        await tasks[0]
        assert observations == [False, True] and a == b

    asyncio.run(scenario())


def test_scoped_order_remains_structural_and_hash_stays_disabled():
    manager, a, b, parent = models()
    module = scope_module()
    with manager.begin():
        b.value = 3

    class Value:
        def __eq__(self, other):
            assert a < b and a.current < b.current
            with pytest.raises(TypeError):
                hash(a)
            return False

    assert module._historical_write_equal(Value(), object()) is False
    with pytest.raises(TypeError):
        hash(a)


def test_cross_manager_nested_callback_restores_outer_scope_and_ownership():
    second = []
    captured = []
    events = []

    def inner_callback(manager, a, b, other):
        captured.append(copy_context())
        events.append(a == b)
        return False

    inner_manager, inner_a, inner_b, inner_parent, inner_old = stage_callback(
        inner_callback
    )

    def outer_callback(manager, a, b, other):
        module = scope_module()
        outer = module._historical_write_scope.get()
        captured.append(copy_context())
        inner_parent.value = object()
        assert module._historical_write_scope.get() is outer and outer.active
        events.append(a == b)
        assert captured[-1].run(lambda: inner_a == inner_b) is True
        return False

    manager, a, b, parent, old = stage_callback(outer_callback)
    parent.value = object()
    assert (
        events == [False, False]
        and manager._callback_depth == inner_manager._callback_depth == 0
    )
    assert all(context.run(lambda: inner_a == inner_b) for context in captured)
    manager.rollback()
    inner_manager.rollback()


def test_identity_write_has_no_new_scope_or_equality_callback():
    module = scope_module()
    contexts = []

    class Value:
        def __eq__(self, other):
            raise AssertionError("identity policy invoked equality")

    value = Value()

    @undoable(eq=True)
    class Parent:
        value: object = managed(
            default=None,
            compare=False,
            write_compare="identity",
            freeze=lambda value: None,
            thaw=lambda baseline: value,
        )

    manager = UndoRedoManager()
    parent = Parent(transaction_manager=manager)
    manager.initialize(parent)
    manager.begin()
    assert parent.working.value is value
    before = module._historical_write_scope.get()
    parent.value = value
    assert module._historical_write_scope.get() is before
    parent.value = Value()
    assert module._historical_write_scope.get() is before
    manager.rollback()


def test_native_cycle_outcomes_are_not_replaced_by_custom_detection():
    module = scope_module()
    first = []
    first.append(first)
    other = []
    other.append(other)
    assert bool(first == first) is module._historical_write_equal(first, first) is True
    with pytest.raises(RecursionError):
        bool(first == other)
    with pytest.raises(RecursionError):
        module._historical_write_equal(first, other)
    assert module._historical_write_scope.get() is None


def test_reflected_subclass_priority_and_notimplemented_stay_native():
    manager, a, b, parent = models()
    trace = []

    class Derived(type(a)):
        def __eq__(self, other):
            trace.append("derived")
            return NotImplemented

    derived = object.__new__(Derived)
    derived._u_state = a._u_state
    derived._u_view = "default"
    derived._u_pin = None

    def callback(own_manager, _left, _right, other):
        assert a == derived
        assert trace == ["derived"]
        assert a.__eq__(object()) is False
        return False

    outer, x, y, parent, old = stage_callback(callback)
    parent.value = object()
    assert a.__eq__(derived) is NotImplemented
    outer.rollback()


def test_inflight_active_sample_can_finish_after_marker_closure():
    manager, a, b, parent = models()
    module = scope_module()
    entered = threading.Event()
    release = threading.Event()
    block = [False]
    result = []
    threads = []
    captured = []

    class Slow(type(a)):
        def __getattribute__(self, name):
            if name == "_u_state" and block[0]:
                entered.set()
                assert release.wait(5)
            return super().__getattribute__(name)

    left = object.__new__(Slow)
    right = object.__new__(Slow)
    for target, original in ((left, a), (right, b)):
        target._u_state = original._u_state
        target._u_view = "default"
        target._u_pin = None

    class Value:
        def __eq__(self, other):
            captured.append(copy_context())
            block[0] = True
            thread = threading.Thread(
                target=lambda: result.append(captured[0].run(lambda: left == right))
            )
            threads.append(thread)
            thread.start()
            assert entered.wait(5)
            return True

    try:
        assert module._historical_write_equal(Value(), object())
        assert captured[0].get(module._historical_write_scope).active is False
    finally:
        block[0] = False
        release.set()
        for thread in threads:
            thread.join(5)
            assert not thread.is_alive()
    assert result == [False]
    assert captured[0].run(lambda: left == right) is True


def test_scope_native_nonboolean_return_is_truth_converted_once_and_retains_no_operands():
    import gc
    import weakref

    module = scope_module()
    captured = []
    trace = []

    class Truth:
        def __bool__(self):
            trace.append("bool")
            return True

    class Value:
        def __eq__(self, other):
            captured.append(copy_context())
            return Truth()

    left = Value()
    right = Value()
    refs = (weakref.ref(left), weakref.ref(right))
    assert module._historical_write_equal(left, right) is True and trace == ["bool"]
    del left, right
    gc.collect()
    assert all(reference() is None for reference in refs)
    assert captured[0].get(module._historical_write_scope).active is False


def test_async_task_explicit_copy_runs_while_active_then_after_closure():
    manager, a, b, parent = models()
    module = scope_module()
    observations = []
    entered = threading.Event()
    release = threading.Event()
    threads = []
    captured = []

    async def worker():
        observations.append(a == b)
        entered.set()
        await asyncio.to_thread(release.wait)
        observations.append(a == b)

    class Value:
        def __eq__(self, other):
            captured.append(copy_context())
            thread = threading.Thread(
                target=lambda: captured[0].run(asyncio.run, worker())
            )
            threads.append(thread)
            thread.start()
            assert entered.wait(5)
            return True

    try:
        assert module._historical_write_equal(Value(), object())
    finally:
        release.set()
        for thread in threads:
            thread.join(5)
            assert not thread.is_alive()
    assert observations == [False, True]


def test_pinned_same_state_and_equal_distinct_states_use_historical_identity():
    manager, a, b, parent = models()
    module = scope_module()
    old = a._u_state.facade("current", (manager._selection.epoch, manager.frame_id))
    with manager.begin():
        a.value = 3
    assert old != a.current and old == b.current
    assert module._historical_write_equal(old, a.current) is True
    assert module._historical_write_equal(old, b.current) is False
    assert old != a.current and old == b.current

import pytest
from yidl_undoable import *


class Truth:
    def __init__(self, key, result):
        self.key, self.result = key, result

    def __bool__(self):
        self.key.invoke("truth")
        return self.result


class Key:
    action = None
    event = "equality"
    remaining = 0
    hits = 0

    def arm(self, event, nth, action):
        self.event, self.remaining, self.action, self.hits = event, nth, action, 0

    def invoke(self, event):
        if self.action is not None and event == self.event:
            self.hits += 1
            self.remaining -= 1
            if self.remaining == 0:
                action, self.action = self.action, None
                action()

    def __hash__(self):
        self.invoke("hash")
        return 37

    def __eq__(self, other):
        self.invoke("equality")
        return Truth(self, self is other)

    def __ne__(self, other):
        self.invoke("equality")
        return Truth(self, self is not other)

    def __repr__(self):
        self.invoke("repr")
        return "KEY"


KEY = Key()


@undoable
class Model:
    value: int = managed(KEY, default=0)
    scratch: int = transient(KEY, default=0)

    @validate_commit(KEY)
    def valid(self):
        return True


CASES = [
    (operation, nth)
    for operation, count in (
        ("commit", 2),
        ("rollback", 2),
        ("join", 2),
        ("read", 2),
        ("scope_commit", 1),
        ("scope_rollback", 1),
        ("register", 3),
        ("validate", 1),
    )
    for nth in range(1, count + 1)
]


@pytest.mark.parametrize("event", ("equality", "truth"))
@pytest.mark.parametrize("operation,nth", CASES)
def test_key_callbacks_cannot_replace_original_edit(event, operation, nth):
    KEY.action = None
    h = UndoRedoManager(tx_key=KEY)
    node = Model(transaction_manager=h)
    h.initialize(node)
    token = h.begin(KEY)
    node.value = 7
    owner = h._edit
    nodes = set(h._nodes)

    def replace():
        h.rollback(KEY)
        h.begin(KEY)
        node.value = 99

    KEY.arm(event, nth, replace)
    operations = {
        "commit": lambda: h.commit(KEY),
        "rollback": lambda: h.rollback(KEY),
        "join": lambda: h.begin(KEY),
        "read": lambda: h.active_transaction_for(KEY),
        "scope_commit": token._scope_commit,
        "scope_rollback": token._scope_rollback,
        "register": lambda: Model(transaction_manager=h),
        "validate": lambda: h.validate(KEY),
    }
    with pytest.raises(ReentrantOperationError):
        operations[operation]()
    assert KEY.hits == nth and KEY.action is None
    assert h._edit is owner and h.active_transaction_for(KEY) is token
    assert token.completion is None and h._backend.begin_count == 1
    assert node.value == 7 and node.current.value == 0 and h.frame_count == 1
    assert set(h._nodes) == nodes
    h.commit(KEY)
    assert (
        node.value == 7
        and h.frame_count == 2
        and h.last_completion.tx_id == token.tx_id
    )


@pytest.mark.parametrize("event", ("equality", "truth", "repr"))
def test_wrong_key_callbacks_and_diagnostics_preserve_owner(event):
    KEY.action = None
    h = UndoRedoManager(tx_key=KEY)
    node = Model(transaction_manager=h)
    h.initialize(node)
    token = h.begin(KEY)
    node.value = 7
    wrong = Key()
    wrong.arm(event, 1, lambda: h.rollback(KEY))
    with pytest.raises(ReentrantOperationError):
        h.commit(wrong)
    assert wrong.hits == 1 and h.active_transaction_for(KEY) is token
    assert node.value == 7 and token.completion is None
    with pytest.raises(RuntimeError, match="unknown transaction key"):
        h.commit(wrong)
    assert h.active_transaction_for(KEY) is token and h._backend.begin_count == 1
    h.commit(KEY)
    assert node.value == 7


@pytest.mark.parametrize("event", ("equality", "truth"))
def test_begin_enlist_key_callback_clean_abort_and_retry(event):
    KEY.action = None
    h = UndoRedoManager(tx_key=KEY)
    node = Model(transaction_manager=h)
    h.initialize(node)
    KEY.arm(event, 3, lambda: h.rollback(KEY))
    with pytest.raises(ReentrantOperationError):
        h.begin(KEY)
    assert KEY.hits == 3 and h.active_transaction_for(KEY) is None
    assert h._edit is None and h._backend.begin_count == 0 and h.frame_count == 1
    with h.begin(KEY):
        node.value = 7
    assert node.value == 7 and h.frame_count == 2


@pytest.mark.parametrize("event", ("equality", "truth"))
def test_setup_abort_key_callback_fault_keeps_both_causes(monkeypatch, event):
    from yidl_undoable import transaction_yidl as runtime

    KEY.action = None
    h = UndoRedoManager(tx_key=KEY)
    node = Model(transaction_manager=h)
    h.initialize(node)
    setup_failure = MemoryError("overlay")

    def fail_overlay(*args, **kwargs):
        raise setup_failure

    monkeypatch.setattr(runtime, "EditOverlay", fail_overlay)
    KEY.arm(event, 3, lambda: h.rollback(KEY))
    with pytest.raises(HistoryFaultError) as caught:
        h.begin(KEY)
    causes = caught.value.__cause__.exceptions
    assert causes[0] is setup_failure and isinstance(causes[1], ReentrantOperationError)
    assert h._edit is None and h._prepared is None and node.value == 0
    assert h.last_completion is None and h._backend.active_transaction is not None
    with pytest.raises(HistoryFaultError):
        h.begin(KEY)


def test_manager_key_hashing_rejects_mutation_during_construction():
    key = Key()
    h = object.__new__(UndoRedoManager)
    key.arm("hash", 1, h.begin)
    with pytest.raises(ReentrantOperationError):
        h.__init__(tx_key=key)
    assert key.hits == 1 and h._callback_depth == 0
    h.__init__(tx_key=key)
    assert h.tx_key is key and h._callback_depth == 0


@pytest.mark.parametrize("event", ("equality", "truth"))
def test_key_callback_validate_rejects_before_recursive_key_comparison(event):
    KEY.action = None
    h = UndoRedoManager(tx_key=KEY)
    node = Model(transaction_manager=h)
    h.initialize(node)
    token = h.begin(KEY)
    node.value = 7

    def validate_repeatedly():
        KEY.action, KEY.remaining = validate_repeatedly, 1
        h.validate(KEY)

    KEY.arm(event, 1, validate_repeatedly)
    try:
        with pytest.raises(ReentrantOperationError):
            h.commit(KEY)
        assert KEY.hits == 1
    finally:
        KEY.action = None
    assert h.active_transaction_for(KEY) is token and token.completion is None
    assert h._backend.begin_count == 1 and node.value == 7 and h.frame_count == 1
    h.commit(KEY)
    assert node.value == 7 and h.frame_count == 2


def test_backend_failure_key_diagnostic_keeps_mutation_fenced(monkeypatch):
    KEY.action = None
    h = UndoRedoManager(tx_key=KEY)
    node = Model(transaction_manager=h)
    h.initialize(node)
    token = h.begin(KEY)
    node.value = 7
    failure = LookupError("synthetic preparation failure")
    changed = []

    def fail_prepare(key, tx_id):
        raise failure

    def change_pending_value():
        node.value = 99
        changed.append(True)

    monkeypatch.setattr(h._aggregate, "_prepare_commit_tx_by_key", fail_prepare)
    KEY.arm("repr", 1, change_pending_value)
    with pytest.raises(LookupError) as caught:
        h.commit(KEY)
    assert caught.value is failure and KEY.hits == 1 and not changed
    assert token.completion.discard_complete and token.completion.finalized
    assert (
        node.value == 0 and h.frame_count == 1 and h.active_transaction_for(KEY) is None
    )
    monkeypatch.undo()
    with h.begin(KEY):
        node.value = 7
    assert node.value == 7 and h.frame_count == 2

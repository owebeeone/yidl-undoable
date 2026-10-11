# YIDL Undoable implementation — STATE-AXIS REVIEW

**Review object:** Complete `yidl_undoable` runtime package, tests, examples, generation resources, README/docs and configuration at `38662bcbbe7758fb5f980859675fa9efcb41d614`. Local implementation draft; runtime acceptance pending. Implementation diff from `72e1433e1290cc41392223c9d5981847e396f68e`. Controlling design accepted at `616f2f65473b1240535a6317d8cc79d5cec18414`; implementation plan at `3440ec2fcee3a8d61c1f88cdfbafafc0683edabf`.

**Baseline:**

| Repository | Exact revision |
| --- | --- |
| `yidl_undoable` | `38662bcbbe7758fb5f980859675fa9efcb41d614` |
| `yidl-lifecycle` | `230362f642d6e9205897698670fe5f87d2c905ce` |
| `yidl` | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| `astichi` | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| `yidl-cache` | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Sources were read from the canonical workspace checkouts using read-only inspection. The exact tuple matched at the beginning and end. Final Git comparisons showed no working-tree differences in runtime sources, tests, examples, README, public documentation or configuration. The controlling design and implementation plan match their accepted revisions.

**Date:** 2026-10-12

**Axis:** In-memory state transitions, callback and backend-token ownership, publication ordering, failure closure, branch abandonment and pinned-state consistency. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: NO-GO** — one new P2 finding blocks acceptance. No P0, P1 or P3 findings. All five historical State counterexamples are closed. I pre-commit to GO on a revision that resolves round 3 P2-1 as specified.

---

## Prior-finding closure table

Historical IDs retain their round namespace. Round 3 P2-1 below is a separate finding.

| ID | Disposition claimed | Verified on corrected tree | Status |
| --- | --- | --- | --- |
| State round 1 P2-1 | Healthy discard requires unchanged selection; installed selection requires confirmed publication. | Independently replayed failure immediately after the original apply callback, and after selection assignment without identity bookkeeping. Both raise `HistoryFaultError`, detach the overlay and reject begin/navigation. Bookkept installed value `7` remains readable; missing bookkeeping blocks live reads and snapshots. | Closed. |
| State round 1 P2-2 | Candidate pins preserve active ordinary/default/working transient values and current baseline values. | Independently replayed the original negative-scratch validator with managed value `10` and scratch `-1`. Candidate reads were `(-1, -1, 0, -1)`; preview and final commit rejected. Final failure retained managed value `0`, cleared scratch and published no frame. Canonical story 16 also passed provider fencing, repair and redo preservation. | Closed. |
| State round 1 P2-3 | Snapshot nodes compare/hash by pinned context and node identity. | Independently replayed a managed frozenset containing a child node. Snapshot decoding, identity, membership and hashing succeeded. The old child snapshot remained readable after a live branch removed the edge. Canonical story 17 passed nested mapping/tuple/frozenset alias checks. | Closed. |
| State round 1 P2-4 | Failed enlist detaches editable state; abort failure faults immediately with causal evidence. | Independently replayed failed enlist plus rollback failure before closure and after closure. Both raise `HistoryFaultError`, retain both causes, detach the overlay, preserve old confirmed reads and reject subsequent begin. The successful-abort enlist case also passed. | Closed. |
| State round 2 P2-1 | Enclose backend acquisition, overlay allocation, enlistment and scope binding in one failure-safe begin boundary, including joined setup. | Independently replayed backend begin raising after token acquisition, overlay allocation raising `MemoryError`, and final Undoable scope binding raising. Confirmed cleanup left no token, nesting or overlay. A retried scope published exactly one additional frame and became idle. Joined backend-return and wrapper-binding failures also closed the joined edit. The targeted fault matrix passed abort failures before/after closure and backend-binding failures. | Closed. |

## Changed-range analysis

Comparison against `72e1433e1290cc41392223c9d5981847e396f68e` identified one changed runtime file:

- `src/yidl_undoable/transaction_yidl.py:242–336` captures ownership before backend begin and encloses acquisition, overlay construction, enlistment, scope binding and final ownership checks. `_abort_begin_setup` identifies the owned token, attempts abort, always detaches private state, and distinguishes confirmed closure from faulted ownership/cleanup.
- `src/yidl_undoable/transaction_yidl.py:489–518` moves provisional projection and thaw inside the operation fence, and recursively projects ordinary provisional values to the requested view.
- `tests/test_begin_setup_faults.py` and `tests/test_provisional_fences.py` add narrow setup/ownership and application-backed mapping cases. Canonical story 18 and its generated golden cover provisional child-view propagation.
- `docs/API.md` documents provisional propagation and whole-edit abort following failed joined begin setup.
- Checkpoint, implementation/TDD/verification evidence and prior review material record the remediation. Review prompts, reports and measurement outputs are outside the runtime object.

These runtime changes fit the cycle 2 dispositions. They do not alter the accepted architecture or public API.

The new finding concerns transaction-key equality outside the callback fence. It is an existing call-path gap exposed while attacking transaction authority; it is not caused by the provisional projection correction. It is a **new bounded implementation root**, **not a new architectural root**. The accepted callback ownership mechanism and transaction model can address it without redesign.

## 0. Evidence base

### Documents and sources inspected

Read workspace `AGENTS.md` and `AGENTS_GWZ.md`, the complete canonical State Round 3 prompt, both historical State reports, and both merged remediation plans.

Read the controlling checkpoint, design and implementation plan, concentrating on construction, field/view semantics, operation ownership, sparse histories, snapshots, publication and failure closure. Read README, API/architecture documentation, examples, packaging configuration, implementation draft, TDD evidence and independent verification evidence. Recorded results were treated as claims to inspect, not acceptance proof.

Runtime inspection included:

- `src/yidl_undoable/transaction_yidl.py:1–677`: aggregate callbacks, initialization, candidate preparation, complete begin boundary, live reads/writes, navigation and completion diagnosis.
- `src/yidl_undoable/facades.py:1–328`: constructor/provider resolution, view identity, lazy/transient materialization and write guards.
- Complete `callbacks.py`, `states.py`, `values.py`, `graph.py`, `history.py`, `snapshots.py` and `policies.py`.
- Decorator and harvester implementation, generation tests and canonical harness.
- Canonical construction, callback, transient validation, snapshot identity and provisional child-view stories, plus diagnostic, history, remediation and setup-fault tests.
- In `yidl-lifecycle`, transaction identity and scope binding, completion discard/publication/finalization, backend begin and keyed completion dispatch in `src/yidl_lifecycle/transaction_yidl.py`.

No other current-round report was accessed. No additional agents were spawned.

### Commands and results

From the canonical workspace root, `git -C <member> rev-parse HEAD` verified all five revisions at start and end. Read-only Git diff established the changed ranges, unchanged runtime working tree and controlling-document equality.

From `yidl_undoable`:

```sh
PYTHONDONTWRITEBYTECODE=1 ../.venv/bin/python -m pytest -q -p no:cacheprovider \
  tests/test_canonical.py tests/test_begin_setup_faults.py \
  tests/test_provisional_fences.py tests/test_faults.py \
  tests/test_remediation_faults.py tests/test_remediation_diagnostics.py \
  tests/test_adversarial_diagnostics.py tests/test_state_diagnostics.py \
  tests/test_history.py tests/test_annotation_recognition.py \
  tests/test_definitions.py \
  tests/test_generation.py::test_matcher_selected_executable_surface
```

Result: **88 passed in 6.17s**.

This executes all eighteen canonical stories and compares their generated source with committed goldens. The layer story exercises the nine inheritable concepts. The selected generation test checks executable matcher choices and generated-base equality.

The resource-copy test was excluded because it writes a temporary directory. No builds, installs, regeneration writes, file edits or Git mutations were performed.

Independent in-memory probes used:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src ../.venv/bin/python - <<'PY'
# In-memory probe body
PY
```

One probe independently replayed all five historical State findings and asserted their corrected outcomes. A separate probe reproduced round 3 P2-1 below. Synthetic replacements existed only within their Python processes and were restored before subsequent operations.

## 1. Findings

### [P2-1] Transaction-key equality can replace the edit before commit captures its token

**Location:** `src/yidl_undoable/transaction_yidl.py:100–102`, with the affected completion ordering at `348–353`. Begin likewise validates the key before capturing ownership at `242–246`. The backend performs further equality-based key checks during dispatch.

**Violated invariant:** Design section 2 supports a caller-configured hashable transaction key. Sections 7 and 10 require application comparison callbacks to run under the same-manager mutation fence and require suspended operations to retain their original transaction authority. Completion must not silently reacquire and publish a replacement token.

`_key` evaluates `key != self.tx_key` directly. A custom key’s equality method therefore runs without a callback fence. In `commit`, this occurs before the active token is passed to `_complete`. Equality can replace the edit, after which the suspended commit captures and publishes the replacement.

**Reproduction:** The following supported custom key has a constant hash and identity equality. Its one-shot equality action uses public manager operations:

```python
from yidl_undoable import *

class Key:
    def __init__(self):
        self.action = None

    def __hash__(self):
        return 37

    def __eq__(self, other):
        action, self.action = self.action, None
        if action:
            action()
        return self is other

    def __repr__(self):
        return "KEY"

key = Key()

@undoable
class Model:
    value: int = managed(key, default=0)

h = UndoRedoManager(tx_key=key)
x = Model(transaction_manager=h)
h.initialize(x)

original = h.begin(key)
x.value = 7
replacement = []

def replace_edit():
    h.rollback(key)
    replacement.append(h.begin(key))
    x.value = 99

key.action = replace_edit
result = h.commit(key)
```

Observed on the reviewed tuple:

```text
commit result:       2
original token ID:   1
replacement token:   2
published value:     99
frame count:         2
manager state:       Idle
active transaction:  None
```

The original pending value `7` was discarded. The call intended to complete token `1` instead successfully completed token `2`. No reentry or ownership error was raised.

**Impact:** An application equality callback can transfer a suspended manager operation to another edit and publish data belonging to the replacement transaction. This defeats the callback/token authority boundary despite the corrected begin setup and completion evidence checks.

**Required correction:** Fence application-backed transaction-key equality and its truth conversion before any state change. Capture the operation’s original ownership before invoking key callbacks and reject reentry or ownership loss. Ensure subsequent backend key validation cannot invoke the same custom callback unfenced; fixing only the first `_key` comparison leaves repeated dispatch comparisons exposed. Preserve the declared custom-hashable-key API and healthy behavior for pure comparisons.

**Closure/regression test:** Add a narrow custom-key diagnostic regression reproducing the sequence above. Assert `ReentrantOperationError` before rollback/replacement, retention of the original token and nesting, pending value `7`, unchanged frame count and no replacement publication. After a pure retry, the original edit must commit normally. Cover equality-result truth conversion and the repeated key-check stages in begin/completion dispatch; wrong-key failures must leave ownership unchanged.

**Classification:** Bounded implementation correction. No architectural redesign is required.

## 2. Invariant analysis

The following attacks did not refute their targeted invariants:

- **Whole begin closure:** The original partial-return, allocation and final-binding failures now close cleanly or fault immediately. Joined setup failure aborts the whole joined edit. Failed abort detaches editable state and preserves causal errors. Unexpected hidden nesting remains faulted after cleanup.
- **Publication diagnosis:** Failure after installed publication faults even when private discard succeeds. Confirmed installed identity permits diagnostic reads; missing identity bookkeeping rejects live reads and snapshots.
- **Transaction-only mutation and nested scopes:** Canonical generated stories reject idle/current managed writes, retain pending versus committed views, make inner commit nonpublishing, abort the entire joined edit on rollback, and reject stale normal scope completion against replacement tokens.
- **Construction and providers:** Setup/provisional dependencies resolve private baselines. Unresolved/recursive providers fail contextually without registering partial nodes. Constructor writes are fenced. Named lazy dependencies materialize through the fenced provider path.
- **Original application callbacks:** Value equality/truth-conversion replacement attempts, transient retained-scope completion, idle lazy begin/navigation and converter/validator reentry remain rejected. Round 3 P2-1 identifies an additional equality entry point outside those protections.
- **Corrected provisional reads:** Ordinary/working child views propagate before and after attachment. Application-backed mapping iteration is fenced before projection/thaw, retains the original token and pending root values, leaves a failed target untouched, and permits a pure retry.
- **Atomic candidates:** Managed validator reads use frozen candidate values through every view. Transient ordinary/default/working reads use token-local values while current uses its baseline. Preview remains repairable; final rejection publishes nothing and preserves redo.
- **Graph membership:** Shared roots/children retain aliases. Foreign edges and final cycles reject. Provisional, omitted, aborted and future-only nodes obey availability rules. Removed final nodes do not publish touched data.
- **Sparse history and branches:** Negative predecessor positions reject. Branch preparation trims untouched future field and presence histories. Empty and equal-valued touched edits produce the specified frames.
- **Absence and snapshots:** Last-visible descendants retain the fallback pin. Snapshot frozensets support cached node identity and hashing. Nested aliases and retained old epochs survive live branching.
- **Stable and nonversioned values:** Recursive stable normalization copies mapping backing stores and rejects invalid keys/cycles. Escaped working containers detach on completion. Const/plain/binding/local/lazy policies and transient cleanup retain their specified behavior.
- **Generation:** Canonical generated-source checks execute all nine concepts and selected field behaviors. Annotation recognition and generated-base equality pass.

The historical failed-begin and incomplete-publication transitions now satisfy their closure requirements. The remaining defect is transaction authority acquired after an unfenced key callback has already replaced the caller’s edit.

No disk persistence, crash recovery, concurrency, collaboration, multikey atomic history, ownership hooks or custom stable-adapter requirements were imposed.

## 3. Risks and next action

Direct execution used the workspace Python environment. Recorded Python 3.12–3.14 and isolated installed-wheel checks were inspected but not independently rerun; this review does not recertify that matrix or packaging.

Trusted converter purity and arbitrary external mutation remain contractual limits. The finding concerns the framework’s promised rejection of same-manager transactional reentry through application comparison callbacks.

The next action is one bounded TDD correction for round 3 P2-1, followed by replay of this key-equality counterexample and retained historical State regressions at a newly settled tuple. Runtime acceptance remains blocked.
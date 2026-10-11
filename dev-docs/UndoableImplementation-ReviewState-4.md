# YIDL Undoable implementation — STATE-AXIS REVIEW

**Review object:** Complete `yidl_undoable` runtime package, tests, examples, generation resources, README/docs and configuration at `d0f85e6005aefb91098d4164663b07e40c7b757e`. Local implementation draft; runtime acceptance pending. Changed-range baseline: `38662bcbbe7758fb5f980859675fa9efcb41d614`. Controlling DRAFT design accepted at `616f2f65473b1240535a6317d8cc79d5cec18414`; implementation plan at `3440ec2fcee3a8d61c1f88cdfbafafc0683edabf`.

**Baseline:**

| Repository | Exact revision |
| --- | --- |
| `yidl_undoable` | `d0f85e6005aefb91098d4164663b07e40c7b757e` |
| `yidl-lifecycle` | `230362f642d6e9205897698670fe5f87d2c905ce` |
| `yidl` | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| `astichi` | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| `yidl-cache` | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Sources were read from the canonical workspace checkouts using read-only inspection. Every revision matched at both the start and end. Git comparisons showed no working-tree differences in runtime sources, tests, examples, README, public documentation or configuration. The controlling design and implementation plan match their specified revisions.

**Date:** 2026-10-12

**Axis:** In-memory state transitions, callback/backend-token authority, publication ordering, failure closure, branch abandonment and pinned-state consistency. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: NO-GO** — one new P2 finding blocks acceptance. No P0, P1 or P3 findings. All six historical State findings are closed. I pre-commit to GO on a revision that resolves round 4 P2-1 as specified.

---

## 0. Evidence base

### Instructions, documents and sources inspected

Read:

- Workspace `AGENTS.md` and `AGENTS_GWZ.md`.
- The complete canonical `dev-docs/review-prompts/UndoableImplementation-State-Round4.md`.
- All three historical State reports and all three merged remediation plans.
- `dev-docs/CurrentProgramCheckpoint.md`, `dev-docs/UndoableDesign.md` and `dev-docs/UndoableImplementationPlan.md`.
- Implementation, TDD and verification evidence, treating recorded success as a claim requiring inspection.
- README, API/architecture documentation, packaging configuration and both examples.

Runtime inspection covered:

- `src/yidl_undoable/transaction_yidl.py:1–709`: initialization, candidate construction, begin setup/abort, scopes, completion, reads/writes, navigation and fault diagnosis.
- Complete `callbacks.py`, `facades.py`, `values.py`, `history.py`, `graph.py`, `snapshots.py`, `states.py`, `policies.py`, bindings and public exports.
- Decorator, harvester and regeneration code; all nine YIDL resources and their matcher-selected contributions.
- Canonical harness/stories, generation and annotation tests, callback diagnostics, setup/cleanup faults and new key/thaw-result regressions.
- Pinned Lifecycle token binding, keyed dispatch, completion sessions, ownership checks and finalization in `yidl-lifecycle/src/yidl_lifecycle/transaction_yidl.py`.

No current-round report from the other axis was accessed. No agents were spawned or consulted.

### Commands and results

Read-only Git commands verified the tuple, changed ranges, unchanged runtime working tree and controlling-document equality.

From `yidl_undoable`:

```sh
PYTHONDONTWRITEBYTECODE=1 ../.venv/bin/python -m pytest -q -p no:cacheprovider \
  tests/test_canonical.py tests/test_begin_setup_faults.py \
  tests/test_provisional_fences.py tests/test_faults.py \
  tests/test_remediation_faults.py tests/test_remediation_diagnostics.py \
  tests/test_adversarial_diagnostics.py tests/test_state_diagnostics.py \
  tests/test_history.py tests/test_annotation_recognition.py \
  tests/test_definitions.py \
  tests/test_generation.py::test_matcher_selected_executable_surface \
  tests/test_transaction_key_fences.py tests/test_thaw_result_fences.py
```

Result: **137 passed in 6.48s**.

This executes all twenty canonical stories, compares their generated source against committed goldens, executes all nine intermediate concepts, and checks matcher-selected executable behavior.

Read-only Python introspection reported **Python 3.12.12** and:

```python
check_undoable_base() == (True, "")
```

The resource-copy test was excluded because it writes temporary files. Recorded Python 3.13/3.14 and installed-wheel checks were inspected but not independently rerun.

Additional in-memory heredoc probes used:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src ../.venv/bin/python - <<'PY'
# In-memory probe body
PY
```

One independently reconstructed and replayed all six historical State roots. Additional probes reproduced the new nonterminal and terminal nesting failures below. Synthetic backend replacements existed only within their Python processes and were restored before subsequent operations.

No writes, builds, installs, regeneration writes, Git mutations or adjacent-source changes were performed.

## 1. Findings

### [P2-1] Completion accepts backend nesting that does not match the authorized transition

**Location:** `src/yidl_undoable/transaction_yidl.py:663–676`, particularly the nonterminal return at `673–676`; the terminal healthy predicate at `683–695` also omits `begin_count == 0`.

**Violated invariant:** Design sections 10–11 require inner completion to discharge exactly one begin, outer completion to close the transaction, and unexpected backend ownership failure to fault. The amended backend dispatch intentionally permits authorized transitions, so its caller must distinguish the expected transition from unexpected nesting changes.

`_complete` captures the selected history but not the pre-completion nesting authority. Whenever terminal evidence is absent and the active token is unchanged, it returns successfully without checking whether an inner completion was authorized or whether nesting decreased by exactly one. The terminal healthy predicate checks that the active token is gone but does not check that nesting was cleared.

**Reproduction — nonterminal failure:**

The following narrow synthetic backend fault inserts an unexpected begin immediately before otherwise normal completion:

```python
from yidl_undoable import *

@undoable
class Model:
    value: int = managed(default=0)

h = UndoRedoManager()
x = Model(transaction_manager=h)
h.initialize(x)
token = h.begin()
x.value = 7

backend_type = type(h._backend)
original_commit = backend_type.commit

def hidden_begin(backend, key):
    backend.begin(key)
    return original_commit(backend, key)

backend_type.commit = hidden_begin
try:
    token.__exit__(None, None, None)
finally:
    backend_type.commit = original_commit

with h.begin():
    x.value = 9
```

Observed after the original outer scope’s successful normal exit:

```text
manager state:       Editing
backend nesting:     1
active token:        original token
pending/current:     7 / 0
frame count:         1
terminal evidence:   None
```

The backend’s unexpected begin made outer completion look like inner completion. Undoable accepted the return because token identity was unchanged.

The subsequent public `with h.begin()` also exited successfully, leaving:

```text
manager state:       Editing
backend nesting:     1
pending/current:     9 / 0
frame count:         1
```

The hidden begin persists and contaminates later scope completion.

A separate application-key probe reproduced the same omission by inserting the backend acquisition during the second comparison in explicit commit dispatch, or the comparison reached through a retained scope callback. Ordinary public callback reentry remains correctly rejected; this probe exercises unexpected backend ownership changes.

**Reproduction — terminal failure:**

On a fresh manager, wrap backend commit to invoke the original successfully, then set `backend.begin_count = 1` before returning.

Observed:

- Commit returned the original token ID.
- Terminal evidence confirmed finalized publication.
- Active backend token was `None`, but backend nesting was `1`.
- Undoable returned to `Idle`.
- `undo()` succeeded.

The coordinator therefore exposed healthy navigation while its backend retained an illegal token/count combination.

**Impact:** Unexpected completion nesting can produce successful scope exits without publication and leave later scopes perpetually joining undisclosed work. Terminal corruption is accepted as healthy and diagnosed only by a later operation. Both violate the declared immediate fail-closed ownership boundary.

**Required correction:** Capture pre-completion authority, including token and nesting, before backend dispatch. Validate the exact permitted transition:

- A successful nonterminal commit must start with genuine joined nesting and reduce it by exactly one while preserving the original token, overlay and selection.
- A failure without terminal evidence may remain repairable only when the original ownership context is unchanged.
- A terminal healthy outcome must leave both active token absent and nesting zero.
- Unexpected transitions must immediately detach editable state, enter `Faulted`, retain available evidence and preserve confirmed historical reads.

Do not fault valid inner commits or key callbacks rejected before any transition.

**Closure/regression test:** Add narrow synthetic tests for the two sequences above, plus failure after an unexpected nesting change. Assert immediate `HistoryFaultError`, no editable overlay, confirmed snapshot readability, and rejection of subsequent begin/navigation. Cover explicit and retained-scope completion. Preserve healthy joined completion, pre-transition key rejection, ordinary rollback and all historical setup/publication cases.

**Classification:** New bounded implementation root, **not a new architectural root**. The existing authority/evidence model can enforce the missing transition checks without redesign.

## 2. Invariant analysis

The following attacks failed to refute their targeted invariants:

- **Historical publication failures:** Post-install exceptions fault even when discard succeeds. Confirmed installed identity remains readable; missing bookkeeping blocks live reads and snapshots.
- **Begin closure:** Backend partial-return, overlay allocation, scope binding and joined setup failures now close cleanly or fault immediately. Abort failures detach overlays and preserve causal errors.
- **Public callback authority:** Equality, truth conversion, diagnostics and repeated manager/backend key comparisons reject public same-manager mutation. Original token, pending value and nesting survive rejected callbacks. Pure custom keys and equal aliases retain healthy behavior.
- **Construction/providers:** Setup and provisional provider reads use private resolved baselines. Unresolved/recursive providers register no partial node. Constructor managed writes reject.
- **Original design callbacks:** Value equality/truth replacement, transient retained-scope completion and idle lazy begin/navigation attacks reject before transactional mutation or target installation; pure retry succeeds.
- **Thaw traversal:** First-thaw results recursively propagate working child handles. Application-backed traversal remains fenced, failed traversal installs no touched target, and retry retains the original edit.
- **Candidate semantics:** Managed reads are frozen through every candidate view. Ordinary/default/working transient reads retain token-local values; current reads retain baseline values. Preview rejection is repairable; final rejection preserves redo.
- **Atomic preparation:** Later-node conversion/validation failures publish nothing. Cleanup retains the previous selection and redo tail.
- **History/topology:** Sparse negative predecessor reads reject; branch preparation trims untouched future fields and presence. Shared aliases, foreign-edge rejection, cycle rejection and provisional/omitted/aborted/future-only availability behave as specified.
- **Absence/snapshots:** Last-visible descendants remain pinned to the fallback frame. Snapshot node frozensets support hashing and alias identity. Retained epochs survive live branch abandonment.
- **Nonversioned data:** Const/plain/binding/local/lazy semantics and transient cleanup remain consistent. Escaped working containers cannot alter committed storage after completion.
- **Generation:** The nine inheritable concepts produce executable AST with matcher-selected constructor, view, lazy, binding and transient behavior. Canonical goldens and generated-base equality pass.

The outstanding gap is completion’s nesting authority, including its healthy-state admission after backend dispatch. No disk persistence, concurrency, collaboration, multikey history, ownership hooks or custom stable adapters were imposed.

## 3. Risks and next action

Direct runtime verification used Python 3.12.12. Recorded supported-version and isolated-wheel evidence was inspected; this report does not independently recertify that matrix.

Converter purity and arbitrary external mutable-object effects remain contractual limits. The finding uses synthetic backend ownership faults to test the explicitly promised failure diagnosis.

The next action is one bounded TDD correction for round 4 P2-1, followed by independent replay of these completion transitions and all retained historical counterexamples at a newly settled tuple.

## Prior-finding closure table

IDs retain their historical round namespaces.

| ID | Disposition claimed | Verified on corrected tree | Status |
| --- | --- | --- | --- |
| State round 1 P2-1 | Healthy discard requires unchanged selection; installed selection requires confirmed publication. | Independently replayed failure after original apply and after selection assignment without bookkeeping. Both fault and block begin/navigation. Known installed value `7` remains readable; unconfirmed reads/snapshots reject. | Closed. |
| State round 1 P2-2 | Candidate pins preserve active transient semantics. | Independently replayed managed value `10` with scratch `-1`. Candidate reads were `(-1, -1, 0, -1)`. Preview and final commit reject; final failure retains value `0`, clears scratch and publishes no frame. Canonical story 16 verifies repair, providers and redo. | Closed. |
| State round 1 P2-3 | Snapshot node equality/hash uses pinned context and node identity. | Independently replayed a child inside managed frozenset. Decoding, cached alias identity, membership and hashing succeed; the retained snapshot survives removal and branch abandonment. | Closed. |
| State round 1 P2-4 | Failed enlist detaches overlays; failed abort faults with causes retained. | Independently replayed enlist failure with abort failure before and after backend closure. Both immediately fault, retain both causes, detach overlays, preserve confirmed old reads and reject later begin/navigation. | Closed. |
| State round 2 P2-1 | Protect complete begin acquisition/allocation/enlistment/binding, including joined setup. | Independently replayed backend return failure, allocation `MemoryError` and final wrapper-binding failure, plus joined return/binding failure. Clean cleanup leaves no token/nesting/overlay; retry publishes exactly one frame. The selected fault matrix also passes abort failures before/after closure. | Closed. |
| State round 3 P2-1 | Fence application-backed key callbacks at manager and backend stages. | Independently replayed the exact original equality rollback/replacement attack. It raises `ReentrantOperationError` before replacement, preserving original token/nesting and pending `7`; pure retry commits that token/value. Repeated equality/truth, wrong-key diagnostics and retained-scope tests pass. | Original public-reentry counterexample closed. Round 4 P2-1 separately identifies insufficient diagnosis of unexpected backend nesting. |

## Changed-range analysis

Comparison against `38662bcbbe7758fb5f980859675fa9efcb41d614` identified:

- `callbacks.py:74–88` adds a backend dispatch fence that permits intended ownership transitions.
- `transaction_yidl.py:70–105` fences manager key hashing, comparison, truth conversion and diagnostics.
- Registration, begin/enlist/binding, setup abort, lookup, stale-scope and completion dispatch now use fenced paths.
- `transaction_yidl.py:534–539` recursively projects thaw output to working views before installation.
- `validate()` now checks mutation authority before invoking key callbacks.
- Canonical stories 19–20, generated goldens and narrow key/thaw-result tests cover the stated dispositions.
- API documentation and implementation/TDD/verification evidence describe these changes. Review material and measurements are outside the runtime object.

These changes follow the cycle 3 dispositions and preserve the accepted API and architecture.

The new depth-only backend fence makes its caller’s transition checks decisive. Begin verifies exact nesting acquisition, but completion’s existing nonterminal shortcut and terminal predicate do not enforce corresponding nesting closure. Round 4 P2-1 is a **bounded completion-ownership implementation defect**, not an architectural failure or a reason to redesign the accepted history model.
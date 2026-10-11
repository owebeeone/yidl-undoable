# YIDL Undoable implementation — STATE-AXIS REVIEW

**Review object:** Complete `yidl_undoable` runtime package, tests, examples, generation resources, README/docs and configuration at `72e1433e1290cc41392223c9d5981847e396f68e`. Local implementation draft; runtime acceptance pending. Implementation diff from `a97e43e5010fd22a9bcd008f27072ca656b73f5b`. Controlling design accepted at `616f2f65473b1240535a6317d8cc79d5cec18414`; implementation plan at `3440ec2fcee3a8d61c1f88cdfbafafc0683edabf`.

**Baseline:**

| Repository | Exact revision |
| --- | --- |
| `yidl_undoable` | `72e1433e1290cc41392223c9d5981847e396f68e` |
| `yidl-lifecycle` | `230362f642d6e9205897698670fe5f87d2c905ce` |
| `yidl` | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| `astichi` | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| `yidl-cache` | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Sources were read from canonical workspace checkouts using read-only inspection. The exact tuple matched at the beginning and end. Git inspection confirmed no working-tree changes to the runtime, tests, examples, public documentation or configuration under review. The design and implementation plan match their controlling revisions.

**Date:** 2026-10-12

**Axis:** In-memory state transitions, backend/token ownership, failure closure, publication ordering, branch abandonment and pinned-state consistency. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: NO-GO** — one P2 finding blocks acceptance. No P0, P1 or P3 findings. All four original State counterexamples are closed, but additional outer-begin failure windows remain unprotected. I pre-commit to GO on a revision that resolves P2-1 as specified.

---

## Prior-finding closure table

The IDs in this table refer to the original State report.

| ID | Disposition claimed | Verified on corrected tree | Status |
| --- | --- | --- | --- |
| State P2-1 | Require unchanged selection for healthy discard; changed selection requires confirmed publication. | Replayed failure immediately after original apply, and after selection assignment without identity bookkeeping. Both raise `HistoryFaultError` and block begin/navigation. Bookkept installed history remains readable; unconfirmed history blocks live reads and snapshots. | Original counterexample closed. |
| State P2-2 | Candidate pins preserve active ordinary/working transient semantics. | Replayed the negative-scratch validator. Ordinary/default/working candidate reads return `-1`; current returns `0`. Preview and final commit reject. Preview remains editable; final failure publishes nothing and clears scratch. Canonical story 16 also verifies redo preservation, repair and provider fences. | Closed. |
| State P2-3 | Snapshot nodes hash and compare by snapshot context and node identity. | Replayed a child inside a managed frozenset. Snapshot reading, membership and hashing succeed; nested mapping/tuple/frozenset aliases resolve to the cached node. Old snapshots remain readable after live branching. | Closed. |
| State P2-4 | Failed enlist always detaches the overlay; failed abort faults immediately with causes preserved. | Replayed enlist failure plus abort failure both before and after backend closure. Both fault immediately, detach the overlay, preserve both causes, retain confirmed old reads and reject later begin/navigation. Also tested failure after actual enlist with successful abort and retry. | Original counterexample closed. The broader failure-safe outer-begin requirement remains open at other setup stages; see new P2-1. |

## Changed-range analysis

Read-only comparison against `a97e43e5010fd22a9bcd008f27072ca656b73f5b` identified these runtime changes:

- `src/yidl_undoable/transaction_yidl.py:253–290` adds failed-enlist abort diagnosis and unconditional overlay detachment. Lines `607–619` restrict healthy discard to unchanged selection.
- `src/yidl_undoable/facades.py:111–127` materializes named lazy constructor providers through the existing generated getter and fenced factory path. Lines `251–255` distinguish candidate pins from historical pins for transient reads.
- `src/yidl_undoable/snapshots.py:32–49` replaces recursive dataclass equality/hash with snapshot-context and node identity.
- `src/yidl_undoable/values.py:92–135` adds recursive built-in set projection, preserving working set identity.
- `src/yidl_undoable/yidl/undoable_core.yidl` supplies an explicit empty constructor boundary; the generated base changes correspond to that resource.
- Canonical stories 13–17, their generated goldens, narrow remediation tests and API documentation cover the stated dispositions.

These changes fit the merged remediation plan. No architecture or public API redesign was introduced.

The additional begin attack reveals that the new cleanup boundary encloses enlistment only. Backend begin, overlay allocation and final scope binding remain outside it. This is a **bounded residual implementation failure**, related to the original begin-safety requirement. It is **not a new architectural root**: the existing abort/evidence mechanism can cover the complete setup operation.

## 0. Evidence base

### Documents and implementation read

Read workspace `AGENTS.md` and `AGENTS_GWZ.md`, the complete canonical State Round 2 prompt, the original State report and merged remediation plan.

Read the controlling checkpoint, design and implementation plan, concentrating on construction, callback ownership, candidate reads, sparse histories, snapshots, publication and failure-state requirements. Read implementation, TDD and independent verification evidence critically, plus README, API/architecture documentation and packaging configuration.

Implementation inspection included:

- `src/yidl_undoable/transaction_yidl.py:1–633`: aggregate callbacks, initialization, candidate preparation, begin/completion, history trimming, reads/writes, navigation and fault diagnosis.
- `src/yidl_undoable/facades.py:1–328`: construction, providers, view identity, lazy/transient materialization and write guards.
- `callbacks.py:1–71`, `values.py:1–135`, `snapshots.py:1–61`, `states.py:1–37`, `history.py:1–61` and `graph.py:1–50`.
- Decorator, harvester, regeneration implementation, nine YIDL resources and canonical harness.
- Canonical construction/callback/validation/container/layer stories and new stories 13–17; diagnostic, history, generation and fault tests.
- In `yidl-lifecycle`, `src/yidl_lifecycle/transaction_yidl.py`, particularly token scope binding, completion ownership and lines `492–632` governing discard, publication, finalization and begin.

The other current-round report was not accessed. No additional agents were spawned.

### Commands and results

From the canonical workspace root, `git -C <member> rev-parse HEAD` verified all five SHAs at start and end. Read-only Git diff/status inspection established the changed ranges and unchanged runtime working tree. Status contained only measurement/review-prompt changes outside the object.

From `yidl_undoable`:

```sh
PYTHONDONTWRITEBYTECODE=1 ../.venv/bin/python -m pytest -q -p no:cacheprovider \
  tests/test_canonical.py tests/test_faults.py \
  tests/test_remediation_faults.py tests/test_remediation_diagnostics.py \
  tests/test_adversarial_diagnostics.py tests/test_state_diagnostics.py \
  tests/test_history.py tests/test_annotation_recognition.py \
  tests/test_definitions.py \
  tests/test_generation.py::test_matcher_selected_executable_surface
```

Result: **54 passed in 5.94s**.

This executes all seventeen canonical stories, including all nine intermediate YIDL layers, and checks their generated goldens. The selected generation test also confirms regenerated base equality.

Additional in-memory probes used:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src ../.venv/bin/python - <<'PY'
# In-memory probe body
PY
```

They independently replayed every original State counterexample, tested adjacent completion failure stages, tested failure after actual enlistment and reproduced new P2-1 at backend-return, overlay-allocation and Undoable scope-binding stages. Injected methods/classes existed only inside probe processes and were restored before subsequent actions.

No file writes, builds, installs, regeneration writes or Git mutations were performed. The resource-copy test was excluded because it writes a temporary directory. Recorded Python-version and installed-wheel checks were inspected, not rerun.

## 1. Findings

### [P2-1] Outer-begin cleanup protects enlistment but leaves other setup failures live

**Location:** `src/yidl_undoable/transaction_yidl.py:246–252` and `291–297`. The exception handler at `253–290` covers only `_backend.enlist`. Backend token creation, overlay allocation and final guarded scope binding lie outside it. The backend installs its token and increments nesting before returning from begin at `yidl-lifecycle/src/yidl_lifecycle/transaction_yidl.py:619–632`.

**Violated invariant:** Design section 11 requires failed begin setup to leave no editable overlay and unexpected ownership/cleanup failures to fault. Sections 3 and 10 require a successful outer scope to complete its owned edit, without an undisclosed begin remaining underneath it.

**Reproduction:** Initialize a generated scalar model at value `0`, then inject failure in either of these framework setup stages:

1. Replace the runtime `EditOverlay` constructor with a callable raising `MemoryError`, then call `h.begin()`.
2. Allow backend scope binding to succeed, but raise from the subsequent Undoable `token.bind_scope` call.

Restore the injected callable after `begin()` raises.

Observed:

| Failure stage | Manager state after failure | Overlay retained | Backend token retained | Nesting |
| --- | --- | --- | --- | --- |
| Overlay allocation | `Idle` | No | Yes | 1 |
| Undoable scope binding | `Editing` | Yes | Yes | 1 |

Then execute:

```python
with h.begin():
    x.value = 9
```

The successful retry joins the token created by the failed begin. Its normal exit completes only the added nesting level:

```text
manager state: Editing
ordinary value: 9
current value: 0
frame count: 1
active token retained: True
backend nesting: 1
```

The scope exits successfully without publishing its edit. The original hidden begin remains active.

A third probe wrapping backend begin to create its token and then raise produced the same `Idle` plus active-token state and retry behavior.

**Impact:** Failed begin can still leave an editable overlay, or leave a hidden backend begin that contaminates subsequent scope ownership. Applications catching a setup failure and retrying can receive successful scope exit while their edits remain uncommitted. Scope-binding failure also admits managed writes immediately after begin has raised.

**Required correction:** Make the complete outer-begin setup one failure-safe operation: backend begin, overlay construction, aggregate enlistment and guarded scope binding. Capture pre-begin ownership before setup. On failure, detach private editable/prepared state and close any newly acquired token where closure can be confirmed. Permit retry only after confirmed clean abort with unchanged selection; otherwise fault immediately, retain available terminal evidence and preserve setup/abort causes. Handle partial backend begin by examining captured versus current ownership rather than relying solely on a returned token.

The correction must also avoid silently retaining an extra nesting level if a joined begin’s setup fails.

**Closure/regression test:** Add narrow synthetic regressions for:

- Backend begin raising after token creation.
- Overlay allocation raising after backend begin.
- Final Undoable scope binding raising after enlistment.
- Abort failure while closing these setup failures.

After confirmed cleanup, assert no active token or editable overlay, and verify that a retried `with h.begin()` publishes exactly one frame and becomes idle. With incomplete cleanup, assert immediate `HistoryFaultError`, preserved causes/evidence, no editable overlay and rejection of begin/navigation. Keep the original successful-abort and failed-enlist regressions green.

**Classification:** Bounded implementation correction; no architectural redesign required.

## 2. Invariant analysis

The following attacks did not refute their targeted invariants:

- **Installed publication:** Original post-install failures now fault. Known installed identity permits diagnostic reads; missing identity bookkeeping blocks live data and snapshots.
- **Unchanged-selection completion:** Failure before selection installation cleanly discards the edit, preserves redo and permits a later successful transaction.
- **Cleanup closure:** Discard failure before cleanup, discard failure after cleanup and after-rollback failure all fault, detach editable state and preserve confirmed old history.
- **Enlist failure:** Failure after actual aggregate registration followed by successful abort remains retryable. Abort failures preserve causal errors and prevent later joins.
- **Candidate semantics:** Managed candidate reads remain frozen through all views without thaw. Transient ordinary/default/working reads retain token-local values; current reads retain baseline values. Preview rejection remains repairable; final rejection preserves redo.
- **Provider fencing:** Constructor dependencies and unresolved/recursive reads, equality/truth attacks, retained transient scope completion and idle lazy begin/navigation attacks execute in canonical stories. Reentry is rejected before transaction replacement or result installation.
- **Graph and history:** Multi-root alias identity, foreign-edge and cycle rejection, provisional/aborted/omitted availability, sparse predecessor lookup and trimming of untouched future histories remain covered by passing executable stories and narrow checks.
- **Absence and snapshots:** Last-visible descendants retain their fallback pin. Snapshot frozensets now support cached node identity and hashing; nested aliases and abandoned-branch snapshots remain readable.
- **Working containers:** Recursive set projection preserves working ownership and ordinary view propagation. Escaped mutable containers cannot alter committed storage after completion.
- **Generation:** All nine inheritable concepts compile executable AST and execute their selected behaviors. Canonical generated-source comparisons and base equality pass.

The remaining broken transition is failed outer-begin setup outside the enlistment handler. No disk durability, concurrency, collaboration, multikey history, ownership-hook or custom-adapter requirements were imposed.

## 3. Risks and next action

This review directly exercised the workspace Python environment. The recorded three-version and installed-wheel gates were inspected but are not independently recertified here.

Trusted converter purity and arbitrary external mutation remain contractual limits. The reported failure concerns the package’s declared handling of unexpected framework setup failures.

The next action is a bounded TDD correction covering the entire begin setup boundary, followed by replay of P2-1 and the original begin/enlist regressions at a newly settled tuple. Runtime acceptance remains blocked until that correction closes.
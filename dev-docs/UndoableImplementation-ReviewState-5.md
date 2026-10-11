# YIDL Undoable implementation — STATE-AXIS REVIEW

**Review object:** Complete `yidl_undoable` runtime package, tests, examples, generation resources, README/docs and configuration at `adcdc3071c00330787c12d05faeb381705215d2d`. Local implementation draft; runtime acceptance pending. Changed-range baseline: `d0f85e6005aefb91098d4164663b07e40c7b757e`. Controlling DRAFT design accepted at `616f2f65473b1240535a6317d8cc79d5cec18414`; implementation plan at `3440ec2fcee3a8d61c1f88cdfbafafc0683edabf`.

**Baseline:**

| Repository | Exact revision |
| --- | --- |
| `yidl_undoable` | `adcdc3071c00330787c12d05faeb381705215d2d` |
| `yidl-lifecycle` | `230362f642d6e9205897698670fe5f87d2c905ce` |
| `yidl` | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| `astichi` | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| `yidl-cache` | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Sources were read from the canonical workspace checkouts using read-only inspection. The exact tuple matched at the beginning and end. Git comparisons showed no working-tree differences in runtime sources, tests, examples, README, public documentation or configuration. The controlling design and implementation plan match their specified revisions.

**Date:** 2026-10-12

**Axis:** In-memory state transitions, completion and callback authority, publication ordering, failure closure, branch abandonment and pinned-state consistency. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: NO-GO** — one P2 finding blocks acceptance. No P0, P1 or P3 findings. All seven historical State original counterexamples are closed, but completion still accepts transitions incompatible with the requested operation. I pre-commit to GO on a revision that resolves round 5 P2-1 as specified.

---

## 0. Evidence base

### Instructions, documents and implementation inspected

Read:

- Workspace `AGENTS.md` and `AGENTS_GWZ.md`.
- The complete canonical `dev-docs/review-prompts/UndoableImplementation-State-Round5.md`.
- All four historical State reports and all four merged remediation plans.
- `dev-docs/CurrentProgramCheckpoint.md`, `dev-docs/UndoableDesign.md` and `dev-docs/UndoableImplementationPlan.md`.
- Implementation, TDD and independent verification evidence, including cycle 4 authority corrections. Recorded passing results were treated as claims requiring examination.
- README, API/architecture documentation, packaging configuration and both examples.

Runtime inspection covered:

- `src/yidl_undoable/transaction_yidl.py:1–780`: aggregate participation, initialization, candidate preparation, begin acquisition/abort, scope callbacks, managed access, navigation and completion diagnosis.
- `callbacks.py:1–98`: captured operation authority, scalar identity checks, application fencing and backend dispatch.
- Complete `facades.py`, `values.py`, `history.py`, `graph.py`, `snapshots.py`, `states.py`, `policies.py`, bindings, candidates, marker adapters, errors and exports.
- Decorator, harvester and regeneration implementation; all nine YIDL resources and matcher-selected contributions.
- Canonical harness, layer-generation story, original constructor/callback stories, historical fault regressions and the new completion-authority tests.
- Pinned Lifecycle token identity and scope binding, keyed dispatch, completion sessions, discard/publication/after-actions and finalization in `yidl-lifecycle/src/yidl_lifecycle/transaction_yidl.py`.

No current-round report from the other axis was accessed. No additional agents were spawned.

### Commands and results

From the canonical workspace root, `git -C <member> rev-parse HEAD` verified all five revisions at start and end.

Read-only Git inspection established:

- The implementation changes since `d0f85e6005aefb91098d4164663b07e40c7b757e`.
- No changes to the controlling design or implementation-plan bytes.
- No working-tree differences in reviewed runtime/public artifacts.
- Only experiment measurement and untracked review-prompt changes outside the runtime object.

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
  tests/test_transaction_key_fences.py tests/test_thaw_result_fences.py \
  tests/test_completion_authority.py
```

Result: **192 passed in 7.85s**.

This executes all twenty canonical stories, compares their generated source with committed goldens, executes all nine intermediate concepts and checks matcher-selected executable behavior.

Read-only Python introspection reported **Python 3.12.12** and:

```python
check_undoable_base() == (True, "")
```

The resource-copy test was excluded because it writes temporary files. Recorded Python 3.13/3.14 and installed-wheel checks were inspected but not independently rerun.

Independent in-memory probes used:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src ../.venv/bin/python - <<'PY'
# In-memory probe body
PY
```

These probes:

- Reconstructed and replayed all seven historical State original counterexamples.
- Replayed round 4’s application-key hidden backend joins at explicit and retained-scope comparison stages.
- Replayed the original design’s constructor/provider, value equality/truth, transient retained-scope/navigation and idle lazy begin/navigation attacks.
- Reproduced four operation-incompatible completion outcomes through both explicit manager calls and token-bound scope callbacks.

Synthetic replacements existed only within probe processes and were restored afterward. No writes, builds, installs, regeneration writes, Git mutations or adjacent-source edits were performed.

## 1. Findings

### [P2-1] Completion validates ownership without validating the requested operation

**Location:** `src/yidl_undoable/transaction_yidl.py:368–399` and `698–769`, particularly the nonterminal acceptance at `730–738` and terminal predicate at `739–767`.

**Violated invariant:** Design sections 3, 10 and 11 distinguish three authorized transitions:

- Inner commit discharges exactly one join and publishes nothing.
- Successful outer commit publishes one frame.
- Rollback closes the entire joined edit without changing published history or redo.

Unexpected backend transitions must fault immediately. Clean terminal evidence establishes what happened; it does not authorize an outcome belonging to a different operation.

Both public completion methods and guarded scope callbacks enter `_complete(callback, token)` without carrying whether completion is commit or rollback. The checker consequently admits:

- Any exact joined decrement as successful nonterminal completion.
- Any otherwise healthy publication or unchanged-selection discard as terminal completion.

It cannot reject a terminal commit from joined depth, a nonterminal rollback, a rollback that publishes, or a successful commit that only discards.

**Reproduction:**

This minimal probe inserts an unexpected decrement before otherwise normal backend commit:

```python
from yidl_undoable import *

@undoable
class Model:
    value: int = managed(default=0)

h = UndoRedoManager()
x = Model(transaction_manager=h)
h.initialize(x)

token = h.begin()
h.begin()
x.value = 7

backend_type = type(h._backend)
original_commit = backend_type.commit

def premature_completion(backend, key):
    backend.begin_count = 1
    return original_commit(backend, key)

backend_type.commit = premature_completion
try:
    result = h.commit()
finally:
    backend_type.commit = original_commit

print(result, x.value, h.frame_count, type(h._state).__name__)
```

Observed:

```text
1 7 2 Idle
```

The caller authorized an inner commit from nesting two. Undoable instead accepts finalized publication, closes both begins and exposes healthy idle state.

Three adjacent probes establish that the omitted operation identity is the common root:

| Requested operation / injected backend outcome | Observed accepted result |
| --- | --- |
| Joined commit; unexpected count drop followed by original commit | Token ID returned; value `7` published; two frames; `Idle`; nesting zero. |
| Joined rollback; replacement rollback calls original backend commit | `None` returned; pending/current values `7 / 0`; one frame; `Editing`; nesting one; no terminal evidence. |
| Outer rollback; replacement rollback calls original backend commit | Token ID returned; value `7` published; two frames; `Idle`; finalized publication evidence. |
| Outer commit; replacement commit calls original backend rollback | Token ID returned; pending value discarded; value `0`; one frame; `Idle`; finalized discard evidence. |

Each sequence was independently reproduced through both explicit manager completion and the retained token’s `_scope_commit` or `_scope_rollback` callback: **eight accepted incompatible outcomes**.

These are narrow synthetic framework faults, matching the historical review’s declared threat model for unexpected backend ownership/completion failures. They require no forged completion record: the original Lifecycle methods produce authentic terminal evidence.

**Impact:** Completion may report success for the wrong state transition. An inner commit can publish prematurely, rollback can leave work active or publish it, and successful outer commit can silently discard work. Publication on rollback can also abandon redo while the manager remains healthy. The declared fail-closed boundary does not diagnose these outcomes.

**Required correction:** Carry the requested completion operation through explicit and guarded token-bound entry points while continuing to delegate to the original Lifecycle callbacks. Validate evidence against that operation and the captured nesting:

- Successful commit from joined depth must be nonterminal, return `None`, decrease nesting exactly once and preserve original token, overlay, state and selection.
- Successful outer commit must confirm publication and its installed selection. Confirmed discard after rejected preparation may remain a healthy closed failure when the original failure is propagated; discard must not masquerade as successful commit.
- Rollback at any depth must be terminal, confirm complete discard and preserve the original selection. Nonterminal decrement or publication cannot satisfy rollback.
- Pre-transition failures remain repairable only with unchanged authority.
- Every incompatible outcome must immediately detach editable/prepared state, enter `Faulted`, retain available evidence and causal failures, and preserve only confirmed historical reads.

Do not attempt to rewind an installed selection merely because its publication was unauthorized.

**Closure/regression test:** Add narrow synthetic regressions for all four rows above through explicit and retained-scope completion. Assert immediate `HistoryFaultError`, detached overlays, retained terminal evidence where present, confirmed old/published snapshot readability as appropriate, and rejection of future begin/navigation.

Retain healthy inner commit, outer commit, rollback at every joined depth, preparation-failure discard, stale exceptional scope handling and unchanged pre-transition key rejection. Independently replay all historical State originals on the corrected tuple.

**Classification:** Bounded residual completion-authority implementation defect. **Not a new architectural root.** The accepted operation-context and terminal-evidence model can enforce the missing distinctions without redesign.

## 2. Invariant analysis

The following attacks failed to refute their targeted invariants:

- **Historical publication diagnosis:** Failure after selection installation faults even when private discard succeeds. Bookkept installed value `7` remains readable. Installation without identity bookkeeping blocks live reads and new snapshots.
- **Begin closure:** Backend begin raising after acquisition, overlay allocation failure and final wrapper-binding failure cleanly close or fault. Independently replayed clean outer/joined setup failures leave no token, nesting or overlay; a retry publishes exactly one frame. Enlist plus abort failure before/after backend closure faults immediately and preserves both causes.
- **Original round 4 nesting attacks:** Hidden begin, changed nesting followed by failure and residual count after finalized publication now fault through explicit and scope completion. Application-key hidden joins at subsequent backend comparison stages also fault.
- **Application callback ownership:** Original key equality rollback/replacement raises `ReentrantOperationError` before replacement, retaining token, nesting and pending `7`; pure retry commits that original edit. Value equality and truth-conversion replacement attacks likewise reject before mutation.
- **Construction and providers:** Setup/provisional named and self providers resolve private baselines through all views. Unresolved construction registers no partial node. Canonical recursion and constructor-write diagnostics pass.
- **Transient and lazy factories:** Retained transient scope completion and navigation reject before mutation or result installation; pure retry succeeds. Fresh idle lazy begin/navigation attacks reject through default/current/working views, leave the target unset and permit one shared cached result on pure retry.
- **Candidate reads:** The original negative-scratch validator observes `(-1, -1, 0, -1)` through ordinary/default/current/working access. Preview and final completion reject; final failure publishes no frame and clears scratch. Managed candidate reads remain frozen and do not thaw.
- **Atomic preparation:** Later-node conversion/validation failures publish no partial history. Preview remains repairable; final rejection closes cleanly and preserves redo.
- **Sparse histories and topology:** Negative predecessor lookup rejects. Branch preparation trims untouched future field and presence histories. Canonical shared roots/aliases, foreign edges, cycles, removed final nodes and provisional/omitted/aborted/future-only availability checks pass.
- **Absence and snapshots:** Last-visible descendants retain their fallback pin. Original child frozenset decoding, nested mapping/tuple aliases, hashing and cached identity succeed. Independently retained snapshots remain readable after live branch removal.
- **Stable/nonversioned values:** Recursive immutable normalization and mapping backing copies protect committed storage. Escaped working containers detach on completion. Const/plain/binding/local/lazy policies and transient cleanup retain their specified behavior.
- **Generation:** Nine inheritable concepts produce executable AST. Matcher-selected constructors, managed views, lazy mutation, bindings and transient factories execute through the canonical harness. Generated goldens and base equality pass.
- **Idle and stale completion:** Ordinary completion without an active token raises the backend’s error while preserving healthy setup/idle state. The new targeted tests reject unauthorized idle acquisition and stale-scope changes to replacement authority.

The remaining gap is operation-specific completion legality. Exact ownership and genuine terminal evidence cannot substitute for checking whether the requested verb permits the observed transition.

No disk persistence, concurrency, collaboration, multikey history, resource ownership hooks or custom stable-adapter requirements were imposed.

## 3. Risks and next action

Direct execution used Python 3.12.12. Supported-version and isolated-wheel evidence was inspected but not independently recertified. Trusted converter purity and arbitrary external mutable-object effects remain contractual limits.

The next action is one bounded TDD correction for round 5 P2-1, followed by independent original-counterexample replay and dual review at a newly settled tuple. Runtime acceptance remains blocked; this review establishes no need for architectural redesign.

## Prior-finding closure table

IDs retain their historical round namespaces.

| ID | Disposition claimed | Verified on corrected tree | Status |
| --- | --- | --- | --- |
| State round 1 P2-1 | Healthy discard requires unchanged selection; installed selection requires confirmed publication. | Independently replayed failure after original apply and after selection assignment without bookkeeping. Both fault and reject begin/navigation. Known installed value `7` remains readable; unconfirmed live reads/snapshots reject. | Closed. |
| State round 1 P2-2 | Candidate pins preserve active transient semantics. | Independently replayed managed value `10` with scratch `-1`. Candidate reads were `(-1, -1, 0, -1)`; preview/final commit reject. Final failure retains value `0`, clears scratch and publishes no frame. | Closed. |
| State round 1 P2-3 | Snapshot node equality/hash uses pinned context and node identity. | Independently replayed a child inside managed frozenset, nested mapping/tuple aliases, cached identity, membership and hashing. Retained snapshot reads survive live branch removal. | Closed. |
| State round 1 P2-4 | Failed enlist detaches overlays; failed abort faults with causes retained. | Independently replayed enlist failure plus abort failure before and after backend closure. Both fault immediately, retain both causal failures, detach the overlay, preserve confirmed old reads and reject later begin. | Closed. |
| State round 2 P2-1 | Protect complete begin acquisition/allocation/enlistment/binding, including joined setup. | Independently replayed backend return failure, allocation `MemoryError`, final wrapper-binding failure and joined return/binding variants. Clean cleanup leaves no token/nesting/overlay; retry publishes exactly one frame. The selected fault matrix also passes abort-before/after and backend-binding cases. | Closed. |
| State round 3 P2-1 | Fence application-backed transaction-key callbacks at manager/backend stages. | Independently replayed the exact equality rollback/replacement attack. Reentry rejects before replacement, retaining original token/nesting and pending `7`; pure retry commits that token/value. Selected equality/truth/repeated-stage diagnostics pass. | Closed. |
| State round 4 P2-1 | Validate exact completion transition and zero terminal nesting. | Independently replayed hidden begin, changed nesting then failure and terminal residual count through explicit/scope completion; all fault. Replayed explicit/backend-key and retained-scope comparison hidden joins; both fault. | Original counterexamples closed. The broader exact-transition requirement remains incomplete for operation-specific outcomes; see round 5 P2-1. |

## Changed-range analysis

Comparison against `d0f85e6005aefb91098d4164663b07e40c7b757e` identified:

- `callbacks.py:8–53` extends captured authority with backend-key identity and exact integer checks for nesting/token IDs.
- `transaction_yidl.py:368–378` checks stale-scope dispatch against unchanged replacement ownership.
- `transaction_yidl.py:673–774` adds shared completion dispatch, selection confirmation and fault handling; captures completion authority; validates joined decrements, token/evidence identity, zero terminal nesting, detached state and terminal return behavior.
- `tests/test_completion_authority.py` adds fifty-five synthetic authority cases.
- `docs/API.md` describes exact inner completion, immediate fault diagnosis and stale-scope preservation.
- Checkpoint, remediation and implementation/TDD/verification records describe the correction. Review material and measurements are outside the runtime object.
- No YIDL resource, generated base, public API, dependency source or accepted-design change occurred.

These changes follow the cycle 4 plan. The added checker closes the historical nesting originals, but its common callback interface omits the requested operation. Its nonterminal and terminal alternatives therefore form a union of legal commit and rollback outcomes.

Round 5 P2-1 is a **bounded residual implementation root in that amended completion boundary**, **not a new architectural root**. The accepted architecture already provides the necessary captured authority and authentic completion evidence; the checker must relate them to the operation requested.
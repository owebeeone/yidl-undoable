# YIDL Undoable implementation — STATE-AXIS REVIEW

**Review object:** Complete `yidl_undoable` runtime package, tests, examples, generation resources, README/docs and configuration at `9d18d60e2244183f3f4715577a1356bf85b517a9`. Local implementation draft; runtime acceptance pending. Changed-range baseline: `adcdc3071c00330787c12d05faeb381705215d2d`. Controlling DRAFT design accepted at `616f2f65473b1240535a6317d8cc79d5cec18414`; implementation plan at `3440ec2fcee3a8d61c1f88cdfbafafc0683edabf`.

**Baseline:**

| Repository | Exact revision verified at start and end |
| --- | --- |
| `yidl_undoable` | `9d18d60e2244183f3f4715577a1356bf85b517a9` |
| `yidl-lifecycle` | `230362f642d6e9205897698670fe5f87d2c905ce` |
| `yidl` | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| `astichi` | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| `yidl-cache` | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Sources were read from the canonical workspace checkouts. Read-only Git comparisons confirmed no working-tree differences in reviewed runtime sources, tests, examples, public documentation or configuration, or inspected dependency sources. The controlling design and implementation-plan bytes match their specified revisions. The exact tuple remained unchanged.

**Date:** 2026-10-12

**Axis:** In-memory state transitions, callback and token authority, publication ordering, failure closure, branch abandonment and pinned-state consistency. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: GO** — no P0, P1, P2 or P3 findings. All eight historical State original counterexamples were independently replayed and closed. No architectural failure was established.

---

## 0. Evidence base

### Instructions and documents inspected

Read:

- Workspace `AGENTS.md` and `AGENTS_GWZ.md`.
- The complete canonical `dev-docs/review-prompts/UndoableImplementation-State-Round6.md`.
- All five historical State reports: `dev-docs/UndoableImplementation-ReviewState.md` and rounds `-2.md` through `-5.md`.
- All five merged plans: `dev-docs/UndoableImplementation-RemPlan.md` and cycles `-2.md` through `-5.md`.
- `dev-docs/CurrentProgramCheckpoint.md`, including the operator’s bounded-remediation authorization and architectural-redesign requirement.
- `dev-docs/UndoableDesign.md` and `dev-docs/UndoableImplementationPlan.md`.
- `dev-docs/ImplementationDraft.md`, `dev-docs/TddEvidence.md` and `dev-docs/VerificationEvidence.md`.
- `README.md`, `docs/API.md`, `docs/Architecture.md`, `pyproject.toml` and both examples.

Recorded red/green, matrix and wheel results were inspected as evidence claims. They were not substituted for original-counterexample replay.

No other current-round prompt or report was read. No additional agents were spawned or consulted.

### Implementation inspected

Locations are relative to the repository owning the file.

In `yidl_undoable`:

- `src/yidl_undoable/transaction_yidl.py:1–810`, including aggregate publication/cleanup, initialization, candidates, complete begin setup/abort, guarded scope callbacks, managed access, navigation and completion diagnosis.
- Complete `callbacks.py`, `facades.py`, `values.py`, `history.py`, `graph.py`, `snapshots.py`, `states.py` and `policies.py`.
- Decorator, harvester, bindings, marker adapter, candidates, errors and public exports.
- Regeneration implementation and all nine YIDL resources, including constructor, field-kind, binding, lazy, transient and managed-view matchers.
- Canonical execution/golden harness and intermediate-layer generation story.
- Constructor/callback, topology, sparse-history, absence/snapshot, nonversioned-policy and atomic-validation stories.
- Historical fault regressions and the amended completion-authority tests.

In pinned `yidl-lifecycle`:

- `src/yidl_lifecycle/transaction_yidl.py`, particularly token identity, scope binding, keyed dispatch, completion ownership, preparation, discard, publication, after-actions and finalization.

### Commands and results

From the canonical workspace root:

```sh
git -C <member> rev-parse HEAD
```

All five revisions matched the baseline table at both review boundaries.

Read-only Git comparisons checked:

- Changes from `adcdc3071c00330787c12d05faeb381705215d2d` to the review object.
- Working-tree equality for reviewed runtime/public artifacts.
- Design equality against `616f2f65473b1240535a6317d8cc79d5cec18414`.
- Implementation-plan equality against `3440ec2fcee3a8d61c1f88cdfbafafc0683edabf`.
- Inspected dependency-source equality against their pinned checkouts.

Status contained an experiment measurement change and untracked round-6 prompts outside the runtime object.

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

Result: **214 passed in 12.38s**.

This executed all twenty canonical stories, compared their actual generated source against committed goldens, executed all nine intermediate concepts and exercised the complete completion-authority suite.

The resource-copy test was excluded because it writes temporary files. No builds, installs, regeneration writes, file edits or Git mutations were performed.

Two independent in-memory probe programs used:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src ../.venv/bin/python - <<'PY'
# In-memory probe body
PY
```

They independently reconstructed and replayed:

- All eight historical State findings.
- Post-install failure with and without identity bookkeeping.
- Negative transient candidate validation, repair and redo preservation.
- Frozenset snapshot nodes, nested aliases and retained epochs.
- Failed enlist plus abort failure before and after closure.
- Partial begin return, overlay allocation and final scope-binding failure, including joined variants.
- The exact custom-key equality rollback/replacement attack.
- Hidden begin, changed nesting followed by failure and finalized residual nesting through explicit and retained scope completion.
- All four round-5 incompatible operation outcomes, plus joined discard, through explicit and retained original callbacks, with successful and exception-after-outcome variants.
- Healthy commit and rollback at depths one, two and four.
- Original constructor-provider, unresolved-read, value equality/truth, transient retained-scope/navigation and idle lazy begin/navigation counterexamples.
- Later-stage custom-key hidden joins.
- Repairable pre-transition failures.
- Genuine preparation rejection and improperly suppressed preparation failure.

Synthetic replacements existed only within their Python processes and were restored afterward. Both probe programs completed successfully.

Read-only introspection reported:

```text
Python: 3.12.12
check_undoable_base(): (True, "")
```

## 2. Invariant analysis

### Operation-specific completion legality

The amended call graph preserves the original Lifecycle scope callbacks and carries the requested verb through both explicit and token-bound entry points:

- Scope binding supplies `"commit"` or `"rollback"` at `transaction_yidl.py:273–283`.
- Guarded scope dispatch forwards the operation at `372–382`.
- Explicit manager completion supplies it at `391–407`.
- `_completion_outcome_intact` evaluates terminal evidence against operation and captured nesting at `703–719`.
- `_complete` restricts nonterminal admission and checks terminal authority at `730–804`.

The independently replayed incompatible outcomes now diagnose faults immediately:

| Requested operation | Injected authentic backend outcome | Corrected result |
| --- | --- | --- |
| Joined commit | Premature terminal publication | `HistoryFaultError`; detached overlay; actual installed value remains confirmed and readable. |
| Joined rollback | Nonterminal inner commit | `HistoryFaultError`; detached overlay; old selection remains confirmed. |
| Outer rollback | Terminal publication | `HistoryFaultError`; actual publication retained; subsequent mutation/navigation rejected. |
| Outer commit | Clean terminal discard | `HistoryFaultError`; old selection retained; discard cannot masquerade as successful commit. |
| Joined commit | Terminal discard | `HistoryFaultError`; old selection retained. |

Each row was exercised through explicit manager completion and a scope callback retained before additional joins. Exceptions raised after the incompatible outcome did not authorize it. Causal exceptions and available terminal evidence were retained.

Healthy retained callbacks at depths one, two and four behaved correctly. Only joined commit returned `None` and discharged exactly one join. Outer commit published one frame and returned the original token ID. Rollback at every tested depth closed the whole edit without publication.

A genuine freeze rejection propagated its original `ValueError`, closed through complete discard, preserved selection and redo, and left the manager healthy. Suppressing that recorded failure and returning a success token caused `HistoryFaultError`. An authentic backend publication flag without selection installation is rejected by the selected authority regressions.

### Ownership, diagnosis and failure closure

The original custom-key equality attack rejected public rollback/replacement before mutation. The original token, nesting and pending value `7` remained intact; a pure retry committed that edit.

Later-stage key comparisons that inserted a hidden backend join faulted through explicit and retained scope completion. Hidden begin, changed nesting followed by failure and residual count after finalized publication also faulted immediately.

Independent pre-transition failure probes retained the exact token, overlay, state, selection and nesting through both completion entry points. These failures remained repairable. The selected tests additionally reject token/evidence identity changes, backend-key changes, scalar protocol traps, idle token acquisition and stale-scope changes to replacement work.

The diagnosed-fault persistence test confirms that otherwise successful backend cleanup cannot revive a manager after callback ownership loss.

Whole-begin setup encloses acquisition, allocation, enlistment and guarded binding. Replayed clean failures left no active token, nesting or overlay; a retried scope published exactly one frame and became idle. Failed abort before or after closure faulted immediately, detached the overlay and retained setup/abort causes.

### Publication and candidate semantics

Failure immediately after original apply faults even when discard succeeds. Bookkept installed value `7` remains readable through confirmed live data and snapshots. Selection assignment without bookkeeping blocks new live managed reads and snapshots; independently pinned old snapshots remain readable.

Candidate managed reads use the frozen candidate and do not thaw. The original negative-scratch validator observed:

```text
ordinary/default/current/working: (-1, -1, 0, -1)
```

Preview rejected while leaving the edit repairable. Final rejection published nothing, preserved redo and cleared transient state. Positive repair succeeded and completion cleared the overlay.

Later-node freeze/validation failures and validator reentry publish no partial candidate. Initialization failure remains setup and retryable. Preview does not consume a frame ID; final rejected preparation may consume an ID without exposing a frame.

### Original design callback counterexamples

Independent reconstruction confirmed:

- Named and self constructor providers read private baselines through all views in setup and provisional construction.
- Unresolved construction fails contextually without partial registration.
- Value equality and truth-conversion rollback/replacement attempts reject before mutation and retain the original edit.
- Transient provider navigation and retained-scope completion reject before target installation; pure retry succeeds.
- Fresh idle lazy begin/undo/redo attempts reject through default/current/working views, preserve selection and leave the target unset. Pure retry creates one shared cached result.

Canonical recursion, constructor-write, converter, validator, application-backed mapping and thaw-result traversal checks also passed.

### Full prior invariant coverage

The following accepted-design groups remained covered by inspected runtime paths and passing executable generation stories:

| Invariant group | Evidence and result |
| --- | --- |
| Initial publication and generated declarations | Scalar/collection frame zero, initialization retry and deterministic generated-source checks held. |
| Transaction-only managed mutation | Idle/current writes reject; ordinary/working views expose pending data; rollback restores committed data. |
| Multiple roots and shared topology | Shared children retain identity; add/remove/move relationships and empty final roots work. Working membership is recomputed from escaped containers. |
| Joined and stale scopes | Inner commit is nonpublishing; rollback closes all joins; stale normal completion rejects and stale exceptional exit preserves the body exception and replacement edit. |
| Sparse versions and identities | Negative predecessor lookup rejects; equal-valued touches and empty edits create the specified frames; cursor, frame and token roles remain distinct. |
| Navigation and branch abandonment | Editing rejects navigation; branching trims every future field and presence history, including untouched fields. |
| Atomic conversion/validation | Later-node failure publishes nothing; preview is repairable; final rejection closes and preserves redo. |
| Views and absence | Ordinary/current/working child modes propagate; strict absence rejects; last-visible descendants remain pinned read-only to the fallback frame. |
| Provisional and unavailable nodes | Provisional editing precedes attachment; removed final nodes do not publish touched data; omitted, aborted and future-only nodes cannot be resurrected. Foreign edges and final cycles reject. |
| Recursive stable values | Immutable backing copies protect storage; invalid values, node mapping keys and cycles reject. Working container references detach on completion. |
| Snapshots | Nested aliases resolve within one pinned context; frozenset hashing and membership work; old epochs survive live branching; absent/nonmanaged/unknown access rejects. |
| Nonversioned policies and inheritance | Const reference, plain, binding, local, lazy, initvar/classvar and transient cleanup semantics hold; compatible single inheritance preserves field identity and unsupported declarations fail contextually. |

### Executable generation and packaging evidence

The nine-layer chain is implemented through inheritable YIDL concepts, typed collections, contributions, ordered phases and matchers. The decorator compiles executable AST from that assembly. Runtime helpers provide shared mechanics; matcher selection determines generated constructor/property behavior.

The canonical layer story independently compiled and executed each concept. Twenty canonical source comparisons and the generated-base equality check passed. Annotation-recognition tests passed on the directly exercised interpreter.

Packaging configuration includes the source package and its YIDL resources. Independent recorded evidence reports rebuilt isolated-wheel checks and full suites on Python 3.12.12, 3.13.12 and 3.14.3. This review inspected that evidence but independently executed only Python 3.12.12.

No disk persistence, concurrency, collaboration, multikey atomic history, resource ownership hooks, arbitrary stable adapters, public registry release or multiple generated-base inheritance requirement was imposed.

## 3. Risks and next action

Supported-version and installed-wheel evidence was inspected, not independently recertified. Trusted converter purity, external mutable-object effects and the declared serialized in-memory scope remain contractual limits.

The single next action is to file this State GO against the exact tuple and apply the required dual-review acceptance gate. This report establishes neither a release nor acceptance of later runtime bytes.

## Prior-finding closure table

Historical IDs retain their round namespaces. “Verified” below means the original counterexample was independently reconstructed and replayed on this tuple.

| ID | Disposition claimed | Verified on corrected tree | Status |
| --- | --- | --- | --- |
| State round 1 P2-1 | Healthy discard requires unchanged selection; installed selection requires confirmed publication. | Replayed original apply-then-raise and assignment-before-bookkeeping variants. Both fault and reject future mutation/navigation. Confirmed installed data remains readable; unconfirmed live reads/new snapshots reject. | Closed. |
| State round 1 P2-2 | Candidate pins preserve active transient semantics. | Replayed managed `10`, scratch `-1`; observed `(-1, -1, 0, -1)`. Preview/final rejection, redo preservation, positive repair and completion cleanup held. | Closed. |
| State round 1 P2-3 | Snapshot node hash/equality uses pinned context and node identity. | Replayed child frozenset decoding, membership/hash, nested mapping/tuple/frozenset aliases and retained snapshots after branch removal. | Closed. |
| State round 1 P2-4 | Failed enlist detaches overlays; failed abort faults with causes retained. | Replayed enlist failure plus abort failure before and after closure. Both immediately fault, preserve both causal failures and confirmed old reads, detach overlays and reject later begin/navigation. | Closed. |
| State round 2 P2-1 | Protect complete begin acquisition/allocation/enlistment/binding, including joined setup. | Replayed partial backend return, allocation `MemoryError`, final binding failure and joined return/binding failures. Clean closure leaves no token/count/overlay; retry publishes exactly one frame. Selected tests cover abort failures across setup stages. | Closed. |
| State round 3 P2-1 | Fence application-backed key callbacks at manager/backend stages. | Replayed exact equality rollback/replacement attack. Reentry rejects before replacement; original token, nesting and pending `7` survive; pure retry commits that original edit. Equality/truth/repeated-stage diagnostics also pass. | Closed. |
| State round 4 P2-1 | Validate exact completion transition and zero terminal nesting. | Replayed hidden begin, changed nesting with failure and residual terminal count through explicit/retained completion. Replayed later-key hidden joins. All immediately fault; confirmed historical reads survive and future mutation/navigation rejects. | Closed. |
| State round 5 P2-1 | Validate observed completion against requested operation and original nesting. | Replayed all four original rows through explicit and retained original scope callbacks, with success/failure variants. Joined discard also faults. Healthy joined/outer completion and propagated preparation rejection remain valid. | Closed. |

## Changed-range analysis

Comparison against `adcdc3071c00330787c12d05faeb381705215d2d` identified these runtime-facing changes:

- `src/yidl_undoable/transaction_yidl.py:273–283`, `372–407` and `730–804` carry the requested completion operation through manager and original token-bound callbacks.
- `transaction_yidl.py:687–719` separates selection confirmation from operation legality and adds the operation-specific terminal predicate.
- `tests/test_completion_authority.py:305–378` adds twenty-two cases covering incompatible outcomes, exception-after-outcome variants, joined discard and publication without actual installation.
- `docs/API.md` documents inner commit, outer publication, propagated preparation-failure discard and rollback-at-any-depth requirements.
- Checkpoint, implementation/TDD/verification records and historical review/remediation material record the correction. Review prompts, reports and measurements are outside the runtime object.

No accepted-design, public API, dependency source, YIDL resource, generated base or canonical golden change occurred.

The amended signature and predicate directly implement the cycle-5 disposition. Independent replay found no new root-cause candidate. The historical completion defects remain classified as bounded implementation defects; this correction establishes no architectural failure or redesign requirement.

Final tuple verification again matched all five baseline revisions exactly.
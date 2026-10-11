# YIDL Undoable implementation — STATE-AXIS REVIEW

**Review object:** Complete `yidl_undoable` runtime package, tests, examples, generation resources, README/docs and configuration at `a97e43e5010fd22a9bcd008f27072ca656b73f5b`. Local implementation draft; runtime acceptance pending. Controlling design accepted at `616f2f65473b1240535a6317d8cc79d5cec18414`; implementation baseline `3440ec2fcee3a8d61c1f88cdfbafafc0683edabf`.

**Baseline:**

| Repository | Exact revision |
| --- | --- |
| `yidl_undoable` | `a97e43e5010fd22a9bcd008f27072ca656b73f5b` |
| `yidl-lifecycle` | `230362f642d6e9205897698670fe5f87d2c905ce` |
| `yidl` | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| `astichi` | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| `yidl-cache` | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Sources were read from the canonical workspace checkouts using `cat`, `nl`, `sed` and `rg`, with Git inspection establishing the pinned revisions and implementation diff. The tuple matched at the beginning and end of review. The design and implementation-plan files have no differences from their respective controlling revisions.

**Date:** 2026-10-12

**Axis:** State machines, in-memory publication ordering, callback/token ownership, failure closure, branch abandonment and pinned-state consistency. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: NO-GO** — four P2 findings block acceptance. No P0, P1 or P3 findings. I pre-commit to GO on a revision that resolves P2-1, P2-2, P2-3 and P2-4 as specified.

---

## 0. Evidence base

### Controlling instructions and documents

Read:

- Workspace `AGENTS.md` and `AGENTS_GWZ.md`.
- The complete canonical `dev-docs/review-prompts/UndoableImplementation-State-Round1.md`.
- `dev-docs/CurrentProgramCheckpoint.md`, including autonomous scope, runtime acceptance and bounded remediation authority.
- `dev-docs/UndoableDesign.md`, particularly sections 4–11 on field semantics, construction, graph membership, callback ownership, sparse storage, snapshots, publication and failures; sections 12–13 on generation and verification.
- `dev-docs/UndoableImplementationPlan.md`.
- `dev-docs/ImplementationDraft.md`, `dev-docs/TddEvidence.md` and `dev-docs/VerificationEvidence.md`. Their claims were treated as evidence to inspect, not acceptance proof.
- `README.md`, `docs/API.md`, `docs/Architecture.md`, both examples and `pyproject.toml`.

The other current-round review prompt/report was not read. No other agent was consulted or spawned.

### Implementation inspected

All locations below are relative to the repository owning the file.

In `yidl_undoable`:

- `src/yidl_undoable/transaction_yidl.py:1–596`: aggregate participation, initialization, candidate freezing/validation, begin/completion, branch preparation, live reads/writes, navigation and fault diagnosis.
- `src/yidl_undoable/facades.py:1–306`: constructor providers, view propagation, lazy/transient materialization and write guards.
- `src/yidl_undoable/callbacks.py:1–71`: captured operation context and callback fencing.
- `src/yidl_undoable/values.py:1–127`, `graph.py:1–50`, `history.py:1–61`, `snapshots.py:1–45`, `policies.py:1–30`, `candidates.py:1–8` and `states.py:1–37`.
- `undoable.py`, `undoable_harvester.py`, marker exports, public errors and binding adapters.
- The nine YIDL resources, generated-base assembly/matcher structure and `regenerate_undoable_base.py`.
- All twelve canonical source stories, the canonical execution/golden harness, and targeted diagnostic/fault/generation tests.

In `yidl-lifecycle`:

- `src/yidl_lifecycle/transaction_yidl.py`, especially completion ownership checks and lines 492–592 governing discard, publication, after-actions and terminal evidence.

### Commands and results

From the canonical workspace root, `git -C <member> rev-parse HEAD` verified every SHA in the baseline table at start and end. Read-only Git diff/status inspection confirmed the runtime sources used were unchanged. Status showed an experiment measurement change and untracked review prompts, which are explicitly outside the review object.

From `yidl_undoable`:

```sh
PYTHONDONTWRITEBYTECODE=1 ../.venv/bin/python -m pytest -q -p no:cacheprovider \
  tests/test_canonical.py tests/test_faults.py \
  tests/test_adversarial_diagnostics.py tests/test_state_diagnostics.py \
  tests/test_history.py
```

Result: **24 passed in 4.91s**.

```sh
PYTHONDONTWRITEBYTECODE=1 ../.venv/bin/python -m pytest -q -p no:cacheprovider \
  tests/test_annotation_recognition.py tests/test_definitions.py \
  tests/test_generation.py::test_matcher_selected_executable_surface
```

Result: **19 passed in 1.21s**.

Read-only Python introspection reported **Python 3.12.12** and:

```python
check_undoable_base() == (True, "")
```

The resource-copy test was not run because it writes a temporary directory. No builds, installs, regeneration writes, file edits or Git mutations were performed.

Additional in-memory probes used:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src ../.venv/bin/python - <<'PY'
# Probe body
PY
```

They reproduced all four findings below. Synthetic fault injection modified only objects/classes within the probe process; backend class methods were restored before continuing.

The existing tests passed, but they do not cover these four counterexamples.

## 1. Findings

### [P2-1] Successful discard evidence masks an incomplete publication after history changed

**Location:** `src/yidl_undoable/transaction_yidl.py:568–589`, particularly the healthy-state predicate at line 578. Publication occurs at lines 50–54.

**Violated invariant:** Design section 11 requires unexpected publication/cleanup failures to enter faulted state when terminal evidence does not confirm a clean outcome. Discarding private overlays must never be interpreted as restoring history after publication. Section 10 explicitly says rollback cleanup never rewinds an installed selection.

**Reproduction:**

1. Initialize a model with managed value `0`.
2. Begin an edit and assign `7`.
3. Wrap the aggregate’s apply callback to invoke the original callback, then raise:

```python
original_apply = h._aggregate._apply_prepared_commit_tx_by_key

def fail_after_publication(key, token_id):
    original_apply(key, token_id)
    raise RuntimeError("failure immediately after publication")

h._aggregate._apply_prepared_commit_tx_by_key = fail_after_publication
h.commit()
```

Observed:

- `commit()` raised the injected `RuntimeError`, rather than `HistoryFaultError`.
- Terminal evidence had:
  - `publication_started=True`
  - `publication_complete=False`
  - `discard_complete=True`
  - `after_actions_complete=True`
  - `ownership_preserved=True`
  - `finalized=True`
- The value was nevertheless published as `7`; frame count increased to two.
- The manager returned to `Idle`.
- A subsequent `begin()` succeeded.

The backend correctly classifies the raising apply callback as incomplete publication, then successfully discards private state. Undoable accepts that discard evidence independently of whether the selected history changed.

**Impact:** An internal publication failure leaves the manager accepting further edits despite an outcome its completion evidence does not certify. A failed commit can already have changed history or abandoned redo, while the coordinator exposes healthy-idle behavior. This violates the declared fail-closed state machine.

**Required correction:** Correlate completion evidence with selection identity. A clean discard outcome must require preservation of the pre-completion selection. An installed new selection requires confirmed publication evidence; incomplete publication must fault even when private discard succeeds. Preserve the installed selection for confirmed diagnostic/snapshot reads when its identity is known.

**Closure/regression test:** Add a narrow synthetic fault test for failure immediately after installation. Assert `HistoryFaultError`, retained terminal evidence, confirmed published value where appropriate, and rejection of begin/navigation. Also test failure between the publication assignment and its internal identity bookkeeping; unconfirmed live reads/snapshots must fail closed. Existing prepare-failure and ordinary rollback tests must remain healthy and preserve redo.

### [P2-2] Candidate pins suppress active transient values during validators

**Location:** `src/yidl_undoable/facades.py:227–233`, particularly the unconditional `_u_pin is not None` baseline branch. Candidate validators receive pinned facades from `transaction_yidl.py:221–230`.

**Violated invariant:** Design section 10 specifies frozen-candidate semantics for **managed** reads while nonversioned fields retain their ordinary semantics. Section 4 defines active ordinary/working transient reads as token-local values; current reads retain the construction baseline.

**Reproduction:**

```python
@undoable
class Model:
    value: int = managed(default=0)
    scratch: int = transient(default=0)

    @validate_commit(DEFAULT_TRANSACTION)
    def reject_negative_scratch(self):
        return self.scratch >= 0

h = UndoRedoManager()
x = Model(transaction_manager=h)
h.initialize(x)
h.begin()
x.value = 10
x.scratch = -1
h.commit()
```

Before completion, live reads were:

```text
ordinary scratch: -1
current scratch:   0
working scratch:  -1
```

An observational version of the validator recorded `(0, 0, 0, 0)` through its ordinary/default/current/working facades. Commit succeeded and published managed value `10`.

The candidate’s pin freezes managed access correctly, but the transient accessor treats that pin as a historical fallback and bypasses the active overlay.

**Impact:** Validators can accept a transaction they should reject, or reject one whose actual transient input is valid. They cannot reliably use transaction-local scratch/provider data under the promised field semantics.

**Required correction:** Distinguish candidate pins from historical fallback pins in transient reads. During candidate validation, ordinary/default/working transient access must retain active-token behavior; current access must retain baseline behavior. Preserve write fencing and historical fallback behavior.

**Closure/regression test:** Add a canonical generated story where a validator reads an explicitly assigned transient value through default/working access and rejects it. Assert preview failure leaves the edit repairable, commit failure publishes nothing and preserves redo, and successful repair clears the transient overlay on completion. Include a working transient factory/provider read during validation and confirm callback fencing still rejects completion or managed writes.

### [P2-3] Snapshot nodes cannot participate in supported frozenset values

**Location:** `src/yidl_undoable/snapshots.py:32–35`, where the frozen dataclass implicitly generates a structural hash; `src/yidl_undoable/values.py:77–78`, where decoding reconstructs frozensets.

**Violated invariant:** Design sections 6–7 admit recursively stable frozensets containing managed node references. Section 9 requires nested snapshot values to resolve to snapshot nodes in the same pinned graph.

**Reproduction:**

```python
@undoable
class Node:
    value: int = managed(default=0)
    children: frozenset = managed(default=frozenset())

h = UndoRedoManager()
child = Node(transaction_manager=h)
root = Node(children=frozenset((child,)), transaction_manager=h)
h.initialize(root)

assert len(root.children) == 1
h.snapshot().node(root.node_id).get("children")
```

Initialization and live reads succeeded. The snapshot read raised:

```text
TypeError: unhashable type: 'dict'
```

Constructing the decoded frozenset hashes its `SnapshotNode`. The generated hash recursively hashes its `FrameSnapshot` and epoch/schema records, eventually reaching an unhashable mapping/dictionary.

**Impact:** A valid committed graph cannot be read through snapshots for this supported container shape. This also limits snapshot-based recovery from confirmed history.

**Required correction:** Give snapshot nodes a stable identity equality/hash contract that does not recursively hash graph records or mutable caches. Preserve alias identity within the pinned snapshot and distinguish nodes from incompatible pinned contexts.

**Closure/regression test:** Add a canonical generated story with a node reference inside a frozenset, including a nested tuple/mapping combination. Assert snapshot reads succeed, aliases resolve to the cached snapshot node, membership/hash operations work, and the snapshot remains readable after live branch truncation.

### [P2-4] Failed begin cleanup leaves an unenlisted overlay available for later joins

**Location:** `src/yidl_undoable/transaction_yidl.py:247–256`. The edit is installed before enlistment; cleanup of that edit occurs only after backend rollback returns successfully.

**Violated invariant:** Design section 11 requires failed begin setup to leave no editable overlay, and unexpected ownership/cleanup failures to fault. Section 10 requires exactly one aggregate participant for every outer edit.

**Reproduction:**

1. Initialize a model with managed value `0`.
2. Inject an enlistment failure and a rollback failure into the backend class.
3. Call `begin()`.
4. Restore both backend methods.

Observed immediately afterward:

```text
begin error: RuntimeError("synthetic abort failure")
manager state: Idle
edit overlay retained: True
backend active token retained: True
```

Calling `begin()` again joined that token instead of enlisting the aggregate. It changed the state to `Editing`, raised nesting to two, and accepted `x.value = 9`.

The first commit returned `None`. The outer commit eventually raised `HistoryFaultError`; the value returned to `0` because no aggregate participant had published it.

**Impact:** A failed begin creates an illegal intermediate state: an overlay and token exist without their required participant, yet a subsequent public begin admits managed writes. The failure is diagnosed only after additional work is accepted and then lost.

**Required correction:** Handle begin setup and abort cleanup as a failure-safe operation. Always detach the private overlay on failed setup. If abort/ownership closure cannot be confirmed, retain available terminal evidence, enter `Faulted`, and raise `HistoryFaultError` with the enlistment/cleanup failures preserved. Never permit later begin to join an unenlisted failed token.

**Closure/regression test:** Extend the narrow enlistment fault coverage with rollback failure before closure and rollback failure after closure. Assert no retained editable overlay, immediate fault diagnosis where cleanup evidence is incomplete, confirmed old snapshot readability, and rejection of subsequent begin/navigation. Keep the existing successful-abort enlistment-failure case retryable.

## 2. Invariant analysis

The following attacks failed to refute their targeted invariants:

- **Transaction-only managed mutation:** Canonical explicit and scope transactions reject idle/current writes, expose pending values only through ordinary/working views, and restore committed values after rollback.
- **Joined token authority:** Nested begin returns the existing token; inner commit publishes nothing; inner rollback closes the whole joined edit. Stale normal exits cannot commit replacement tokens, and stale exceptional exits preserve the original exception.
- **Construction context:** Setup/provisional named dependencies and opt-in self factories read private resolved baselines through all three views. Unresolved/recursive providers fail contextually, constructor writes are fenced, and failed construction does not register a partial node.
- **Original callback counterexamples:** Equality and truth-conversion attempts to rollback/replace transactions are fenced. Transient provider attempts to complete a retained scope are fenced. Idle lazy attempts to begin/navigate leave the target unset and permit a pure retry.
- **Operation ownership:** Captured selection, state, overlay, token, nesting and key identity are checked after callbacks. The existing private-backend replacement probe rejects result installation and faults.
- **Atomic preparation:** Later-node freeze/validation failure does not publish earlier values. Failed final preparation closes the edit and preserves redo. Failed preview remains repairable. These successful checks do not cover P2-1’s failure after installation.
- **Sparse histories and branching:** Negative predecessor indexes raise instead of selecting the last value. Branch preparation trims untouched future field histories and presence histories. Equal-valued touches and empty edits produce frames as specified.
- **Topology:** Multi-root aliases preserve node identity; membership is recomputed from working containers. Foreign edges and final managed cycles fail. Removed final nodes do not publish touched data. Omitted, aborted and abandoned future-only nodes cannot be resurrected.
- **Absence:** Strict absence rejects managed reads. Last-visible resolution uses surviving prior presence and pins descendants to the fallback frame, preventing a historical-parent/live-child mixture.
- **Stable values:** Stored containers are normalized recursively; immutable mapping wrappers receive private backing copies. Invalid outputs, mapping node keys and container cycles fail. Escaped working lists are detached after completion.
- **Snapshots:** Tuple/mapping aliases and old epochs survive branch truncation; nonmanaged/unknown fields and absent nodes are rejected. P2-3 exposes an uncovered supported frozenset shape.
- **Nonversioned policies:** Const reference behavior, plain/binding/local storage, lazy caching and transient completion cleanup passed their canonical scenarios. P2-2 isolates the candidate-validator transient exception.
- **Generation:** The canonical layer story compiled all nine concepts and executed their AST-built models. Matcher checks selected constructor forms, managed view access, mutable lazy access and transient factory paths. Generated-base regeneration matched committed bytes.

The current completion and begin predicates therefore do not yet form the closed legal-state grammar claimed by the design. P2-1 and P2-4 identify distinct transitions that admit healthy/editable behavior without sufficient completion or participant evidence.

No disk durability, crash recovery, concurrency, collaboration, ownership hooks, custom stable adapters or multikey history requirements were imposed.

## 3. Risks and next action

Direct runtime verification in this review used Python 3.12.12. The recorded independent Python 3.13/3.14 and installed-wheel checks were inspected but not rerun; no new version-matrix or packaging certification is claimed.

Trusted converter purity and arbitrary external mutation remain explicit contractual limits. They are not additional findings. The fault probes concern the package’s declared handling of unexpected internal ownership/publication/cleanup failures.

The next action is one bounded remediation revision addressing all four findings with failing regressions first, followed by originating State counterexample closure at a newly pinned tuple. These findings do not establish a need for architectural redesign.
# YIDL Undoable implementation — CODE + SURFACE-AXIS REVIEW

**Review object:** Complete `yidl_undoable` runtime package, tests, examples, generation resources, documentation and configuration at `adcdc3071c00330787c12d05faeb381705215d2d`; local implementation draft, runtime acceptance pending. Controlling design: `dev-docs/UndoableDesign.md`, accepted at `616f2f65473b1240535a6317d8cc79d5cec18414`.

**Baseline:**

| Repository | Pinned revision |
| --- | --- |
| `yidl_undoable` | `adcdc3071c00330787c12d05faeb381705215d2d` |
| `yidl-lifecycle` | `230362f642d6e9205897698670fe5f87d2c905ce` |
| `yidl` | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| `astichi` | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| `yidl-cache` | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Sources were read from the working tree. Read-only Git comparisons confirmed the reviewed runtime, tests, public documentation, examples, configuration and controlling documents match `HEAD`. The design matches its accepted revision; the implementation plan matches `3440ec2fcee3a8d61c1f88cdfbafafc0683edabf`. Correction comparison: `d0f85e6005aefb91098d4164663b07e40c7b757e..adcdc3071c00330787c12d05faeb381705215d2d`. The complete tuple was verified at review start and end and did not move.

**Date:** 2026-10-12

**Axis:** Code architecture, interfaces, call graphs, composition and compatibility, plus the cold Python API surface. Independent, adversarial, read-only replacement review under Step 5.5. The other axis runs in parallel; nothing here relies on its current-round report. Filed verbatim by the lane owner.

**Verdict: GO** — no P0, P1, P2 or P3 findings established. All six historical Code findings were independently replayed and are closed on this exact tuple.

---

## 0. Evidence base

The cold reading order was `README.md`, `docs/API.md`, then `examples/first_use.py` and `examples/nested.py`, before design, implementation source or historical reports.

Subsequent inspection covered:

- Workspace `AGENTS.md` and `AGENTS_GWZ.md`, and the complete canonical `dev-docs/review-prompts/UndoableImplementation-Code-Round5.md`.
- Controlling `dev-docs/CurrentProgramCheckpoint.md`, `UndoableDesign.md` and `UndoableImplementationPlan.md`.
- All four historical same-axis reports: `UndoableImplementation-ReviewCode.md`, `UndoableImplementation-ReviewCode-2.md`, `UndoableImplementation-ReviewCode-3.md` and `UndoableImplementation-ReviewCode-4.md`.
- All four merged remediation plans: `UndoableImplementation-RemPlan.md` through `UndoableImplementation-RemPlan-4.md`.
- `docs/Architecture.md`, package exports, exact Lifecycle marker re-exports, `pyproject.toml` and the regeneration interface.
- Complete runtime construction/provider mechanics in `facades.py`; manager and aggregate implementation in `transaction_yidl.py:1–780`; callback authority in `callbacks.py`; stable normalization/projection in `values.py`; and history, graph, absence policy, snapshot, binding, candidate, state and error support.
- Declaration recognition, inheritance adaptation and executable AST assembly in `undoable_harvester.py` and `undoable.py`.
- All nine owning YIDL resources, their matcher-selected contributions and phase dependencies.
- All twenty canonical scenario sources and their executed generated-source comparisons. Narrow diagnostic and synthetic-fault coverage was executed as listed below; the changed completion-authority tests and callback/key/projection tests were also inspected.
- Pinned Lifecycle transaction identity, scope binding, stale callbacks, group begin/completion, participant cleanup and terminal evidence in `src/yidl_lifecycle/transaction_yidl.py:72–782`.
- `ImplementationDraft.md`, `TddEvidence.md` and `VerificationEvidence.md`. Their test, matrix and wheel claims were inspected critically and were not treated as acceptance proof.

Commands and observed results:

1. From the canonical workspace root, `git -C <member> rev-parse HEAD` for each of the five members at both ends: all matched the pinned tuple.
2. Read-only correction diff, statistics and commit history: production changes are confined to `callbacks.py`, `transaction_yidl.py` and six added API-documentation lines.
3. `git diff --exit-code HEAD -- src tests docs examples README.md pyproject.toml dev-docs/UndoableDesign.md dev-docs/UndoableImplementationPlan.md`: exit 0.
4. Design comparison with `616f2f6` and implementation-plan comparison with `3440ec2`: exit 0.
5. From `yidl_undoable`:

   ```sh
   PYTHONDONTWRITEBYTECODE=1 ../.venv/bin/python -m pytest -q -p no:cacheprovider \
     tests/test_canonical.py \
     tests/test_definitions.py \
     tests/test_annotation_recognition.py \
     tests/test_history.py \
     tests/test_faults.py \
     tests/test_state_diagnostics.py \
     tests/test_adversarial_diagnostics.py \
     tests/test_remediation_diagnostics.py \
     tests/test_remediation_faults.py \
     tests/test_begin_setup_faults.py \
     tests/test_provisional_fences.py \
     tests/test_thaw_result_fences.py \
     tests/test_transaction_key_fences.py \
     tests/test_completion_authority.py \
     tests/test_generation.py::test_matcher_selected_executable_surface
   ```

   Result: **192 passed in 7.69s**, Python **3.12.12**. The resource-layout test was excluded because it copies resources through `tmp_path`; this accounts for the difference from the recorded 193-test suite.

6. Independent no-bytecode, in-memory probes using `PYTHONPATH=src`:
   - Replayed all six original Code counterexamples and relevant construction/view variants.
   - Independently checked unset and recursive named lazy dependencies reject without registration.
   - Replayed application equality and truth-conversion rollback/replacement attacks.
   - Exercised twelve transient-provider begin, commit, rollback, undo, redo and retained-scope attacks through ordinary/working access.
   - Exercised nine idle-lazy begin/navigation attacks through default/current/working access.
   - Attacked first-thaw result iteration and item lookup on established and provisional nodes.
   - Attacked manager and subsequent backend key equality/truth stages, preserving the original edit and permitting pure commit retry.
   - Independently injected hidden begin, changed nesting followed by failure, and residual terminal count through explicit and scope completion.
   - Checked healthy joined completion, stale exceptional scopes and idle completion errors.
   - Executed both examples successfully.
7. Independently compiled and executed empty declarations through all nine intermediate YIDL concepts. Each produced a valid `(*, transaction_manager)` constructor and supported initialization, completion and navigation.
8. Two fresh native generated-base renders matched one another and the checked-in base. Canonical tests compared the actual generated executable source with all twenty checked-in goldens.
9. Read-only introspection confirmed eleven public marker factories are the exact Lifecycle objects, five keyed manager methods default to `DEFAULT_TRANSACTION`, and nine package YIDL resources are discoverable. Regenerator help exposes checking as the ordinary operation and `--write` as explicit mutation.

Final status contained only measurement-output changes and untracked round-five review prompts, which are outside the reviewed object. Reviewed paths remained unchanged.

No files were written or edited; no installations, builds, regeneration with writes, Git mutations, neighboring edits or additional agents were performed. No other current-round report was read.

## 2. Invariant analysis

The attempted refutations did not establish a remaining defect:

- **Managed mutability and views:** Idle, current and construction writes reject. Ordinary reads do not initiate thaw. Existing, pending and provisional relationships propagate default/current/working views. First-thaw output receives the same projection before installation; repeated access preserves owned working containers.
- **Construction and providers:** Named dependencies resolve private baselines in dependency order. Named lazy providers materialize once and agree with self-provider behavior. Unset, unresolved and recursive providers fail contextually without partial registration. Controlled nested construction retains the original manager context.
- **Lifecycle joins and scopes:** Healthy inner completion discharges one join without publication; outer completion publishes once. Rollback closes the entire joined edit. Stale normal scopes reject; stale exceptional scopes preserve the body exception and leave replacement work unchanged.
- **Completion authority:** The amended path captures authority before dispatch. A no-evidence success requires genuine joined nesting, a `None` result and exactly one decrement with unchanged token, overlay, selection, state and backend key. Failure without terminal evidence remains repairable only when the original owner is intact. Hidden acquisition, unexpected transitions and residual terminal nesting fault and detach editable state.
- **Terminal evidence and persistent faults:** Terminal admission checks original token/evidence identity, no active token, zero nesting, publication/discard evidence, cleanup, detached prepared state and the proper result. A diagnosed callback ownership fault cannot become healthy merely because backend after-actions reset the state to Idle.
- **Begin/setup failures:** Existing acquisition, overlay allocation, enlistment and both binding-stage fault coverage passed. Confirmed clean closure allows retry without hidden nesting; incomplete ownership or abort evidence faults and detaches overlays.
- **Graph integrity:** Shared children preserve identity. Managed cycles and foreign edges reject. Working membership reflects escaped-container changes. Empty final roots, provisional editing, removed-node restoration and unavailable omitted/aborted/future-only handles retain their stated behavior.
- **Sparse history and branches:** Predecessor lookup rejects negative positions. Branch preparation trims every future field and presence history, including untouched fields. Failed preparation and rollback preserve redo. Empty and touch-only successful edits publish frames.
- **Absence and snapshots:** Strict absence raises. Last-visible descendants remain pinned and read-only. Snapshots retain nested aliases, frozenset identities and abandoned-branch data while excluding nonmanaged fields and application methods.
- **Stable storage and publication:** Mapping wrappers normalize to private immutable backing storage. A complete frozen candidate is prepared and validated before one selection assignment; later-node failure publishes no earlier prepared value.
- **Nonversioned/transient policies:** Const references, plain fields, bindings, local stores and lazy results retain shared semantics. Candidate ordinary/working transient reads use token-local values; current reads use baselines. Completion clears overlays, including removed nodes.
- **Application callbacks and keys:** Original equality/truth, transient-provider and idle-lazy attacks reject before same-manager mutation. Mapping traversal and first-thaw result traversal remain fenced. Failed target materialization installs nothing and permits pure retry. Key comparison, truth conversion and diagnostics are fenced at manager and backend stages.
- **Generation and compatibility:** Nine inheritable concepts generate executable native AST. Matchers select constructor forms, field kinds, lazy policies, binding shape, transient factories and managed view/thaw access. Annotation recognition uses `inspect.get_annotations`. Exact Lifecycle marker reuse and inherited field-ID coverage remain intact.

These conclusions rest on source inspection, canonical execution and independent counterexample replay. Existing passing tests alone were not accepted as historical closure.

## 3. Risks and next action

Independent execution establishes Python 3.12.12 source behavior and read-only native generation checks. The recorded Python 3.13.12/3.14.3 matrix, wheel contents and isolated installed-wheel checks were inspected but not independently repeated.

Acceptance is scoped to the pinned dependency tuple and the accepted serialized, in-memory design. Public registry release, arbitrary older same-version dependency compatibility and the explicit persistence, concurrency, collaboration, ownership, adapter, multi-key and multiple-generated-base deferrals remain outside this verdict.

No new architectural root or bounded correction requirement was established.

The next action is to combine this Code + Surface GO with the independent State verdict on the same settled tuple before recording runtime acceptance.

## Prior-finding closure table

Historical namespaces are explicit. Every CLOSED row includes independent replay of the original counterexample on this tuple.

| ID | Disposition claimed | Verified on corrected tree | Status |
| --- | --- | --- | --- |
| Code round 1 P2-1 | Supply explicit empty constructor parameters in the owning YIDL resource; retain required keyword-only `transaction_manager`. | Decorated empty, local-store-only, classvar-only and managed `init=False` declarations. Each constructed with only `transaction_manager`, initialized, committed and navigated. Signatures were `(*, transaction_manager)`. Independently executed empty declarations through all nine concepts. | CLOSED |
| Code round 1 P2-2 | Recursively project exact built-in sets; preserve working ownership and separate ordinary projection. | Replayed the original `frozenset`/`set` scenario. Ordinary access returned the default child without touching its value; the owned set retained working children. Pending current-child sets projected to working. Escaped-set mutation after completion did not change committed membership. | CLOSED |
| Code round 1 P2-3 | Materialize named lazy constructor providers and reject unusable providers contextually. | Replayed named-versus-self const providers, managed consumers, reversed order and provisional construction. All received `7`, with one evaluation per instance across views. Unset and recursive named dependencies independently rejected without node registration. | CLOSED |
| Code round 2 P2-4 | Project raw provisional child facades to the requested parent view under the operation fence. | Replayed a provisional parent containing `child.current` while the child had pending data, before and after attachment. Ordinary access returned the default child and pending value; working access permitted nested append. Current provisional access stayed absent. Publication retained both edits. | CLOSED |
| Code round 2 P2-5 | Fence provisional projection/thaw before backing-map callbacks and retain original token/overlay ownership. | Replayed the original application-backed mapping rollback attack through working and ordinary access. Both rejected before completion, preserved the original token and pending root value, left the provisional target untouched and permitted pure retry. Navigation, replacement and retained-scope diagnostic variants also passed. | CLOSED |
| Code round 3 P2-6 | Project thaw output to working views inside the original fence before installation/return. | Replayed the original fresh-list converter on established/provisional parents returning default/current children. The first read returned working children, exposed pending values and permitted nested thaw/edit. Repeated access preserved container identity. Independent result iteration/item-lookup attacks rejected without installation and permitted retry. | CLOSED |

Code round 4 reported no new finding; it added no seventh closure obligation.

## Changed-range analysis

Since `d0f85e6`, two runtime modules changed, six API-documentation lines were added, and one narrow completion-authority test file was introduced. No owning YIDL resource, generated base, canonical story, golden, public marker or packaging dependency changed. Process records document the correction and verification.

- **Captured authority, `callbacks.py:9–52`:** `OperationContext` now includes backend key identity. Integrity checks require exact integer nesting/token IDs before equality, preventing application scalar protocols from running during the post-callback check.
- **Stale scopes, `transaction_yidl.py:368–378`:** Stale original callbacks execute through the shared fenced dispatch and must leave the captured replacement owner intact. Ordinary stale rollback retains Lifecycle’s exception-preserving behavior.
- **Shared completion dispatch and fault path, `transaction_yidl.py:673–696`:** Dispatch returns result/failure for one outcome analysis. The fault helper retains available completion evidence, identifies the known selection, detaches overlays and raises `HistoryFaultError` with the causal failure.
- **Nonterminal transition, `transaction_yidl.py:698–738`:** Completion requires original authorization. No-evidence failure is repairable only with intact authority. Successful inner completion requires genuine joined nesting and the exact permitted one-count decrement.
- **Terminal transition, `transaction_yidl.py:739–774`:** Health requires original token/evidence identity, zero nesting, no active transaction, existing publication/cleanup evidence, detached editable/prepared state, Idle state and the expected result. The existing fault reason prevents cleanup from reviving a diagnosed fault.
- **Coverage and documentation:** The 55 narrow authority cases exercise explicit/scope transitions, unexpected acquisition, stale replacement ownership, terminal identity/results, scalar traps and persistent faults. API additions state these expectations without changing method names, defaults or lifecycle placement.

Independent amended-path probes reproduced the intended rejection of hidden begin, changed nesting then failure and residual terminal count, while healthy nested completion and original callback/key retries still worked.

The changes implement the merged bounded disposition and preserve the accepted original Lifecycle tokens, one-participant publication model and native generation architecture. No change outside those dispositions or **NEW ARCHITECTURAL root cause** was established.

## 4. Surface

The cold Python walkthrough identifies package-root imports, `@undoable`, required `transaction_manager=`, setup construction and explicit initialization. First use, normal commit, exceptional rollback, undo/redo, nested child editing and snapshots are discoverable. Both examples passed.

Begin/commit/rollback, undo/redo and root add/remove form documented lifecycle pairs. Defaults are stated for the manager key, strict absence, unmarked field interpretation and lazy mutability. Introspection agrees with the keyed defaults. Regeneration checks by default and writes only with `--write`.

Default/current/working handles, provisional absence, first-thaw projection, pinned snapshots, shared nonversioned resources and fault recovery limits are explained. All six historical surface contradictions no longer reproduce.

Installation requires the documented relative sibling-source development layout. The README provides development commands but no standalone dependency-cloning recipe, so that layout must be supplied by the workspace operator. This remains a local-draft documentation limitation; no registry installation or release is advertised.

No additional naming, default, lifecycle-pair or compatibility-shape defect was established.
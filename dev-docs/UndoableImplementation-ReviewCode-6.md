# YIDL Undoable implementation — CODE + SURFACE-AXIS REVIEW

**Review object:** Complete `yidl_undoable` runtime package, tests, examples, generation resources, documentation and configuration at `9d18d60e2244183f3f4715577a1356bf85b517a9`. Local implementation draft; runtime acceptance pending. Controlling design: `dev-docs/UndoableDesign.md`, accepted at `616f2f65473b1240535a6317d8cc79d5cec18414`.

**Baseline:**

| Repository | Exact revision |
| --- | --- |
| `yidl_undoable` | `9d18d60e2244183f3f4715577a1356bf85b517a9` |
| `yidl-lifecycle` | `230362f642d6e9205897698670fe5f87d2c905ce` |
| `yidl` | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| `astichi` | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| `yidl-cache` | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Sources were inspected from the working tree, with read-only Git comparisons confirming that reviewed implementation paths match `HEAD`. The accepted design and implementation plan match their controlling revisions. Correction comparison: `adcdc3071c00330787c12d05faeb381705215d2d..9d18d60e2244183f3f4715577a1356bf85b517a9`.

**Date:** 2026-10-12

**Axis:** Code architecture, interfaces, call graphs, generation and compatibility, plus the cold Python API surface. Independent, adversarial, read-only replacement review. The other axis runs in parallel; nothing here relies on its current-round report. Filed verbatim by the lane owner.

**Verdict: GO** — no P0, P1, P2 or P3 findings established. All six historical Code findings were independently replayed and are closed on this tuple. The complete five-repository tuple was checked at review start and end and remained unchanged.

---

## 0. Evidence base

The cold reading order was `README.md`, `docs/API.md`, then `examples/first_use.py` and `examples/nested.py`, before design, implementation source or historical reports.

Subsequent inspection covered:

- Workspace `AGENTS.md`, `AGENTS_GWZ.md`, and the complete governing `dev-docs/review-prompts/UndoableImplementation-Code-Round6.md`.
- Controlling `CurrentProgramCheckpoint.md`, `UndoableDesign.md` and `UndoableImplementationPlan.md`.
- All five historical same-axis reports: `UndoableImplementation-ReviewCode.md` and numbered reports 2–5.
- All five merged remediation plans: `UndoableImplementation-RemPlan.md` and numbered plans 2–5.
- `docs/Architecture.md`, package exports, exact Lifecycle marker re-exports, regeneration interface and `pyproject.toml`.
- `src/yidl_undoable/transaction_yidl.py:1–810`, particularly construction registration, begin setup, original scope callbacks, candidate preparation, projection and completion authority.
- Construction/provider mechanics in `facades.py`; callback capture and dispatch in `callbacks.py`; stable normalization and recursive projection in `values.py`; history, graph, absence, snapshots, states, bindings, candidate and error support.
- Declaration harvesting and native executable AST assembly in `undoable_harvester.py` and `undoable.py`.
- All nine owning YIDL resources, their matcher-selected contributions, extension chain and assembly dependencies.
- All twenty canonical scenario sources and their executed generated-source comparisons.
- Definition, annotation, history, diagnostic, callback, setup and synthetic-fault tests, including the amended 77-case completion-authority suite.
- Pinned Lifecycle token identity, original scope binding, stale callbacks, nested completion, participant cleanup and terminal evidence in `src/yidl_lifecycle/transaction_yidl.py`.
- Implementation, TDD and verification records. Their reported wheel and interpreter results were inspected as evidence claims, not accepted as substitutes for runtime attacks.

Commands and observed results:

1. From the canonical workspace root, `git -C <member> rev-parse HEAD` for all five members at both ends: every result matched the exact tuple.
2. Read-only correction diff and statistics: production changes are confined to `transaction_yidl.py` and its API documentation; supporting completion tests and process/evidence records changed.
3. `git diff --exit-code HEAD -- src tests docs examples README.md pyproject.toml dev-docs/UndoableDesign.md dev-docs/UndoableImplementationPlan.md`: exit 0.
4. Design comparison with `616f2f65473b1240535a6317d8cc79d5cec18414` and plan comparison with `3440ec2fcee3a8d61c1f88cdfbafafc0683edabf`: exit 0.
5. Whitespace check over changed implementation, tests and public documentation: exit 0.
6. From `yidl_undoable`:

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

   Result: **214 passed in 12.02s**, Python **3.12.12**. The resource-layout test was excluded because it copies resources using `tmp_path`; this explains the difference from the recorded 215-test full suite.

7. Independent no-bytecode, in-memory probes using `PYTHONPATH=src`:
   - Replayed all six historical Code counterexamples and their relevant setup/provisional, ordinary/current/working and declaration-order variants.
   - Replayed application equality and truth-conversion rollback/replacement attacks.
   - Exercised fourteen transient-provider begin, completion, navigation and retained-scope attacks through ordinary/working access.
   - Exercised nine idle-lazy begin/navigation attacks through default/current/working access.
   - Exercised twenty operation-incompatible outcomes through explicit and token-bound scope entry, with and without post-transition exceptions.
   - Independently reproduced the hidden-begin, changed-nesting failure and residual terminal-count attacks through both completion entries.
   - Verified rollback at depths one, two and three through explicit and scope entry.
   - Retained outer scope callables before a later begin rebound the token; both premature publication and nonterminal rollback faulted.
   - Verified genuine preparation rejection through explicit and scope completion preserves selection and redo, while preview failure remains repairable.
   - Verified four failures before any backend transition preserve the exact original edit, state, token and nesting.
   - Exercised sixteen manager/backend key equality and truth attacks, followed by successful pure commit retry.
   - Exercised converter-result iteration and lookup attacks on established and provisional nodes.
   - Verified authentic backend publication evidence without actual selection installation faults while keeping confirmed old data readable.
   - Executed both examples successfully.
8. Independently compiled and executed empty declarations through all nine intermediate YIDL concepts. Each produced a valid `(*, transaction_manager)` constructor and supported initialization, completion and navigation.
9. Two fresh native generated-base renders matched one another and the checked-in base. Canonical execution compared actual generated source with all twenty goldens.
10. Read-only introspection confirmed eleven exported marker factories are the exact Lifecycle objects, all five keyed manager operations default to `DEFAULT_TRANSACTION`, and nine YIDL resources are discoverable. Regenerator help exposes checking as the default and `--write` as explicit mutation.

Final status contained only measurement-output changes and untracked round-six prompts, outside the reviewed object. Reviewed paths remained unchanged.

No file writes, installations, builds, regeneration with writes, Git mutations, neighboring edits or additional agents were performed. No other current-round report was read.

## 2. Invariant analysis

The attempted refutations did not establish a remaining defect.

- **Managed mutation:** Idle, current and constructor writes reject. Ordinary reads do not initiate thaw. Candidate managed reads through all three views resolve the frozen candidate.
- **Construction and providers:** Named dependencies resolve private baselines in dependency order. Named lazy providers materialize once and agree with self-provider behavior. Unset, unresolved and recursive providers fail contextually without partial registration. Controlled nested construction remains supported.
- **View propagation:** Established, pending and provisional relationships propagate their requesting view. Exact working sets and fresh thaw-result containers project children correctly on the first read. Repeated working reads preserve owned container identity; ordinary projection does not rewrite those owned children.
- **Begin setup:** Inspection and executed fault coverage cover partial acquisition, overlay allocation, enlistment, binding, joined setup and abort failure. Confirmed closure allows retry; incomplete ownership or cleanup detaches editable state and faults.
- **Joined completion:** Only commit may return a nonterminal result. It must begin genuinely joined, return `None`, decrement exactly once and preserve token, overlay, selection, state and backend key. Independent incompatible-outcome probes rejected premature joined publication and discard.
- **Outer commit:** Successful terminal admission requires original depth one, authentic identity/cleanup evidence and confirmed selection installation. A genuine preparation failure may propagate after complete discard with unchanged selection. Independent freeze-rejection probes preserved redo and allowed a later new edit.
- **Rollback:** At every tested depth, explicit and original scope rollback discarded the entire edit and preserved selection. Delegating rollback to either inner or publishing commit faulted.
- **Outcome with failure:** A post-transition exception did not authorize an incompatible operation. Wrong commit/rollback outcomes faulted with the causal exception retained.
- **Original scopes:** Guarded callbacks retain the original token-bound backend behavior. Stale normal completion rejects; stale exceptional completion preserves the body exception and replacement edit. Callables retained before later scope rebinding remained subject to the correct requested operation.
- **Authority and fault persistence:** Hidden acquisition, changed nesting followed by failure, residual terminal nesting, altered identities and unconfirmed installation fault. A failure before any authority change remains repairable. Backend cleanup cannot revive an already diagnosed fault.
- **Graph integrity:** Canonical execution and source inspection cover shared aliases, cycles, foreign-manager edges, recomputed working reachability, empty final roots, provisional editing and removed-node restoration. Omitted setup, aborted and future-only handles cannot be resurrected.
- **Sparse history and branching:** Negative predecessor positions reject. Branch preparation trims all future field and presence records, including untouched fields. Failed preparation and rollback preserve redo. Empty and touched-only successful commits create frames.
- **Absence and snapshots:** Strict absence raises. Last-visible descendants remain pinned and read-only. Snapshots preserve nested aliases, frozenset node identity and abandoned-branch data while excluding nonmanaged fields and application methods.
- **Stable values and atomic publication:** Mapping wrappers normalize into private immutable backing storage. Complete rooted candidates are frozen and validated before one selection assignment; a later-node failure publishes no earlier value.
- **Field policy parity:** Const references, plain values, bindings, local stores and lazy results retain shared nonversioned behavior. Candidate ordinary/working transient reads use token-local values; current reads use baselines. Completion clears transient overlays, including removed nodes.
- **Callback ownership:** Equality/truth, transient-provider, idle-lazy, provisional mapping and thaw-result traversal attacks reject before same-manager mutation. Failed materialization installs no target and permits pure retry. Key callbacks are fenced at both manager and subsequent backend stages.
- **Generation and compatibility:** Nine inheritable concepts produce executable native AST. Matchers select constructor forms, field kinds, binding shape, lazy policy, transient factory paths and managed view/thaw access. Annotation recognition uses `inspect.get_annotations`; exact marker reuse, contextual definition errors and stable inherited field IDs remain covered.

These conclusions combine source retracing, executed canonical behavior and independent original-counterexample replay. Historical GO reports and existing tests alone were not treated as closure.

## 3. Risks and next action

Independent execution establishes Python 3.12.12 source behavior and read-only native generation checks. The recorded Python 3.13.12/3.14.3 matrix, wheel contents and isolated installed-wheel checks were inspected but not independently repeated.

The verdict is limited to the pinned dependency tuple and accepted serialized, in-memory design. Registry release and compatibility with arbitrary older distributions bearing the same dependency version numbers are not established.

No **NEW ARCHITECTURAL root cause** or bounded correction requirement was established. The completion correction is coherent with the existing captured authority, terminal evidence and single publication boundary; it does not require redesign.

The next action is to combine this Code + Surface GO with the independent State verdict on the same exact tuple before recording runtime acceptance.

## Prior-finding closure table

Every CLOSED row includes independent replay of the original counterexample on this revision.

| ID | Disposition claimed | Verified on corrected tree | Status |
| --- | --- | --- | --- |
| Code round 1 P2-1 | Explicit empty constructor-parameter composition; preserve mandatory keyword-only manager. | Decorated empty, local-store-only, classvar-only and managed `init=False` declarations. Each constructed with only `transaction_manager`, initialized, committed and navigated. Signatures were `(*, transaction_manager)`. Empty declarations also executed through all nine concepts. | CLOSED |
| Code round 1 P2-2 | Recursive exact-set projection with separate ordinary projection and preserved working ownership. | Replayed the original `frozenset`/`set` case. Ordinary access returned the default child without touching its value; the owned set retained working children. Assigned current-child sets projected to working. Escaped-set mutation after completion did not change committed membership. | CLOSED |
| Code round 1 P2-3 | Materialize named lazy constructor providers; reject unusable providers contextually. | Replayed named/self const providers, managed consumers, reversed declaration order and provisional construction. Consumers received `7`, with one provider evaluation per instance shared across views. Unset and recursive providers rejected without registration. | CLOSED |
| Code round 2 P2-4 | Project raw provisional child handles to the parent’s requested view. | Replayed a provisional parent containing `child.current` while the child had pending data, before and after attachment. Ordinary access returned the default child and pending value; working access permitted nested append. Current provisional access remained absent; publication retained the edits. | CLOSED |
| Code round 2 P2-5 | Fence provisional projection/thaw before mapping callbacks and retain original ownership. | Replayed the original mapping-backed rollback attack through ordinary and working access. Navigation, begin and retained-scope variants also rejected before completion, preserved the original token and pending root value, left the target untouched and permitted pure retry. | CLOSED |
| Code round 3 P2-6 | Project thaw output to working views inside the original fence before installation. | Replayed the original fresh-list converter on established/provisional parents returning default/current children. The first read returned working children, exposed pending values and permitted nested editing; repeated reads preserved container identity. Independent result iteration/lookup attacks rejected without installation and permitted retry. | CLOSED |

Code rounds 4 and 5 reported no new Code findings and therefore add no seventh or eighth same-axis closure obligation.

## Changed-range analysis

Since `adcdc3071c00330787c12d05faeb381705215d2d`, production changes affect one runtime module and API documentation. Completion tests and process/evidence records accompany the correction. No owning YIDL resource, generated base, canonical story, golden, public marker or packaging dependency changed.

- **Requested operation propagation, `transaction_yidl.py:269–407`:** Explicit commit/rollback and guarded original scope callbacks now pass the requested operation into shared completion analysis. Stale callbacks retain their separate unchanged-replacement-owner contract.
- **Publication confirmation, lines 687–701:** Selection integrity retains the existing unchanged-selection alternative and a factored original-token installation check.
- **Operation predicate, lines 703–719:** Rollback requires complete discard without publication and unchanged selection. Terminal commit requires original depth one and confirmed installation, or propagated recorded rejection with complete unchanged-selection discard.
- **Shared completion, lines 730–804:** Nonterminal admission is restricted to joined commit. Existing original identity, exact decrement, terminal cleanup, zero nesting, detached state and persistent-fault checks remain in force. Operation-incompatible outcomes use the existing fault path.
- **Documentation and coverage:** API text distinguishes inner commit, outer commit, preparation rejection and rollback. Twenty-two added narrow cases cover incompatible outcomes, exception variants and publication evidence without installation.

Independent probes reproduced the specified rejection through explicit, current scope and pre-rebinding retained scope callables. Healthy joins, rollback at multiple depths, genuine preparation failures, original-owner repairability and historical callback retries still worked.

The inspected changes implement the merged bounded disposition. No change outside that correction or **NEW ARCHITECTURAL root cause** was established.

## 4. Surface

The cold Python walkthrough identifies package-root imports, `@undoable`, required `transaction_manager=`, setup construction and explicit initialization. First use, normal commit, exceptional rollback, undo/redo, nested editing and snapshots are discoverable. Both examples passed.

Begin/commit/rollback, undo/redo and root add/remove form documented lifecycle pairs. Defaults are stated for transaction keys, strict absence, unmarked field interpretation and lazy mutability. Introspection agrees with the keyed defaults. Regeneration checks by default and writes only with `--write`.

Live default/current/working views, provisional absence, pinned snapshots, shared nonversioned resources, transient cleanup and fault recovery limits are explained. The amended completion documentation agrees with the observed operation-specific behavior. All six historical surface contradictions no longer reproduce.

Installation assumes the stated relative sibling-source development layout. The README supplies development commands but no standalone dependency-cloning recipe; the workspace operator must supply that layout. For this explicitly local, unpublished draft, this remains a documentation limitation below the finding threshold.

No additional naming, default, lifecycle-pair or compatibility-shape defect was established.

**End-of-review confirmation:** `yidl_undoable` remained at `9d18d60e2244183f3f4715577a1356bf85b517a9`; Lifecycle, YIDL, Astichi and Cache remained at the exact revisions in the baseline table. Reviewed files remained unchanged. **Final verdict: GO.**
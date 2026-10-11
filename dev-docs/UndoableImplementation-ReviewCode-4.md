# YIDL Undoable implementation — CODE + SURFACE-AXIS REVIEW

**Review object:** Complete `yidl_undoable` runtime package, tests, examples, generation resources, documentation and configuration at `d0f85e6005aefb91098d4164663b07e40c7b757e`; local implementation draft, runtime acceptance pending. Controlling design: `dev-docs/UndoableDesign.md`, accepted at `616f2f65473b1240535a6317d8cc79d5cec18414`.

**Baseline:**

| Repository | Pinned revision |
| --- | --- |
| `yidl_undoable` | `d0f85e6005aefb91098d4164663b07e40c7b757e` |
| `yidl-lifecycle` | `230362f642d6e9205897698670fe5f87d2c905ce` |
| `yidl` | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| `astichi` | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| `yidl-cache` | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Sources were read from the working tree. Read-only Git comparisons confirmed the reviewed runtime, tests, public documentation, examples, configuration and controlling documents match `HEAD`. The design matches its accepted revision; the implementation plan matches `3440ec2fcee3a8d61c1f88cdfbafafc0683edabf`. Correction comparison: `38662bcbbe7758fb5f980859675fa9efcb41d614..d0f85e6005aefb91098d4164663b07e40c7b757e`. The complete tuple was verified at review start and end and did not move.

**Date:** 2026-10-12

**Axis:** Code architecture, interfaces, call graphs, composition and compatibility, plus the cold Python API surface. Independent, adversarial, read-only replacement review under Step 5.5. The other axis runs in parallel; nothing here relies on its current-round report. Filed verbatim by the lane owner.

**Verdict: GO** — no P0, P1, P2 or P3 findings established. All six historical Code findings are independently closed on this exact tuple.

---

## 0. Evidence base

The cold reading order was `README.md`, `docs/API.md`, then `examples/first_use.py` and `examples/nested.py`, before design, implementation source or historical reports.

Subsequent inspection covered:

- Workspace `AGENTS.md` and `AGENTS_GWZ.md`, and the complete canonical `dev-docs/review-prompts/UndoableImplementation-Code-Round4.md`.
- The complete controlling `dev-docs/CurrentProgramCheckpoint.md`, `UndoableDesign.md` and `UndoableImplementationPlan.md`.
- All three historical same-axis reports: `UndoableImplementation-ReviewCode.md`, `UndoableImplementation-ReviewCode-2.md` and `UndoableImplementation-ReviewCode-3.md`.
- All three merged remediation plans: `UndoableImplementation-RemPlan.md`, `UndoableImplementation-RemPlan-2.md` and `UndoableImplementation-RemPlan-3.md`.
- `docs/Architecture.md`, public exports, exact Lifecycle marker re-exports, `pyproject.toml` and the regeneration interface.
- Runtime construction/provider mechanics in `facades.py`; the complete manager/aggregate implementation in `transaction_yidl.py:1–709`; callback ownership and dispatch in `callbacks.py`; normalization/projection in `values.py`; and graph, history, absence policy, snapshot, binding, candidate, state and error support.
- Declaration recognition, inheritance adaptation and executable AST assembly in `undoable_harvester.py` and `undoable.py`.
- All nine owning YIDL resources, generated record/container and assembly structure, the checked-in generated-base comparison, and the canonical intermediate-layer fixture.
- All twenty canonical scenario sources and their executable generated-source comparisons, plus definition, recognition, history, state, fault, callback, remediation, setup, provisional, thaw-result and transaction-key diagnostics.
- Pinned Lifecycle key dispatch, group begin/completion, scope binding, stale-token behavior and terminal completion evidence.
- `ImplementationDraft.md`, `TddEvidence.md` and `VerificationEvidence.md`, treated as claims to inspect rather than proof of acceptance.

Commands and observed results:

1. From the canonical workspace root, `git -C <member> rev-parse HEAD` for all five members at both ends of the review: every result matched the exact tuple.
2. Read-only correction diff and statistics: the runtime changes are confined to `callbacks.py` and `transaction_yidl.py`; the associated coverage and API changes are analyzed below.
3. `git diff --exit-code HEAD -- src tests docs examples README.md pyproject.toml dev-docs/UndoableDesign.md dev-docs/UndoableImplementationPlan.md`: exit 0.
4. Comparisons of the controlling design with `616f2f6` and implementation plan with `3440ec2`: exit 0.
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
     tests/test_generation.py::test_matcher_selected_executable_surface
   ```

   Result: **137 passed in 7.12s**, Python **3.12.12**. The single resource-layout test was excluded because it copies resources through `tmp_path`; this explains the difference from the recorded 138-test full-suite result.

6. Independent no-bytecode, in-memory probes using `PYTHONPATH=src`:
   - Replayed all six original Code counterexamples, with the results recorded in the closure table.
   - Executed both examples successfully.
   - Replayed the original application equality/truth completion and replacement attacks.
   - Exercised transient rollback, commit, navigation, begin and retained-scope completion through ordinary/working access.
   - Exercised idle lazy begin/undo/redo attempts through default/current/working access, checking unset targets, unchanged history and pure retry.
   - Attacked first-thaw output traversal through both mapping iteration and item lookup, on committed and provisional parents.
   - Checked cyclic and foreign-manager thaw outputs reject without touching the target or losing pending edits.
   - Attacked first and subsequent manager/backend key-comparison stages in commit, rollback, joined begin and active-token lookup, plus retained scope completion.
   - Independently generated and executed empty declarations through all nine intermediate concepts, confirming valid `(*, transaction_manager)` constructors.
7. Read-only introspection confirmed eleven public marker factories are the exact Lifecycle objects, all five keyed manager operations default to `DEFAULT_TRANSACTION`, and nine package YIDL resources are discoverable.
8. Two fresh native generated-base renders matched each other. The permitted generation test confirmed equality with the checked-in base. Regenerator help identifies checking as the ordinary operation and `--write` as the explicit mutation option.

Final member status showed changes only to measurement output and untracked round-four review prompts, which are explicitly outside this review object. The reviewed paths remained unchanged.

No files were written or edited; no builds, installations, regeneration with writes, Git mutations, adjacent edits or additional agents were performed. No other current-round report was read.

The recorded round-three State report was completed by the same reviewer after an initial service error that produced no complete report or verdict. That failed attempt is not a third review.

## 2. Invariant analysis

The attempted refutations did not establish a remaining defect:

- **Transaction-only managed mutability:** Idle, current and construction writes reject. Ordinary reads do not initiate thaw. Candidate managed reads through every view resolve frozen candidate data.
- **Construction and providers:** Private resolved baselines are available through construction views. Named dependencies resolve in order; lazy providers materialize once. Unresolved and recursive dependencies fail contextually without partial registration. Controlled nested construction remains supported.
- **Lifecycle joins and scopes:** Inner completion publishes nothing; rollback closes the joined edit. Stale normal exits reject, while stale exceptional exits preserve the body exception and cannot abort replacement work.
- **Setup failures:** The permitted fault tests cover partial backend acquisition, overlay allocation, enlistment, both binding stages, joined setup and abort failures. Confirmed clean closure permits retry without hidden nesting; incomplete ownership or cleanup detaches overlays and faults.
- **Graph integrity:** Aliases preserve node identity. Managed cycles and foreign edges reject. Escaped-container changes affect recomputed working membership. Empty final roots, provisional editing, removed-node restoration and unavailable omitted/aborted/future-only handles retain their stated behavior.
- **Sparse history and branches:** Negative predecessor lookup rejects. Branch preparation trims every future field and presence history, including untouched fields. Failed preparation and rollback preserve redo. Empty and touch-only successful edits publish frames.
- **Absence and snapshots:** Strict absence raises; last-visible descendants remain pinned and read-only. Snapshots retain aliases and abandoned-branch data, including frozenset references, while excluding nonmanaged fields and application methods.
- **Stable storage and publication:** Mapping wrappers normalize into private immutable backing stores. Later-node freeze or validation failures publish no earlier prepared value. Preparation builds a complete replacement epoch before one selection assignment.
- **Nonversioned/transient policies:** Const references, ordinary fields, bindings, local stores and lazy results retain shared behavior. Candidate ordinary/working transient reads retain token-local values; current reads retain baselines. Completion clears transient overlays, including removed nodes.
- **Callback ownership:** Original equality/truth, transient-provider and idle-lazy attacks reject before same-manager mutation. Backed mapping traversal is fenced during normalization, pending/provisional projection and first-thaw output projection. Failed materialization leaves its target uninstalled and supports pure retry.
- **Key callbacks:** Manager checks and backend dispatch both fence equality, truth conversion and diagnostics. Rejected pre-acquisition reentry preserves the original edit and nesting. Authorized backend transitions remain possible, with acquisition and terminal evidence supplying their ownership checks.
- **Fault evidence:** Confirmed installed history remains readable after cleanup faults. Unconfirmed publication blocks live managed reads and new snapshots; previously pinned snapshots remain readable.
- **Generation and compatibility:** The nine concepts generate executable AST, with matchers selecting constructor forms, field kinds, binding shape, lazy policies, transient factories and managed view/thaw behavior. All twenty canonical source comparisons and base checks passed. Annotation recognition uses the language API.

These conclusions combine source inspection, executable canonical coverage and independent original-counterexample replay; passing existing tests alone was not treated as closure.

## 3. Risks and next action

Independent execution in this review establishes Python 3.12.12 source behavior and read-only native generation checks. The recorded Python 3.13.12/3.14.3 matrix, rebuilt wheel contents and isolated installed-wheel checks were inspected but not repeated.

Acceptance remains scoped to the pinned dependency tuple and the accepted serialized, in-memory design. Registry publication, arbitrary older same-version dependency compatibility and the explicit persistence, concurrency, ownership, adapter and multi-key deferrals are outside this verdict.

No new architectural root or bounded correction requirement was established.

The next action is to combine this Code + Surface GO with the independent State-axis verdict on the same settled tuple before recording runtime acceptance.

## Prior-finding closure table

Historical namespaces are distinguished explicitly. Each CLOSED entry includes independent replay of the original counterexample on this tuple.

| ID | Disposition claimed | Verified on corrected tree | Status |
| --- | --- | --- | --- |
| Code round 1 P2-1 | Supply explicit empty constructor parameters in the owning YIDL resource; retain required keyword-only `transaction_manager`. | Independently decorated empty, local-store-only, classvar-only and managed `init=False` declarations. All constructed with only `transaction_manager`, initialized, committed and navigated. Signatures were `(*, transaction_manager)`. Empty declarations also generated and executed through all nine intermediate concepts. | CLOSED |
| Code round 1 P2-2 | Recursively project exact built-in sets; preserve working ownership and keep ordinary projection separate. | Replayed the original `frozenset`/`set` scenario. Ordinary access returned a default child without touching its value; the owned set retained working children. Pending current-child sets projected to working. Escaped-set mutation after completion did not change committed membership. Canonical story 14 additionally passed nested-container/current checks. | CLOSED |
| Code round 1 P2-3 | Materialize named lazy constructor providers; reject unusable providers contextually. | Replayed named-versus-self const providers and the managed-provider variant, including reversed order and provisional construction. Every consumer received `7`; one evaluation was shared across views. Unset/recursive providers rejected without registration. | CLOSED |
| Code round 2 P2-4 | Project raw provisional baseline child handles to the requested parent view under the operation fence. | Replayed the original parent containing `child.current` with a pending child edit, before and after attachment. Ordinary access returned the default child and pending data; working access returned the working child and permitted nested append. Current provisional access remained absent. Publication preserved both edits. | CLOSED |
| Code round 2 P2-5 | Fence provisional projection/thaw before backing-map callbacks; preserve original token and overlay. | Replayed the original mapping-backed rollback attack through working access, then ordinary access. Additional navigation, rollback/replacement and retained-scope attempts rejected before completion, preserved the original token/pending root edit, left the target untouched and permitted pure retry. The ten canonical diagnostic variants also passed. | CLOSED |
| Code round 3 P2-6 | Project the thaw result to working views inside the original fence before installation/return. | Replayed the exact first-thaw fresh-list converter for committed/provisional parents and default/current returned children. The first read returned working children, exposed pending values and allowed nested thaw/edit; repeated access preserved the owned container. Mapping output iteration/item-lookup attacks rejected without touched installation; pure retry succeeded. Canonical story 19 additionally passed nested dict/set identity checks. | CLOSED |

## Changed-range analysis

Since `38662bcbbe7758fb5f980859675fa9efcb41d614`, the correction changes two runtime modules, clarifies the API, adds two canonical stories and goldens, adds thaw-result/key diagnostics, and adjusts one existing pending-proxy fixture. No owning YIDL resource or generated-base change occurs.

- **First-thaw output, `transaction_yidl.py:518–544`:** The converter result now passes through recursive working projection inside the same operation-owned call as input projection and thaw. Touched installation follows successful completion of that call. Original first-read behavior and output-traversal attacks are independently closed.
- **Backend fence, `callbacks.py:74–91`:** `dispatch` retains the same-manager mutation fence while allowing the intended backend state transition. It restores depth in `finally`. Begin and completion callers retain their acquisition/terminal-evidence checks instead of incorrectly requiring unchanged ownership during legitimate transitions.
- **Manager key boundaries, `transaction_yidl.py:70–135`, `248–389`, `651–703`:** Construction hashing, key comparison/diagnostics, registration and active-token lookup are fenced. Begin/enlist/binding/setup-abort and completion dispatch protect subsequent backend callbacks. `validate` checks mutation before invoking key code, preventing recursive mutating entry.
- **Pre-acquisition rejection, `transaction_yidl.py:288–298`:** An ownership-intact reentry rejection before backend acquisition preserves existing editing/nesting. Later acquired setup failures continue through the shared abort-or-fault path.
- **Coverage:** Canonical stories 19 and 20 exercise first-thaw child propagation and healthy custom-key aliases/scopes. Narrow tests attack output traversal, repeated key-comparison/truth stages, wrong-key diagnostics, setup abort, constructor hashing and backend error diagnostics.
- **Existing fixture adjustment:** `test_pending_mapping_proxy_traversal_cannot_complete_its_edit` now assigns the pending proxy through its setter before attacking ordinary traversal. Immediate first-thaw traversal now correctly rejects earlier; the adjustment preserves the separate touched-value attack.

The inspected changes implement the merged bounded dispositions and preserve the accepted public API, original Lifecycle tokens, one-participant publication model and native generation architecture. No change outside those dispositions or **NEW ARCHITECTURAL root cause** was established.

## 4. Surface

The cold Python walkthrough identifies package-root imports, `@undoable`, required `transaction_manager=`, setup construction and explicit initialization. First use, normal commit, exceptional rollback, undo/redo, nested child editing and snapshots are discoverable. Both executable examples passed.

Begin/commit/rollback, undo/redo and root add/remove form documented lifecycle pairs. Defaults are stated for the manager key, strict absence policy, ordinary field interpretation and lazy mutability. Regeneration checks by default; writing is explicit.

Default/current/working handles, provisional absence, first-thaw child projection, pinned snapshots, nonversioned resources and fault recovery limits are described together. Signature introspection agrees with the documented keyed defaults. The six previously reported surface contradictions no longer reproduce.

The installation walkthrough requires the stated relative sibling-source development layout. The README provides development commands but no standalone dependency-cloning recipe, so the workspace operator must supply that layout. This remains a local-draft documentation limitation; no registry installation or release is advertised.

No additional naming, default, lifecycle-pair or compatibility-shape defect was established.
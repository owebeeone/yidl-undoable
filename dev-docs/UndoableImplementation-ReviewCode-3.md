# YIDL Undoable implementation — CODE + SURFACE-AXIS REVIEW

**Review object:** Complete `yidl_undoable` runtime package, tests, examples, generation resources, documentation and configuration at `38662bcbbe7758fb5f980859675fa9efcb41d614`; local implementation draft, runtime acceptance pending. Controlling design: `dev-docs/UndoableDesign.md`, accepted at `616f2f65473b1240535a6317d8cc79d5cec18414`.

**Baseline:**

| Repository | Pinned revision |
| --- | --- |
| `yidl_undoable` | `38662bcbbe7758fb5f980859675fa9efcb41d614` |
| `yidl-lifecycle` | `230362f642d6e9205897698670fe5f87d2c905ce` |
| `yidl` | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| `astichi` | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| `yidl-cache` | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Sources were read from the working tree. Read-only Git comparisons confirmed reviewed runtime files, tests, user documentation, examples, configuration and controlling documents match `HEAD`. The design matches its accepted revision; the implementation plan matches `3440ec2fcee3a8d61c1f88cdfbafafc0683edabf`. Correction comparison: `72e1433e1290cc41392223c9d5981847e396f68e..38662bcbbe7758fb5f980859675fa9efcb41d614`. The complete tuple was verified at review start and end and did not move.

**Date:** 2026-10-12

**Axis:** Code architecture, interfaces, call graphs, composition and compatibility, plus the cold Python API surface. Independent, adversarial, read-only replacement review under Step 5.5. The other axis runs in parallel; nothing here relies on its current-round report. Filed verbatim by the lane owner.

**Verdict: NO-GO** — one new P2 finding blocks acceptance. All five historical Code findings are closed. No P0, P1 or P3 findings. I pre-commit to GO on a revision that resolves P2-6 as specified.

---

## Prior-finding closure table

Historical namespaces are distinguished explicitly. Closure means the original counterexample was independently replayed on this tuple.

| ID | Disposition claimed | Verified on corrected tree | Status |
| --- | --- | --- | --- |
| Code round 1 P2-1 | Supply explicit empty constructor parameters in the owning YIDL resource; preserve required keyword-only `transaction_manager`. | Independently decorated empty, local-store-only, classvar-only and managed `init=False` declarations. All constructed with only `transaction_manager`, initialized, committed and navigated. Every signature was `(*, transaction_manager)`. Canonical story 13 and generated-base comparison also passed. | CLOSED |
| Code round 1 P2-2 | Recursively project exact built-in sets, preserving working ownership and keeping ordinary projection separate. | Replayed the original `frozenset`/`set` scenario. Ordinary access after thaw returned a default child and did not touch its field; the owned set retained working children. A pending set containing a current child projected to working. Escaped-set mutation after commit did not change committed membership. Canonical story 14 additionally passed nested-container and current-view checks. | CLOSED |
| Code round 1 P2-3 | Materialize named lazy constructor providers; reject unusable providers contextually. | Replayed named-versus-self const providers and the managed-provider variant, including reversed declaration order and provisional construction. All received `7`, never `MISSING`. Canonical story 15 verified one evaluation per instance across views. Unset and recursive dependency diagnostics passed without partial registration. | CLOSED |
| Code round 2 P2-4 | Project raw provisional baseline child handles to the requested parent view under the operation fence. | Replayed the parent containing `child.current`, with a pending child edit. Ordinary access returned the default child and pending data; working access returned the working child and permitted the nested append. Publication retained both edits. Canonical story 18 passed before/after attachment, nested aliases, untouched no-thaw reads and current provisional absence. | CLOSED |
| Code round 2 P2-5 | Fence provisional projection and thaw before backing-map callbacks; retain original token/overlay ownership. | Replayed the original application-backed `MappingProxyType` rollback attack through working access, then ordinary access. Also independently exercised undo, begin and retained-scope completion. Each raised `ReentrantOperationError` before completion, retained the original token and pending root edit, left the target untouched and permitted pure retry. All ten added proxy cases passed, including rollback/replacement. | CLOSED |

These closures establish the original failures. They do not cover the separate first-thaw-result path in P2-6.

## Changed-range analysis

The runtime correction changes `src/yidl_undoable/transaction_yidl.py`; it adds canonical story 18 and its generated golden, provisional-fence diagnostics, full begin-setup fault diagnostics, API clarifications and implementation/process evidence. No owning YIDL resource or generated-base change occurs in this cycle.

- **Begin setup, lines 242–336:** Captures ownership before backend acquisition and guards backend begin, overlay allocation, aggregate enlistment and wrapper binding together. Successful setup checks token, nesting, selection, state and overlay identities. The shared failure helper detaches editable/prepared state, aborts only the recognized token, requires terminal cleanup evidence, preserves setup/abort causes and keeps detected ownership faults faulted. Added tests cover outer and joined setup, partial backend return, allocation failure, both binding stages, abort failure before/after closure, unexpected nesting and changed selection.
- **Managed reads, lines 499–518:** Moves provisional projection inside the same fenced call as thaw. Untouched provisional reads now recursively project raw facade references instead of using the committed `NodeRef` decoder. Original provisional view and callback counterexamples are closed.
- **Public documentation:** Adds provisional-parent propagation and explains that failed joined setup aborts the entire joined edit, with retry allowed only after confirmed clean closure.
- **Coverage:** Existing canonical stories and narrow diagnostics remain intact; the added story and fault tests execute the real generated classes and backend.

The correction stays within the merged bounded dispositions and preserves the accepted API and architecture. P2-6 is a **bounded retained runtime root cause, not a NEW ARCHITECTURAL root cause**: the first thaw result bypasses the projection already applied to subsequent touched-value reads. The architecture supplies the necessary projection and ownership fence; the missing application is local to materialization.

## 0. Evidence base

Cold reading order was `README.md`, `docs/API.md`, then `examples/first_use.py` and `examples/nested.py`, before design, implementation source or historical reports.

Subsequent inspection covered:

- `dev-docs/CurrentProgramCheckpoint.md`, the complete `UndoableDesign.md` and `UndoableImplementationPlan.md`.
- Both historical same-axis reports, `UndoableImplementation-ReviewCode.md` and `UndoableImplementation-ReviewCode-2.md`, and both merged remediation plans.
- `docs/Architecture.md`, package-root exports, exact marker re-exports, `pyproject.toml` and the regeneration interface.
- `transaction_yidl.py`, `facades.py`, `values.py`, `callbacks.py`, `undoable.py`, `undoable_harvester.py`, and supporting history, graph, policy, snapshot and state mechanics. The changed read path was inspected with numbered lines 463–518.
- All nine YIDL resources and the canonical intermediate-concept fixture.
- All eighteen canonical scenario sources and the narrow definition, recognition, history, state, callback, remediation, provisional-fence and begin-setup tests.
- `ImplementationDraft.md`, `TddEvidence.md` and `VerificationEvidence.md`, treated as claims to inspect rather than acceptance evidence.
- Pinned Lifecycle token binding, group begin, key checking and scope completion mechanics.

Commands and observed results:

1. From the canonical workspace root, `git -C <member> rev-parse HEAD` for all five members at review start and end: every result matched the pinned tuple.
2. Read-only `git diff 72e1433 HEAD -- src/yidl_undoable/transaction_yidl.py docs/API.md`, correction statistics and commit history: changed ranges are analyzed above.
3. `git diff --exit-code HEAD -- src tests docs examples README.md pyproject.toml dev-docs/UndoableDesign.md dev-docs/UndoableImplementationPlan.md`: exit 0.
4. Comparisons of `UndoableDesign.md` with `616f2f6` and `UndoableImplementationPlan.md` with `3440ec2`: exit 0.
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
     tests/test_generation.py::test_matcher_selected_executable_surface
   ```

   Result: **88 passed in 5.65s**, Python **3.12.12**. The resource-layout test was excluded because it copies resources through `tmp_path`; no review file writes were performed.

6. No-bytecode in-memory Python probes using `PYTHONPATH=src`:
   - Independently replayed all five historical Code counterexamples.
   - Executed both examples successfully.
   - Replayed transient-provider rollback, commit, undo, begin and retained-scope completion attacks. Every attack was fenced; the original edit and pending value survived, the target remained unset and pure retry succeeded.
   - Exercised idle lazy begin/navigation attacks through default, current and working views. Every attack left the target unset, history unchanged and no transaction active; subsequent pure reads cached one shared value.
   - Reproduced P2-6 on both committed and provisional parents.
   - Confirmed eleven public marker factories are the exact Lifecycle objects, all five keyed operations default to `DEFAULT_TRANSACTION`, and nine package YIDL resources are discoverable.
7. Regenerator help, under the same source/no-bytecode environment, showed checking as the default and `--write` as the explicit mutation option. The permitted generation test independently confirmed generated-base equality.

No builds, installations, regeneration with writes, Git mutations, adjacent edits or additional agents were performed. The recorded Python 3.13/3.14 and isolated-wheel results were inspected but not independently repeated. No other current-round report was read.

## 1. Findings

### [P2-6] First thaw returns unprojected child facades, so nested working behavior changes on the second read

**Location:** `src/yidl_undoable/transaction_yidl.py:499–513`, particularly returning the raw converter result at lines 505 and 513. Subsequent touched reads apply recursive working projection at lines 478–487.

**Violated invariant:** Managed child relationships propagate the requesting parent’s view. A working parent must return working children on the first read as well as later reads. Repeated working access must preserve the owned container without changing the meaning of its child access solely because another parent read occurred.

The materialization path projects the converter’s input, invokes `thaw`, installs its returned value and returns it directly. A pure converter may return supported built-in containers containing ordinary/current handles. That result is not projected until the next field read.

**Reproduction:**

```python
from yidl_undoable import UndoRedoManager, managed, undoable

@undoable
class Child:
    items: tuple = managed(default=(), thaw=list, freeze=tuple)

@undoable
class Parent:
    children: tuple = managed(
        default=(),
        thaw=lambda children: [child.default for child in children],
        freeze=tuple,
    )

history = UndoRedoManager()
child = Child(transaction_manager=history)
parent = Parent(children=(child,), transaction_manager=history)
history.initialize(parent)

history.begin()
first = parent.working.children
assert first[0]._u_view == "default"

first[0].items.append("nested")
```

The nested edit raises:

```text
AttributeError: 'tuple' object has no attribute 'append'
```

Reading the same parent field again changes the result:

```python
second = parent.working.children
assert second is first
assert second[0]._u_view == "working"
second[0].items.append("nested")  # succeeds
history.commit()
assert parent.children[0].items == ("nested",)
```

The same failure and second-read success were independently reproduced with a parent constructed provisionally during the edit.

A converter returning `child.current` instead also exposes committed child data on the first working read and pending child data after the second read.

These converters create fresh lists, do not mutate their inputs, perform no transactional reentry and produce no external mutation. Their values use supported built-in containers and same-manager node references. The documented converter purity/separation contract does not prohibit returning ordinary/current handles; pending assignment and subsequent working reads already support projecting those handles.

**Impact:** The first nested working edit can fail, or read stale committed child data, while an identical second access succeeds. Applications must accidentally or deliberately prime the parent field to obtain its documented working semantics. The gap affects both established and provisional nodes.

**Required correction:** Recursively project the thaw result to the working view before installing or returning it, preserving the owned built-in working container where appropriate. Keep result traversal within the original operation fence and complete it before touched installation, so mapping callbacks or projection failure cannot install a partially accepted target.

**Closure/regression test:** Add canonical coverage for committed and provisional parents whose pure thaw returns a fresh list containing ordinary/current child handles. The very first working read must return working children, permit a nested thaw/edit and expose pending child data. Repeated access must return the same owned container; ordinary access must return default children without initiating untouched child thaws. Include nested dict/set containers. Add a narrow mapping-backed thaw-result attack that attempts completion during result projection: reject before mutation, retain the original token and pending edits, leave the parent target untouched and permit pure retry.

This is a bounded materialization/projection defect and does not require redesign.

## 2. Invariant analysis

The following attacks held outside P2-6:

- **Transaction-only managed mutability:** Idle, current and construction writes reject. Ordinary reads do not initiate thaw. Candidate managed reads through all views remain frozen and read-only.
- **Construction and providers:** Already-resolved private baselines are readable through all construction views. Named dependencies resolve in order; unresolved/recursive providers fail contextually. Named lazy providers materialize once and agree with self providers. Failed constructors register no partial node.
- **Lifecycle joins and scope ownership:** Nested begins join one token; inner commit publishes nothing; rollback closes the entire joined edit. Stale normal scopes reject, and stale exceptional scopes preserve the body exception without aborting replacement work.
- **Begin failure windows:** The permitted setup tests exercised partial backend acquisition, allocation, enlistment/binding failures, joined failures and abort failures. Confirmed closure allows clean retry without hidden nesting; incomplete or unexpected ownership faults detach editable state and reject future mutation/navigation.
- **Root graph integrity:** Shared children preserve identity; foreign edges and managed cycles reject. Working reachability is recomputed after escaped-container mutation. Empty final roots, provisional editing, omitted setup nodes, aborted handles, future-only handles and removed-node restoration pass.
- **Sparse history and branch trimming:** Negative predecessor lookup rejects. Branch publication trims untouched future field histories and node presence. Failed preparation and rollback preserve redo. Touch-only and empty successful edits still publish frames.
- **Absence and snapshots:** Strict absence raises. Last-visible descendants stay pinned to the fallback frame and read-only. Snapshots preserve aliases, frozenset node identity and abandoned branches while excluding nonmanaged fields and application methods.
- **Stable storage and atomic publication:** Mapping wrappers are copied to private immutable backing storage. Later-node freeze/validation failure installs no earlier value. Preparation builds a complete candidate before one selection assignment.
- **Nonversioned and transient policies:** Const references, plain fields, bindings, scratch stores and lazy results retain shared semantics. Candidate ordinary/working transient reads retain token-local values; current reads use baselines. Completion clears transient overlays, including removed nodes.
- **Callback originals:** Equality/truth completion attempts, transient navigation/completion, idle lazy begin/navigation, backing-map normalization, touched projection and corrected provisional projection reject reentry. Failed materialization remains retryable.
- **Fault evidence:** Confirmed installed history remains readable after cleanup faults. Unconfirmed selection blocks live managed reads and new snapshots; previously pinned snapshots remain readable.
- **Actual generation and recognition:** All nine inheritable concepts compile executable AST. Matchers select constructor forms, field kinds, binding shape, lazy mutability/factory behavior, transient factory behavior and managed view/thaw access. All eighteen canonical source comparisons and the checked-in base comparison passed. Annotation recognition uses the language API rather than raw class-dictionary assumptions.

The passing projection tests primarily exercise converter outputs that preserve their projected input handles, or values already installed through setters. They do not exercise a first thaw result containing a different supported facade view. This explains why the suite remains green while P2-6 is reproducible.

## 3. Risks and next action

P2-6 has a bounded correction within the accepted design. No architectural failure was established.

The next action is a test-led correction of first-thaw-result projection, followed by replay of P2-6 and all five historical Code counterexamples, then the existing acceptance gates.

Independent execution in this review is limited to Python 3.12.12 source behavior and read-only generation checks. The recorded three-version and isolated-wheel evidence applies to the pinned dependency tuple and was inspected, not repeated. Registry release, arbitrary older same-version dependency compatibility and the explicit persistence, concurrency, ownership and multi-key deferrals remain outside this verdict.

## 4. Surface

The cold first-day walkthrough identifies the package-root imports, decorator, required `transaction_manager=`, setup construction and explicit initialization. Manager-owned begin/commit/rollback/validate operations, exceptional rollback, undo/redo boundaries and branching are discoverable. Both executable examples pass.

Defaults are stated for the transaction key, strict absent policy, ordinary field interpretation and lazy mutability. Begin/completion, undo/redo and root add/remove form documented lifecycle pairs. Default/current/working handles, pinned snapshots, provisional absence, application-owned resources and the lack of fault recovery are explained together.

Installation requires the stated relative sibling-source development layout. The README does not provide a standalone dependency-cloning recipe, so that layout must be supplied by the workspace operator. This remains a local-draft documentation limitation; no registry installation or release is advertised.

No additional naming, default or lifecycle-pair defect was established. P2-6 is the remaining concrete surface contradiction: `parent.working.children` can return an ordinary/current child on its first read and a working child on its second.
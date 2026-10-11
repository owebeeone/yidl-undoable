# YIDL Undoable implementation — CODE + SURFACE-AXIS REVIEW

**Review object:** Complete `yidl_undoable` runtime package, tests, examples, generation resources, documentation and configuration at `72e1433e1290cc41392223c9d5981847e396f68e`; local implementation draft, runtime acceptance pending. Controlling design: `dev-docs/UndoableDesign.md`, accepted at `616f2f65473b1240535a6317d8cc79d5cec18414`.

**Baseline:**

| Repository | Pinned revision |
| --- | --- |
| `yidl_undoable` | `72e1433e1290cc41392223c9d5981847e396f68e` |
| `yidl-lifecycle` | `230362f642d6e9205897698670fe5f87d2c905ce` |
| `yidl` | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| `astichi` | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| `yidl-cache` | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Sources were read from the working tree. Read-only Git comparisons confirmed reviewed runtime files, tests, documentation, configuration and controlling records match `HEAD`. The design matches its accepted revision; the implementation plan matches `3440ec2fcee3a8d61c1f88cdfbafafc0683edabf`. Correction comparison: `a97e43e5010fd22a9bcd008f27072ca656b73f5b..72e1433e1290cc41392223c9d5981847e396f68e`. The complete tuple was verified at review start and end and did not move.

**Date:** 2026-10-12

**Axis:** Code architecture, interfaces, call graphs, composition and compatibility, plus the cold Python API surface. Independent, adversarial, read-only replacement review under Step 5.5. The other axis runs in parallel; nothing here relies on its current-round report. Filed verbatim by the lane owner.

**Verdict: NO-GO** — two new P2 findings block acceptance. All three original Code findings are closed. No P0, P1 or P3 findings. I pre-commit to GO on a revision that resolves P2-4 and P2-5 as specified.

---

## Prior-finding closure table

IDs in this table belong to the original Code report.

| ID | Disposition claimed | Verified on corrected tree | Status |
| --- | --- | --- | --- |
| Code P2-1 | Supply an explicit empty constructor-parameter contribution in the owning YIDL resource; regenerate the base. | Independently decorated and constructed empty, local-store-only, classvar-only and managed `init=False` declarations. Each signature is `(*, transaction_manager)`, with no dummy field. Initialization, commit and navigation succeeded. Canonical story 13 and deterministic generation checks also passed. | CLOSED |
| Code P2-2 | Recursively project exact built-in sets, preserving owned working-set identity and keeping ordinary projection separate. | Reran the original `frozenset`/`set` scenario: ordinary access after thaw returned a default child and did not touch its `value`; the owned set retained working children. Pending sets containing current/default handles projected to working children. Escaped-set mutation after commit did not change stored data. Canonical story 14 additionally exercised nested containers and current reads. | CLOSED |
| Code P2-3 | Materialize named lazy constructor providers through the existing fenced getter; reject unusable providers contextually. | Reran the original named-versus-self const provider comparison and the managed dependency variant. All received `7`, never `MISSING`; reversed declaration order and provisional construction worked. Factory calls remained one per instance across all views. Unset and recursive dependencies failed contextually without registration. Canonical story 15 and narrow diagnostic tests passed. | CLOSED |

These closures establish the original counterexamples. They do not close the separate provisional-baseline defects below.

## Changed-range analysis

The correction contains five runtime-module changes, one owning YIDL-resource change, regenerated base output, five new canonical stories and their goldens, narrow remediation tests, and documentation/evidence updates.

- `yidl/undoable_core.yidl` adds `EmptyParams`, its contribution, matcher and ordered constructor-boundary phase. The generated-base change corresponds to that resource change. Executable signatures and the regeneration check independently confirm the disposition.
- `values.py` adds exact built-in set admission and reconstruction/in-place replacement. Both original projection directions and nested-container coverage pass.
- `facades.py` adds `_u_constructor_provider`, routing unresolved named lazy providers through generated accessors. It also distinguishes candidate pins from historical pins for transient access. Named provider materialization, recursion diagnostics and candidate-transient canonical behavior pass.
- `transaction_yidl.py` adds failed-begin abort-evidence checks and unconditional overlay detachment, and restricts clean-discard completion to an unchanged selection. The narrow corrected fault tests pass; inspection confirms these changes implement the merged dispositions.
- `snapshots.py` changes node equality/hash to snapshot-context identity plus node ID. The new canonical frozenset/alias scenario passes.
- `docs/API.md` describes the corrected constructor, provider, candidate-transient, snapshot-identity and fault behavior.

No inspected runtime change establishes a new architectural root or falls outside the bounded remediation intent. The two new findings are retained defects exposed by extending the original view-propagation and callback-ownership attacks into provisional baseline reads. They are **bounded runtime root causes, not NEW ARCHITECTURAL root causes**.

## 0. Evidence base

Cold reading order was `README.md`, `docs/API.md`, then `examples/first_use.py` and `examples/nested.py`, before design, source or prior reports.

Subsequent inspection covered:

- Public generation architecture, exports, marker identities, packaging configuration and regeneration interface.
- `dev-docs/CurrentProgramCheckpoint.md`, `UndoableDesign.md`, `UndoableImplementationPlan.md`, the original `UndoableImplementation-ReviewCode.md`, and `UndoableImplementation-RemPlan.md`.
- TDD and independent verification records, treated as claims rather than runtime acceptance.
- `facades.py:1–328`, `transaction_yidl.py:1–633`, `values.py:1–133`, `undoable_harvester.py:1–132`, `undoable.py:1–76`, and callback, state, graph, history, snapshot and absence-policy mechanics.
- All nine YIDL resources and the changed generated-base ranges.
- Canonical scenario sources, especially construction/providers, callback fences, atomic validation, working projection, intermediate layers and remediation stories 13–17.
- Narrow generation, annotation-recognition, definition, history, state, fault, adversarial and remediation tests.
- Pinned Lifecycle provider-parameter recognition, terminal-completion records and token-bound scope callbacks.

Commands and observed results:

1. From the canonical workspace, `git -C <member> rev-parse HEAD` for all five members at both ends: all matched the exact tuple.
2. Read-only correction diff and implementation comparison. The correction spans 31 files including process records; the runtime/resource changes are those analyzed above.
3. `git diff --exit-code HEAD --` over reviewed runtime files, tests, public docs, examples, configuration and controlling records: exit 0.
4. Comparisons of the controlling design and implementation plan with their pinned revisions: exit 0.
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
     tests/test_generation.py::test_matcher_selected_executable_surface
   ```

   Result: **54 passed in 5.61s**, Python **3.12.12**. The resource-layout test was excluded because it copies files through `tmp_path`.

6. No-bytecode in-memory probes with `PYTHONPATH=src`:
   - Reran every original Code counterexample and confirmed the closure table.
   - Executed both examples successfully.
   - Confirmed all five keyed operations default to `DEFAULT_TRANSACTION`.
   - Confirmed eleven public marker factories are the exact Lifecycle factory objects and nine YIDL resources are discoverable.
   - Attacked transient-provider undo, explicit commit/rollback and retained scope completion. Each raised `ReentrantOperationError`, retained the original token, left the failed target unset and allowed a pure retry.
   - Reproduced both new findings below.
7. Regeneration help exposes checking as the default and `--write` as explicit mutation. The permitted generation test checked regenerated source against the checked-in base.

No writes, installations, builds, Git mutations, neighboring edits or additional agents were performed. Python 3.13/3.14 and isolated-wheel evidence was inspected, not independently repeated. No other current-round report was read.

## 1. Findings

### [P2-4] Provisional baseline reads preserve constructor child views instead of propagating the parent view

**Location:** `src/yidl_undoable/transaction_yidl.py:471–474`; `src/yidl_undoable/values.py:68–79`.

**Violated invariant:** A managed relationship propagates its parent’s view. Ordinary parents return ordinary children; working parents return working children. Provisional nodes are editable before attachment and must obey the same relationship semantics after construction.

The provisional branch calls `decode(state.values[name], ...)`. Constructor baselines contain application `RuntimeFacade` handles, whereas `decode` converts only internal `NodeRef` records. Consequently, an existing facade passes through unchanged.

**Reproduction:**

```python
from yidl_undoable import UndoRedoManager, managed, undoable

@undoable
class Node:
    value: tuple = managed(default=(), thaw=list, freeze=tuple)
    children: tuple = managed(default=())

history = UndoRedoManager()
child = Node(transaction_manager=history)
history.initialize(child)

history.begin()
child.working.value.append("pending")
parent = Node(
    children=(child.current,),
    transaction_manager=history,
)
history.add_root(parent)

assert parent.children[0]._u_view == "current"
assert parent.children[0].value == ()

parent.working.children[0].value.append("nested")
```

The last operation raises:

```text
AttributeError: 'tuple' object has no attribute 'append'
```

The original child’s working value is `["pending"]`, but both ordinary and working reads through the provisional parent return its current facade and committed `()`.

After publication, `parent.children[0]` becomes the default facade and exposes `("pending",)`. The relationship therefore changes view semantics solely because its parent crossed publication.

**Impact:** A provisional parent can expose stale committed child data during an edit and reject a nested working edit that the documented view contract permits. Supplying an ordinary child instead also fails to propagate the working view before publication.

**Required correction:** Project raw provisional constructor baselines recursively to the requesting facade’s view, including raw facade references within supported containers. Preserve ordinary reads’ no-thaw behavior and current provisional absence semantics. Perform application-backed container traversal under the callback fence.

**Closure/regression test:** Add canonical coverage creating a parent during an active transaction with existing ordinary/current child handles. Before and after attachment, assert ordinary children are default facades and working children are working facades, pending child values are visible through ordinary access, and a working child read thaws exactly as expected. Include nested containers and an untouched child field; retain current provisional absence checks.

This is a bounded view-projection defect, not an architectural failure.

### [P2-5] Provisional pre-thaw projection invokes mapping callbacks outside the operation fence

**Location:** `src/yidl_undoable/transaction_yidl.py:450–469`, specifically the unfenced provisional `project_working` call at lines 451–453; `values.py:98–105` invokes mapping iteration.

**Violated invariant:** Application callbacks during managed traversal/conversion must reject same-manager completion before changing state and retain the original operation’s token and overlay ownership. A suspended operation must not capture a fresh context after its original transaction has been aborted.

Already-touched projection is wrapped in `_call` at lines 439–448. The provisional pre-thaw projection is not. A `MappingProxyType` may invoke application code in its backing mapping before the later fenced thaw call begins.

**Reproduction:**

```python
from collections.abc import Mapping
from types import MappingProxyType
from yidl_undoable import UndoRedoManager, managed, undoable

class ProviderMap(Mapping):
    def __iter__(self):
        if attack[0]:
            attack[0] = False
            history.rollback()
        return iter(("value",))

    def __len__(self):
        return 1

    def __getitem__(self, key):
        return 1

@undoable
class Node:
    value: object = managed(
        default=MappingProxyType({}),
        thaw=dict,
        freeze=MappingProxyType,
    )

history = UndoRedoManager()
root = Node(transaction_manager=history)
history.initialize(root)

token = history.begin()
root.value = MappingProxyType({"pending": 9})
attack = [True]
child = Node(
    value=MappingProxyType(ProviderMap()),
    transaction_manager=history,
)

result = child.working.value
```

Observed:

```text
result: {'value': 1}
original token finalized: True
active transaction: None
root value: {}
frame count: 1
```

No `ReentrantOperationError` occurs. Reading the provisional working field aborts the original edit, discards the unrelated pending root change and still returns normally. The later `_call` captures healthy idle state, so it cannot detect that projection already lost the original transaction.

A variant that attempts rollback on every iteration raises a raw no-active-transaction error only after the first rollback has already succeeded.

**Impact:** A documented callback-fencing boundary can silently abort an edit and discard pending changes. This is the same admitted mapping-wrapper surface already covered by initial-normalization and pending-projection tests, reached through an uncovered provisional path.

**Required correction:** Fence provisional pre-thaw projection before invoking backing-map methods. Keep projection, thaw and touched-value installation bound to the original overlay/token; reject callback completion before mutation and install no target value when ownership is lost.

**Closure/regression test:** Add a narrow adversarial case using a provisional mapping-backed baseline. Its first iteration attempts rollback, then separately navigation and replacement begin. Each must raise `ReentrantOperationError`, preserve the original token and pending root change, and leave the provisional field untouched. Switch the callback to pure behavior and verify a successful retry under the same token. Exercise a retained scope-completion attempt as well.

This is a bounded missing callback fence, independent of P2-4’s raw-handle decoding defect. It does not require redesign.

## 2. Invariant analysis

The following attacks held outside the two identified provisional paths:

- **Construction and providers:** Complete nodes register only after successful construction. Unresolved/recursive self and named providers fail contextually. Named lazy dependencies now materialize once and agree with self-provider results.
- **Managed mutability:** Idle/current writes reject. Ordinary reads do not initiate thaw. Existing pending list/set projections propagate views and preserve owned working containers.
- **Lifecycle ownership:** Nested scopes join one token; inner commit does not publish; rollback closes the joined edit. Stale exceptional scopes preserve the body exception without aborting a replacement edit.
- **Graph integrity:** Alias identity, foreign-edge rejection, cycle rejection, final empty roots, unavailable omitted/aborted/future-only nodes and removed-node restoration remain covered by passing canonical scenarios.
- **Sparse history and epochs:** Negative predecessor lookup rejects. Branch publication trims untouched future histories and presence records. Failed final preparation and rollback preserve redo.
- **Absence and snapshots:** Last-visible descendants remain pinned. Snapshots preserve abandoned branches, nested aliases and node frozenset hashing while excluding application methods and nonmanaged fields.
- **Atomic publication:** Complete candidates are frozen and validated before one selection assignment. Later-node failures publish no earlier prepared data.
- **Nonversioned/transient policies:** Shared const/plain/binding/local/lazy behavior and transient completion cleanup pass. Candidate ordinary/working transient reads now retain active values while current reads retain baselines.
- **Callback originals:** Equality/truth rollback attacks, transient completion/navigation attempts, idle lazy begin/navigation, initial mapping normalization and already-touched mapping projection reject reentry. Failed targets remain retryable.
- **Fault evidence:** Corrected begin-abort and incomplete-publication tests pass, preserving confirmed readable history while rejecting further edits/navigation where evidence is incomplete.
- **Actual generation:** Nine inheritable concepts compile and execute real generated AST. Matchers select constructor, field kind, view/thaw, lazy policy, binding shape and transient-factory behavior. All seventeen canonical generated-source comparisons and the base check pass.

The provisional branch explains why these results coexist with the findings: committed values contain normalized `NodeRef` records, and touched values use fenced recursive projection. Untouched provisional constructor values use a separate raw-baseline path that lacks equivalent treatment.

## 3. Risks and next action

Both new findings have bounded corrections within the accepted runtime architecture. No architectural redesign is established.

The next action is one test-led correction of P2-4 and P2-5, followed by rerunning these exact counterexamples, retaining the three original closures, and repeating the existing acceptance gates.

Residual verification limits are Python 3.12 source execution and read-only generation checks. The recorded three-version and isolated-wheel results were inspected but not repeated. Public registry release, compatibility with arbitrary older same-version dependency wheels, persistence, concurrency and other explicit deferrals remain outside this verdict.

## 4. Surface

The cold first-day walkthrough identifies package-root imports, the decorator, required `transaction_manager=`, explicit initialization, manager-owned begin/completion, exceptional rollback, undo/redo boundaries and branching behavior without requiring source inspection. Both examples execute successfully.

Defaults are stated for the manager key, strict absence policy, lazy mutability and field interpretation. Begin/commit/rollback, undo/redo, root add/remove and live views/snapshots have discoverable lifecycle relationships. Fault recovery limits and application-owned resources are explicit.

The installation instructions require the stated relative sibling-source development layout. They do not give a standalone dependency-cloning recipe; this remains a local-draft documentation limitation rather than a broken advertised registry installation.

The remaining shipped surface contradictions are P2-4 and P2-5: provisional nested working access can return a current child, and a managed read can permit the very same-manager completion the callback contract promises to reject. No additional naming, default or lifecycle-pair finding was established.
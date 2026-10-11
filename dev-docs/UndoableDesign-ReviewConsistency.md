# YIDL Undoable Design — CONSISTENCY-AXIS REVIEW

**Review object:** `README.md` and `dev-docs/UndoableDesign.md` at `dbd89160ed54d6bab5887ee43bb75c4217459d21`. Controlling design status: DRAFT, 2026-10-12. Design-stage API review only.

**Baseline:**

| Repository | Revision |
| --- | --- |
| `yidl_undoable` | `dbd89160ed54d6bab5887ee43bb75c4217459d21` |
| `yidl-lifecycle` | `230362f642d6e9205897698670fe5f87d2c905ce` |
| `yidl` | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| `astichi` | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| `yidl-cache` | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Object and source evidence were read using `git show SHA:PATH`. Every listed HEAD matched this tuple at both the start and end of review.

**Date:** 2026-10-12

**Axis:** Consistency against the controlling document graph, including the required cold Surface walkthrough. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: NO-GO** — one P2 finding blocks; two P3 documentation findings remain. I pre-commit to GO on a revision that resolves P2-1 as specified.

---

## 0. Evidence base

The Surface review began with `README.md`, lines 1–52, before reading the design or implementation evidence.

The following controlling documents and source evidence were inspected:

- `dev-docs/UndoableDesign.md`, sections 1–15, lines 1–734.
- `dev-docs/CurrentProgramCheckpoint.md`, lines 1–55.
- `../yidl-lifecycle/docs/ManagedContextApiDraft.md`, especially transaction completion, live views, aggregate editing, and initialization lifetimes.
- `../yidl-lifecycle/dev-docs/TransactionScopeOwnership.md`, including stale scopes, callback fencing, terminal completion evidence, and candidate-write boundaries.
- `../yidl-lifecycle/dev-docs/YidlLifecycleFieldKindMatrix.md` and `dev-docs/README.md`.
- `../yidl-lifecycle/src/yidl_lifecycle/lifecycle_markers.py`, including marker defaults, normalized declarations, supported factories, and method markers.
- `../yidl-lifecycle/src/yidl_lifecycle/lifecycle_harvester.py`, especially declaration harvesting, factory arguments, binding shape, inherited metadata, and override validation.
- `../yidl-lifecycle/src/yidl_lifecycle/transaction_yidl.py`, including `LifecycleTransaction`, completion sessions, `GroupTransactionManager`, enlistment, nested completion, and scope callbacks.
- `../yidl-lifecycle/src/yidl_lifecycle/lifecycle.py`, targeted decorator-generation and builder-binding evidence.
- `../yidl-lifecycle/src/yidl_lifecycle/yidl/lifecycle_core.yidl`, `lifecycle_managed.yidl`, `lifecycle_default_factories.yidl`, `lifecycle_transient.yidl`, `lifecycle_owned.yidl`, `lifecycle_local_store.yidl`, and `lifecycle_base.yidl`, targeted field, factory, matcher, and composition evidence.
- `../yidl/dev-docs/YidlDesignSummary.md`, targeted generator, matcher, contribution, and compiler-boundary sections; `dev-docs/YidlCodingRules.md`.
- `../astichi/dev-docs/AstichiSingleSourceSummary.md`, targeted current surface and composition contracts; `dev-docs/AstichiCodingRules.md`.
- `../yidl-cache/README.md`, for the compiled-code consumer boundary.

Workspace instructions and applicable member `AGENTS.md` files were read. No member-level `AGENTS.md` exists in `yidl_undoable`.

Inspection used `pwd`, `cat`, `rg`, `sed`, pinned `git show`, `git rev-parse HEAD`, and read-only Python inspection. Python parsed the README and design Python examples successfully with `ast.parse`; the examples were not executed. No tests, builds, edits, Git mutations, or current-round reports from another reviewer were inspected.

## 1. Findings

### [P2-1] Constructor factory reuse lacks a managed-read contract before initial publication

**Location:** `dev-docs/UndoableDesign.md`, lines 174–181, 197–202, 248–260, and 270–272. Supporting source: `../yidl-lifecycle/src/yidl_lifecycle/yidl/lifecycle_default_factories.yidl`, lines 438–471 and 688–696.

**Violated invariant:** Supported construction factories must be able to obtain their declared providers without requiring a committed frame that construction precedes.

The design promises Lifecycle factory-provider behavior, including `allow_self_factory`. However, its general ordinary-view rule resolves committed values when no transaction is active. Setup construction has no active transaction, and frame zero does not exist until `initialize()`. The provisional-baseline traversal exception is specified during editing, not during setup construction.

A supported declaration exposes the gap:

```python
@undoable
class Counter:
    seed: int = managed(default=3)
    total: int = managed(
        default_factory=lambda self: self.seed + 1,
        allow_self_factory=True,
    )


history = UndoRedoManager()
counter = Counter(transaction_manager=history)
history.initialize(counter)
```

The state sequence is:

1. `history` is in setup.
2. Construction resolves `seed` into an unpublished constructor baseline.
3. The `total` factory receives the ordinary facade and reads `self.seed`.
4. No transaction is active, so the documented ordinary-view rule requires a committed value.
5. There is no selected committed frame.

The document supplies no defined result for step 4. Returning the constructor baseline requires an exception to the stated view rule; rejecting the read breaks the promised factory support.

This affects named field providers too if Lifecycle’s generation pattern is reused directly: `DefaultFactoryStoredArg` obtains a provider through `self.<provider>`, while `DefaultFactorySelfArg` passes the facade itself. It is therefore more than an unusual callback pattern.

**Impact:** Constructor-factory parity cannot be implemented against the written contract without adding an undocumented read mode or restricting an advertised feature. The broad “factories/provider dependencies” acceptance fixture does not settle this lifetime boundary.

**Required correction:** Define construction-time managed reads explicitly. State which facade or provider path sees already-resolved unpublished constructor baselines, how unresolved providers fail, and how this applies both to setup nodes and transaction-created provisional nodes. Preserve the rule that construction does not publish history or enable ordinary managed editing.

**Closure/regression test:** Add canonical generated-source coverage for:

- A setup node whose opt-in self factory reads an already-resolved managed field.
- A named factory provider referring to a managed field.
- The same declarations on a provisional node created during editing.
- An unresolved/self-referential provider producing a contextual diagnostic.
- Frame zero containing the resulting values, with no earlier publication.

**Root-cause classification:** An incomplete lifecycle boundary between constructor baselines and published-frame resolution. This is a bounded contract correction; the evidence does not establish that the aggregate-participant or immutable-epoch architecture must be replaced.

### [P3-1] The first-use page omits the default field-kind policy

**Location:** `README.md`, lines 3–5 and 17–52; controlling policy in `dev-docs/UndoableDesign.md`, lines 142–155.

**Violated invariant:** A first-use surface must state whether an ordinary annotated field participates in undo.

The README demonstrates explicit `managed`, `const`, and `local_store` declarations, but never states what an unmarked annotation means. The detailed design specifies that it becomes a plain, nontransactional `field`.

A reader extending the example can reasonably write:

```python
@undoable
class Document:
    count: int = 0
```

Then initialize, assign `count` during an edit, commit, and undo. Under the controlling design, `count` survives undo and rollback. The README supplies no rule from which the reader can predict that result.

**Impact:** Users can place model data outside history unintentionally. The desired semantics already exist in the controlling document, so this is a documentation correction rather than a required compatibility change.

**Required correction:** State on the first-use page that unmarked annotated fields are plain and nontransactional, and that reversible model data requires `managed`. Make the sentence cover rollback as well as undo.

**Closure test:** Repeat the cold walkthrough with an unmarked scalar beside a managed scalar. The reader should be able to predict both results from the README alone; canonical implementation coverage should demonstrate the distinction.

### [P3-2] The first-use page provides no nested-object inspection path

**Location:** `README.md`, lines 17–52; controlling topology and view contracts in `dev-docs/UndoableDesign.md`, lines 204–215 and 262–280.

**Violated invariant:** The required first-day walkthrough must let the reader inspect nested objects and identify which relationships belong to history.

The README’s collection contains strings. It gives no nested-node example and does not introduce `.current`, propagated child views, or the distinction between managed and nonversioned node relationships.

After the documented scalar/collection walkthrough, a reader adding a child must guess:

- Whether an ordinary node-valued attribute establishes historical membership.
- How to inspect the committed child while an edit is active.
- Whether `parent.current.child` and `parent.working.child` preserve their respective views.

The detailed design answers these questions, but the first-use page does not.

**Impact:** The user cannot complete the specified nested-object walkthrough from this page, and may place topology in a nonversioned field.

**Required correction:** Add a compact nested-node example with a managed relationship and committed versus working child reads. State that child views propagate and nonversioned references do not establish historical membership.

**Closure test:** A cold reader should be able to initialize a parent/child graph, edit the child, inspect its committed value during editing, commit, undo, and redo without inventing an accessor or relationship policy.

## 2. Invariant analysis

### Surface walkthrough

Initialization, editing, explicit abort, explicit commit, undo, and redo are discoverable in the README. The distinction between rollback of a pending edit and undo of a committed frame is stated. Context-manager completion is described, although its syntax is demonstrated only in the detailed design.

The completion pairs are coherent:

- `begin` is completed by `commit` or `rollback`.
- `undo` is paired with `redo`.
- `add_root` is paired with `remove_root`.
- Setup publication is deliberately one-time; no misleading reset/uninitialize placeholder is proposed.

The detailed manager table states the default transaction key and default absence policy. Its custom-key instructions agree with the keyed backend interface. No implemented CLI or importable package was expected or tested.

The cold walkthrough fails at field-kind defaults and nested inspection as recorded above.

### Transaction ownership and publication

The proposed composition is feasible against the pinned Lifecycle runtime. `GroupTransactionManager` accepts participant callbacks matching the aggregate’s proposed shape. Exactly one aggregate participant avoids per-node application ordering and partial per-node publication.

Nested commits decrement the begin count without final completion. Rollback closes the joined transaction. Token-bound stale scope behavior agrees with `TransactionScopeOwnership.md`. The proposed manager-owned completion surface is an explicit Undoable narrowing, not a contradiction with Lifecycle’s model convenience methods.

The aggregate’s `requires_validation_for=False` is coherent because final candidate validation occurs in preparation. Public Undoable `validate()` must invoke that preparation path rather than delegate to the backend’s validator-only operation; the design explicitly requires this.

Terminal evidence and installed-selection identity are used together. This correctly avoids interpreting an exception as proof that publication did not happen.

### History, topology, and snapshots

The sparse predecessor algorithm excludes negative-index fallback. Branch truncation explicitly removes future versions from untouched fields and presence histories. Failed preparation and rollback preserve redo.

Immutable epochs allow retained snapshots to read abandoned history without reactivating it. Snapshot membership and managed-field-only access are separately defined, avoiding a claim that management resources rewind.

Shared child identity, final-graph membership, cross-manager rejection, and cycle rejection are coherent. Last-visible descendants are pinned to the fallback frame, which closes the historical-parent/current-child mixture.

Working membership is recomputed after escaped mutable containers may change. Touched values on previously present nodes ending unreachable are deliberately excluded from publication. Provisional and future-only handles have separate availability rules.

### Generation and dependency boundaries

The feature-layer chain, matcher-selected contributions, stable ordering, and plain generated classes agree with the relevant YIDL/Astichi mechanisms. The design does not require a handwritten wrapper to stand in for generated behavior.

The harvester reuse proposal explicitly preserves Undoable’s own inheritance metadata instead of passing generated Undoable bases into Lifecycle’s inheritance lookup. The package-resource reuse fallback avoids assuming private checkout paths are distributable.

The cache is correctly treated as a transitive dependency, without claiming an Undoable cache adapter exists.

### Evidence and scope

The checkpoint agrees with the design’s ordering: design acceptance precedes the separate TDD implementation plan, and runtime acceptance requires its own checks and review. The planned verification gates are prospective, not fabricated execution evidence.

The listed deferrals were treated as scope decisions. No finding is based on missing disk persistence, multi-key histories, resource ownership, hooks, arbitrary custom managed values, or multiple generated bases.

## 3. Risks and next action

This review establishes document consistency and source-level reuse feasibility only. It does not certify converter isolation, cleanup reliability, generated output, wheel contents, or runtime parity.

The next action is one bounded remediation patch defining construction-time managed-provider reads and repairing the README’s first-use omissions, followed by review of that settled revision. Resolve P2-1 before entering implementation planning.
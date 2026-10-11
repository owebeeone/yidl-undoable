# YIDL Undoable Design — CONSISTENCY-AXIS REVIEW

**Review object:** `README.md` and `dev-docs/UndoableDesign.md` at `14de6f98cf2aca81d24acd3e20a959cdf795498f`. Controlling design status: DRAFT, dated 2026-10-12. Design-stage API review only.

**Baseline:**

| Repository | Revision |
| --- | --- |
| `yidl_undoable` | `14de6f98cf2aca81d24acd3e20a959cdf795498f` |
| `yidl-lifecycle` | `230362f642d6e9205897698670fe5f87d2c905ce` |
| `yidl` | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| `astichi` | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| `yidl-cache` | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Object bytes and substantive source evidence were read using `git show SHA:PATH`. Every listed HEAD matched this tuple at the start and end of review.

**Date:** 2026-10-12

**Axis:** Consistency against the controlling document graph, including the required cold Surface walkthrough. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: GO** — no open P0, P1, P2, or P3 findings on this axis. The three original Consistency findings close at the design-contract level. This verdict does not certify implementation or close another axis’s findings.

---

## Prior-finding closure table

| Prior finding | Independent counterexample retrace | Disposition |
| --- | --- | --- |
| P2-1 — Constructor factory reuse lacks a managed-read contract before initial publication | With `seed = managed(default=3)` and an opt-in self factory computing `self.seed + 1`, corrected section 5 directs the factory’s read to the already-resolved private constructor baseline, yielding `4` without consulting a committed frame. Named providers use the same table in dependency order. Both rules explicitly apply to setup and provisional construction. Unresolved/self-recursive reads fail contextually; failed construction registers no partially initialized node or published value. Section 13 now requires canonical coverage of these cases. | **Closed for design.** `dev-docs/UndoableDesign.md:217–236`, `710–712`. Runtime evidence remains an implementation gate. |
| P3-1 — First-use page omits the default field-kind policy | Repeat the original unmarked `count: int = 0` example beside a managed scalar. The README now explicitly predicts that the unmarked field is plain and survives rollback and undo, whereas reversible data must use `managed`. This agrees with the detailed field-policy table. | **Closed.** `README.md:17–19`; `dev-docs/UndoableDesign.md:142–155`. |
| P3-2 — First-use page provides no nested-object inspection path | Follow the new parent/child example: create both nodes with the same manager, initialize the parent, mutate through `parent.working.children[0]`, inspect the old label through `parent.current.children[0]`, complete the context, undo, and redo. Every accessor and relationship policy needed for this sequence is present on the page. | **Closed.** `README.md`, “Nested objects and committed reads”; `dev-docs/UndoableDesign.md:204–209`, `283–304`. |

Closure was determined from the corrected contract and the original sequences, not from the remediation plan’s claimed dispositions.

## Changed-range analysis

The object comparison against `dbd89160ed54d6bab5887ee43bb75c4217459d21` was computed with read-only Python using pinned Git objects.

- **README:** Added the unmarked-field policy and a managed nested relationship walkthrough. The added example agrees with current/working propagation, manager-owned completion, and undo/redo selection.
- **Construction reads, design lines 217–236:** Added an explicit precedence rule for private constructor baselines, provider ordering, recursive-provider failure, registration timing, and setup reads before initialization. The exception is bounded to construction/setup lifetimes and does not permit managed editing or publication before initialization.
- **Application callbacks, design lines 352–375:** Extended operation ownership to comparison, truth conversion, and factories as well as conversion and validation. Provider materialization and nested construction have explicit allowances under the original context; generated managed/transient writes and transaction replacement remain fenced.
- **Scope callbacks, design lines 460–466:** Specified guarded rebinding through the existing `LifecycleTransaction.bind_scope` surface while preserving the original token-bound backend callbacks. The pinned source supports this composition.
- **Verification, design lines 701–704 and 710–712:** Added concrete callback and construction-provider cases to canonical coverage. These are prospective implementation obligations, not claims of executed tests.

The full corrected contract was reviewed beyond these ranges. No new architectural root cause was established.

## 0. Evidence base

The Surface review began with the pinned `README.md`, before reading the design, remediation plan, prior report, or executable source.

The following evidence was inspected:

- `README.md`, complete proposed first-use surface.
- `dev-docs/UndoableDesign.md`, complete document, lines 1–791.
- `dev-docs/CurrentProgramCheckpoint.md`, complete directive, review state, and operator override.
- `dev-docs/UndoableDesign-ReviewConsistency.md`, complete prior Consistency report.
- `dev-docs/UndoableDesign-RemPlan-1.md`, complete merged remediation plan.
- `../yidl-lifecycle/docs/ManagedContextApiDraft.md`, complete transaction, view, aggregate-editing, initialization, and proposed-alias guide.
- `../yidl-lifecycle/dev-docs/TransactionScopeOwnership.md`, complete ownership, stale-scope, completion-evidence, and candidate-write contract.
- `../yidl-lifecycle/dev-docs/YidlLifecycleFieldKindMatrix.md` and `dev-docs/README.md`.
- `../yidl-lifecycle/src/yidl_lifecycle/transaction_yidl.py`, targeted participant interface, token scope binding, `GroupTransactionManager`, nesting, validation, completion, and enlistment evidence: lines 1–57, 176–301, and 596–884.
- `../yidl-lifecycle/src/yidl_lifecycle/lifecycle_markers.py`, targeted declaration defaults and normalization: lines 1–60, 124–194, and 239–386.
- `../yidl-lifecycle/src/yidl_lifecycle/lifecycle_harvester.py`, targeted declaration harvesting, factory facts, transaction metadata, inheritance, override checks, and reserved names: lines 1–144, 205–274, 413–444, 537–631, and 678–708.
- `../yidl-lifecycle/src/yidl_lifecycle/lifecycle.py`, generated AST assembly and runtime-value binding: lines 40–133 and 184–187.
- `../yidl-lifecycle/src/yidl_lifecycle/yidl/lifecycle_default_factories.yidl`, dependency ordering, provider diagnostics, self/stored arguments, and matcher contributions: lines 100–255, 438–471, and 644–711.
- `../yidl-lifecycle/src/yidl_lifecycle/yidl/lifecycle_transient.yidl`, baseline fallback, working factory injection, clearing, and matcher-selected behavior: lines 201–330, 421–444, and 715–778.
- `../yidl-lifecycle/src/yidl_lifecycle/yidl/lifecycle_core.yidl`, declaration facts, lines 1–73; `lifecycle_base.yidl`, complete final assembly.
- `../yidl/dev-docs/YidlDesignSummary.md`, targeted compiler boundary, generation-data substrate, matcher/production rules, parser boundary, and recorded concept composition: sections 26–27 and decision-ledger entries 55–58.
- `../yidl/dev-docs/YidlCodingRules.md`.
- `../astichi/dev-docs/AstichiSingleSourceSummary.md`, targeted governing composition, executable AST, hygiene, and public builder contracts.
- `../astichi/dev-docs/AstichiCodingRules.md`, targeted surface, layering, additive composition, and ownership rules.
- `../yidl-cache/README.md`, compiled-code and consumer ownership boundary.

Workspace `AGENTS.md`, `AGENTS_GWZ.md`, and applicable member `AGENTS.md` files were read. No member-level `AGENTS.md` was found in `yidl_undoable`.

Inspection used `cat`, `rg`, pinned `git show`, `git log -n 3`, `git rev-parse HEAD`, and read-only Python. Python successfully parsed both README Python examples and the design Python example with `ast.parse`; none was executed. The comparison used `difflib` in memory.

No files were written, no builds or tests were run, and no Git state was mutated. No other current-round reviewer prompt or report was inspected.

## 2. Invariant analysis

### Surface walkthrough

The README now supplies a complete conceptual first-day path:

1. Declare reversible fields using `managed`.
2. Construct a manager and nodes using `transaction_manager=`.
3. Publish frame zero with `initialize`.
4. Begin an edit and request mutable collection access through `.working`.
5. Abort with `rollback` on failure or complete with `commit`.
6. Undo and redo committed frames.
7. Inspect nested committed and pending values through propagated `.current` and `.working` views.

The context-manager example demonstrates automatic successful completion; the preceding example demonstrates explicit completion and abort. The page explains that rollback discards a pending edit while undo selects an earlier committed frame.

The former guesses about unmarked annotations and nested relationships have been eliminated. The page also explicitly limits reversal to managed model data and excludes caches, file descriptors, external resources, and side effects.

Lifecycle pairs are coherent: begin/commit-or-rollback, undo/redo, and add-root/remove-root. One-time initialization does not advertise an incomplete reset lifecycle. The manager table states the transaction-key and absence-policy defaults; custom-key calls are explicitly described. Reused marker defaults are fixed by the pinned marker factories, including value comparison, constructor participation, opt-in self factories, and write-once lazy storage.

No installed CLI or importable package was assumed. The README clearly labels the API as proposed.

### Construction and factory providers

The original setup counterexample no longer reaches committed-frame lookup. The construction context precedes ordinary view resolution and exposes resolved private baselines through default/current/working facades. Named providers use that same table rather than needing a published history.

The provisional counterpart also holds: construction occurs under an active edit, but provider reads use the new node’s private constructor context. After successful construction, provisional traversal uses its baseline until attachment and publication. No current-frame membership is created merely by construction.

The unresolved/self-recursive case has a specified contextual failure and registration boundary. The new canonical obligations distinguish successful provider resolution from failure diagnostics.

These provisions can be implemented using the inspected Lifecycle dependency facts and argument contribution patterns, while replacing their value-resolution path with Undoable’s construction context. Direct reuse of Lifecycle historical slots is neither required nor claimed.

### Transaction composition and callbacks

The proposed aggregate matches the pinned participant callback interface. Enlisting exactly one `HistoryParticipant` gives the backend one preparation/application boundary for the entire graph.

Nested begins return the joined token, inner successful completion decrements the count, and rollback closes the whole edit. Guarded `bind_scope` rebinding is feasible against the existing method and preserves stale-token ordinary and exceptional exit behavior.

The expanded callback contract is consistent with those semantics. A comparison or working factory cannot complete or replace the transaction through an explicit manager call or retained scope exit. After callback return, the suspended operation must verify its original ownership before installing a result; it cannot continue under a newly acquired token.

Read-only provider materialization and controlled nested construction are explicit exceptions within the original context. They do not authorize transaction completion or generated managed writes. This avoids making ordinary provider-based factories impossible merely because they invoke another provider.

Returning false from `requires_validation_for` remains coherent: the aggregate validates the frozen candidate during preparation. Public Undoable `validate()` explicitly uses that preparation path, rather than relying on the backend’s validator-only method. A preview does not certify later changes.

### Publication and failure evidence

Preparation builds a replacement immutable selection without altering published history. Application consists of one selection-reference installation, with no converter or validator running at that point.

A later cleanup failure is not described as an unpublished rollback. Terminal token evidence and installed-selection identity determine what happened; uncertain ownership or cleanup enters faulted state. This agrees with the adjacent completion-evidence contract.

Expected callback failures leave no new target-field result and preserve earlier valid overlays for repair or rollback. Failed outer preparation aborts the edit and preserves the prior selection and redo tail. Preview failure keeps the edit active.

### History, absence, topology, and snapshots

The predecessor rule explicitly rejects negative-index fallback. Branch truncation trims every field and presence history, including untouched fields, so an abandoned future value cannot become the predecessor on the new branch.

Frame IDs remain monotonic while cursor positions remain contiguous. This keeps predecessor ordering and last-visible resolution coherent after branching.

Managed topology preserves shared node identity, rejects foreign-manager edges and final cycles, and uses final reachability for publication. Removing one path does not make a child absent while another rooted path remains. Recomputing working membership accounts for escaped mutable containers.

Last-visible reads select a surviving prior presence frame and pin descendants to it. They cannot combine a historical parent with current children or resurrect a node solely from abandoned/aborted history.

Snapshots retain immutable epochs and expose managed data only. They remain readable after branch truncation without reactivating abandoned live nodes. Nonversioned management storage is consistently excluded from historical guarantees.

### Generation, packaging, and controlling scope

The feature chain, matcher-selected field behavior, stable contribution ordering, and plain generated classes agree with the inspected YIDL/Astichi mechanisms. The design preserves ownership boundaries between history semantics and compiler assembly.

Harvester adaptation explicitly retains Undoable inheritance metadata instead of relying on Lifecycle’s generated-base metadata. Resource reuse has a wheel-safe lookup requirement and an Undoable-owned fallback, so source-checkout paths are not assumed to be distributable dependencies.

The cache remains a transitive dependency without an invented Undoable cache integration. Minimum-version compatibility, generated resources, regeneration, wheel smoke checks, and runtime review are explicit future gates.

The checkpoint and design agree that design acceptance precedes a separate TDD implementation plan. Their superseded background clauses agree on one-root scope, illustrative names, and nested begins. The background concept was not treated as competing authority or included in the review object.

Explicit deferrals were treated as scope outcomes. No finding is based on absent persistence, retention, collaboration, multi-key history, owned resources, hooks, custom stable adapters, or multiple generated bases.

## 3. Risks and next action

This GO accepts a coherent design contract and source-level reuse approach. Converter isolation, callback enforcement, candidate preparation, cleanup, generated inheritance, and installed-wheel behavior remain unproved until implementation.

The next action is to carry the specified canonical counterexamples and failure checks into the separate red/green/refactor implementation plan, subject to the independent dual design gate. No additional Consistency remediation is required at this tuple.
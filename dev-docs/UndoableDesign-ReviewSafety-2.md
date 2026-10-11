# YIDL Undoable Design — SAFETY-AXIS REVIEW

**Review object:** `yidl_undoable` README.md and dev-docs/UndoableDesign.md at `14de6f98cf2aca81d24acd3e20a959cdf795498f`. Controlling design status: DRAFT, dated 2026-10-12. Design-stage API review only.

**Baseline:**

| Repository | Revision |
| --- | --- |
| `yidl_undoable` | `14de6f98cf2aca81d24acd3e20a959cdf795498f` |
| `yidl-lifecycle` | `230362f642d6e9205897698670fe5f87d2c905ce` |
| `yidl` | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| `astichi` | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| `yidl-cache` | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Object and supporting source bytes were read with `git show SHA:PATH`. All five HEADs matched this tuple at the start and end.

**Date:** 2026-10-12

**Axis:** Safety — attack callback ownership, publication, recovery, historical isolation, degraded paths, and compatibility. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: NO-GO** — original P2-1 is closed at the design-contract level; one new P2 finding blocks. I pre-commit to GO on a revision that resolves P2-2 as specified.

---

## Prior-finding closure table

| Prior finding | Independent retrace | Disposition |
| --- | --- | --- |
| Safety P2-1: comparison callback replaces its initiating transaction | Under transaction T and overlay O, equality attempts rollback followed by replacement begin. Revised section 7 fences both calls before lifecycle mutation, includes comparison-result truth conversion, and requires verification of T/O before installing a result. Swallowing the rejected reentry does not authorize replacement; propagating it installs no target result. | Closed in the written contract. |
| Safety P2-1: transient working factory completes its transaction before installing its result | Revised section 7 includes working factories. Completion through explicit manager methods is fenced. Revised section 10 requires retained token scope callbacks to check that same fence before delegating to the original token-bound backend callbacks. Completion therefore cannot clean up T and then allow the suspended factory to install its result afterward. | Closed in the written contract. |

The pinned Lifecycle implementation provides `LifecycleTransaction.bind_scope` at src/yidl_lifecycle/transaction_yidl.py, lines 272–280, so the required guarded binding is feasible without replacing its token-bound scope semantics.

Canonical coverage for equality/truth conversion, transient factory completion, and retained scope exits is explicitly required by the revised design, lines 701–704. These are implementation obligations, not tests executed during this document review.

## Changed-range analysis

The committed comparison against the prior reviewed revision, `dbd89160ed54d6bab5887ee43bb75c4217459d21`, established these substantive changes:

| Revised location in `yidl_undoable` | Safety analysis |
| --- | --- |
| dev-docs/UndoableDesign.md, lines 217–236 | Construction reads use resolved private baselines without enabling managed writes or publication. Unresolved and recursive reads fail contextually; successful registration requires a complete node. |
| dev-docs/UndoableDesign.md, lines 352–375 | Operation-owned callback fencing closes the original comparison and working-factory sequences. Its extension to lazy factories introduces P2-2: the required post-call state excludes a documented healthy-idle operation. |
| dev-docs/UndoableDesign.md, lines 460–466 | Guarded scope rebinding closes the retained-token scope-exit bypass while preserving original token ownership and stale-scope behavior. |
| dev-docs/UndoableDesign.md, lines 701–712 | Adds explicit adversarial callback coverage and construction-provider coverage to the canonical implementation obligations. |
| README.md, “Proposed first use” and “Nested objects and committed reads” | Clarifies nontransactional defaults and managed topology. The walkthrough consistently separates current child reads from working child edits. |

The new finding is a bounded contract correction. No **NEW ARCHITECTURAL** root cause was established.

## 0. Evidence base

Read workspace AGENTS.md and AGENTS_GWZ.md, plus applicable member AGENTS.md files in `yidl-lifecycle`, `yidl`, `astichi`, and `yidl-cache`. No member AGENTS.md was found in `yidl_undoable`.

Reviewed the pinned object and legitimate prior-round inputs:

- `yidl_undoable`: README.md in full.
- `yidl_undoable`: dev-docs/UndoableDesign.md, sections 1–15, with numbered inspection of field policies, construction, callbacks, histories, snapshots, publication, failure states, and verification requirements.
- `yidl_undoable`: dev-docs/CurrentProgramCheckpoint.md.
- `yidl_undoable`: dev-docs/UndoableDesign-ReviewSafety.md.
- `yidl_undoable`: dev-docs/UndoableDesign-RemPlan-1.md.
- Read-only Python `difflib` comparison of the two committed README and design revisions.

Inspected supporting evidence at the pinned Lifecycle revision:

- docs/ManagedContextApiDraft.md and dev-docs/TransactionScopeOwnership.md in full.
- dev-docs/README.md.
- src/yidl_lifecycle/transaction_yidl.py, lines 1–320 and 330–810: scope binding, token ownership, participant capture, completion fencing, application/discard ordering, finalization, and completion evidence.
- src/yidl_lifecycle/lifecycle_markers.py, lines 1–385: supported factories, marker defaults, comparison options, and normalized declarations.
- src/yidl_lifecycle/lifecycle_harvester.py, lines 44–189, 436–498, 548–627, and 669–711: normalized facts, factory signatures, inheritance restrictions, and reserved names.
- src/yidl_lifecycle/lifecycle.py, lines 1–200: generation, executable AST, builder binding, and supported field layers.
- src/yidl_lifecycle/yidl/lifecycle_core.yidl, lines 410–490.
- src/yidl_lifecycle/yidl/lifecycle_managed.yidl, lines 205–390.
- src/yidl_lifecycle/yidl/lifecycle_transient.yidl, lines 185–310.
- src/yidl_lifecycle/yidl/lifecycle_default_factories.yidl, lines 1–210.
- src/yidl_lifecycle/yidl/lifecycle_const_static.yidl, especially lines 99–128.
- src/yidl_lifecycle/yidl/lifecycle_base.yidl and pyproject.toml.

Selected generation-boundary evidence was also inspected in:

- `astichi`: dev-docs/AstichiSingleSourceSummary.md, current snapshot, governing rules, executable-AST guidance, and selected public compile/build surface; dev-docs/AstichiCodingRules.md.
- `yidl`: dev-docs/YidlDesignSummary.md, lines 1–90.

Only inspection commands were used. No writes, tests, builds, or Git mutations occurred. No other current-round reviewer prompt or report was inspected.

## 1. Findings

### [P2-2] Callback postconditions exclude permitted idle lazy initialization

**Location:** `yidl_undoable`: dev-docs/UndoableDesign.md, lines 354–357 and 369–375, conflicting with lines 147 and 174–180. The distinct healthy-idle state is specified at lines 518–519.

**Root cause:** The expanded callback contract includes lazy factories, but its installation postcondition admits only “editable/construction state.” A lazy factory can legitimately run after initialization while the manager is healthy idle. That operation has neither an editable transaction nor a construction context.

This is a new bounded contract root, not an architectural failure.

**Violated invariant:** Documented nonversioned first-read initialization must remain available through an idle current facade without requiring a transaction. Callback ownership checks must preserve the operation’s actual permitted context.

**Credible state sequence:**

```python
@undoable
class Document:
    value: int = managed(default=0)
    memo: dict[str, int] = lazy(default_factory=dict)


history = UndoRedoManager()
document = Document(transaction_manager=history)
history.initialize(document)

memo = document.current.memo
```

1. Construction leaves `memo` awaiting its first read, as required by the lazy policy.
2. Initialization publishes frame zero and leaves the manager healthy idle.
3. Reading `document.current.memo` invokes the pure lazy factory. Section 4 expressly permits first access to initialize a lazy field through a current facade.
4. Section 7 requires this operation to capture its transaction token/overlay or setup/construction context.
5. There is no active transaction, overlay, or remaining construction context.
6. After `dict` returns, the required “editable/construction state” check cannot succeed. The result therefore cannot be installed under the written rule.

This needs no reentrant callback, external mutation, or implementation failure. The ordinary documented operation itself encounters the contradictory postcondition.

**Impact:** An implementation following the new guard literally must reject a supported idle lazy read. An implementation preserving the field policy must invent an exception to the callback contract. The design therefore does not supply one coherent rule for generated callback ownership across the states in which its supported callbacks run.

**Required correction:** Define callback ownership by the original permitted operation context. Explicitly cover healthy-idle lazy materialization, with no transaction required, while retaining the same-manager mutation fence and post-call verification of that original context. Keep the existing token/overlay checks for transaction-local operations.

Also make the wording accommodate callbacks legitimately running during preparation: their result checks must verify the original authorized preparation context rather than require the manager to have returned to editing. Do not broaden idle lazy materialization into permission to begin, complete, navigate, or edit managed data from the callback.

**Closure/regression test:** Extend canonical generated coverage with first-read lazy initialization through default/current/working facades while initialized and idle. Verify one shared cached result, unchanged cursor/history, and no transaction creation. Add an idle lazy factory that attempts navigation or begin: rejection must precede manager mutation, propagated failure must leave the lazy target unset, and a later pure retry must succeed. Preserve the original equality and transient-factory fencing coverage.

## 2. Invariant analysis

The following attacks did not establish additional findings:

- **Original comparison replacement:** Equality and its truth conversion are explicitly within the fence; original token and overlay verification prevents a suspended operation from continuing under a replacement transaction.
- **Original factory-after-cleanup sequence:** Explicit completion and retained scope completion are guarded before backend lifecycle mutation. Factory failure installs no target result.
- **Nested provider materialization:** The text permits controlled nested provider reads under the same token, detects recursive fields, and preserves earlier valid overlays when the target callback fails.
- **Stale outer scopes:** The revised scope binding retains original token-bound callbacks. The pinned backend rejects stale normal exits and preserves body exceptions on stale exceptional exits.
- **Partial multi-root publication:** One aggregate participant prepares a complete replacement selection. Apply contains one reference assignment and no converters, validators, user hooks, or per-node publication.
- **Failure after publication:** Installed-selection identity and terminal completion evidence control diagnosis. Unconfirmed cleanup or ownership faults the manager instead of certifying rollback.
- **Abandoned future values:** Branch preparation trims all field and presence histories, including untouched fields. Future-only histories without a surviving baseline are removed; negative predecessor indexes are unavailable.
- **Snapshot isolation:** Snapshots retain immutable epochs. Publication normalizes mutable containers into private immutable storage, and retained working lists cannot affect committed values or later transactions.
- **Mixed historical views:** Current and working child propagation is explicit. Last-visible fallback pins descendants to its fallback frame.
- **Unsafe resurrection:** Aborted and future-only nodes without a surviving baseline cannot be attached. Previously visible absent nodes must regain working reachability before editing.
- **Topology and scope expansion:** Aliases retain node identity; cross-manager relationships and final managed cycles fail validation. Nonversioned references do not establish historical membership.
- **Resource or management disclosure through snapshots:** Snapshots expose managed data only, excluding user methods, lazy fields, caches, resources, and the live manager.
- **Generation and mixed-version reuse:** The design requires an adapter with Undoable-owned inheritance metadata, matcher-based feature composition, compatible minimum-version testing, deterministic regeneration, and installed-wheel smoke evidence. Pinned source revisions are not claimed as distribution compatibility certification.

These conclusions assess the written design, not an existing runtime.

## 3. Risks and next action

Linear history growth, snapshot retention, trusted callable purity, externally serialized access, and absence of durable recovery remain explicit accepted limits. Generation, packaging, cleanup faults, and callback enforcement still require implementation evidence at the named gates.

The next action is a bounded design correction resolving P2-2, followed by reviewer closure at a newly pinned revision. Runtime implementation remains behind the design gate.
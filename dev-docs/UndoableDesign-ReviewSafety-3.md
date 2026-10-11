# YIDL Undoable Design — SAFETY-AXIS REVIEW

**Review object:** `yidl_undoable` README.md and dev-docs/UndoableDesign.md at `616f2f65473b1240535a6317d8cc79d5cec18414`. Controlling design status: DRAFT, dated 2026-10-12. Design-stage API review only.

**Baseline:**

| Repository | Revision |
| --- | --- |
| `yidl_undoable` | `616f2f65473b1240535a6317d8cc79d5cec18414` |
| `yidl-lifecycle` | `230362f642d6e9205897698670fe5f87d2c905ce` |
| `yidl` | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| `astichi` | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| `yidl-cache` | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Object and supporting source bytes were read using `git show SHA:PATH`. All five HEADs matched this tuple at the start and end.

**Date:** 2026-10-12

**Axis:** Safety — attack callback ownership, publication, recovery, historical isolation, degraded paths, and compatibility. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: GO** — zero open findings. P2-2 is closed in the written contract, original P2-1 closure is preserved, and full-contract regression review established no new defect. This fulfills the prior pre-commit to GO.

---

## Prior-finding closure table

| Prior finding and counterexample | Independent retrace against this revision | Disposition |
| --- | --- | --- |
| P2-1: equality replaces its initiating transaction | A setter captures transaction T and overlay O. Equality or comparison-result truth conversion attempts rollback and replacement begin. Lines 354–363 require the callback fence to reject these operations before lifecycle mutation. Lines 371–384 require the original token, overlay, and editing state before installation; the operation cannot resume under replacement U. | Closed; closure preserved. |
| P2-1: transient working factory completes T before installing its result | Working factories remain fenced. Lines 470–476 require retained token scope callbacks to check the fence before delegating to original token-bound backend callbacks. Propagated callback failure installs no target result; catching a rejected completion leaves the result owned by T and subject to T’s later cleanup. | Closed; closure preserved. |
| P2-2: first-read lazy factory has no permitted idle context | After initialization, `document.current.memo` invokes its pure lazy factory while healthy idle. Lines 354–358 now capture the published selection and idle state. Lines 375–380 explicitly permit initialization through default/current/working views without a transaction, verify that captured context, and cache one shared result without changing history. | Closed. |
| P2-2: callback installation incorrectly requires editing during preparation | Freeze and validation callbacks capture their authorized candidate/preparation context. Lines 371–375 require verification of that context during preparation rather than a return to editing. This agrees with the aggregate preparation/publication ordering in lines 483–499 and the preview contract in lines 519–524. | Closed. |
| P2-2: idle factory reentry failure prevents coherent retry | Begin/navigation remains forbidden by the same-manager fence. Propagated failure leaves the lazy target unset; a later pure retry is expressly permitted. Lines 722–725 require canonical coverage for the cached idle result, unchanged history, rejected reentry, and retry. | Closed. |

These closures were derived from the corrected rules and original sequences, not from the remediation plan’s claimed dispositions. Runtime regression tests remain implementation obligations.

## Changed-range analysis

Read-only comparison against `14de6f98cf2aca81d24acd3e20a959cdf795498f` established the following object changes:

| Location in `yidl_undoable` | Analysis |
| --- | --- |
| dev-docs/UndoableDesign.md, lines 354–358 | Replaces the incomplete editing/construction ownership model with the original permitted operation context, explicitly including idle selection/state and authorized preparation. |
| dev-docs/UndoableDesign.md, lines 371–385 | Gives context-specific post-call checks. Permits idle lazy materialization, preserves transaction-local token/overlay checks, keeps mutation fencing in every context, and defines failed lazy retry. |
| dev-docs/UndoableDesign.md, lines 722–725 | Adds the required canonical idle-lazy and rejected-reentry coverage. |
| README.md | Unchanged. Its field-policy and nested-view walkthroughs remain consistent with the corrected contract. |

The correction changes no public method, field policy, historical storage, publication point, or ownership architecture. No **NEW ARCHITECTURAL** root cause was established.

## 0. Evidence base

Workspace AGENTS.md, AGENTS_GWZ.md, and applicable member AGENTS.md instructions were read in this continuing reviewer context. No member AGENTS.md was found in `yidl_undoable`.

For this focused re-verdict, read at the new pinned revision:

- `yidl_undoable`: README.md in full.
- `yidl_undoable`: dev-docs/UndoableDesign.md in full, lines 1–804.
- `yidl_undoable`: dev-docs/CurrentProgramCheckpoint.md.
- `yidl_undoable`: dev-docs/UndoableDesign-RemPlan-2.md.
- `yidl_undoable`: dev-docs/UndoableDesign-ReviewSafety-2.md.
- The complete canonical-generated Safety Round 3 prompt.
- Read-only Python `difflib` comparison of the preceding and current committed design and README bytes.

The continuing context also retains the original Safety report, RemPlan-1, and direct inspection of unchanged pinned supporting evidence:

- `yidl-lifecycle`: docs/ManagedContextApiDraft.md and dev-docs/TransactionScopeOwnership.md in full.
- src/yidl_lifecycle/transaction_yidl.py, lines 1–320 and 330–810: scope binding, original-token ownership, participant capture, completion fencing, application/discard ordering, finalization, and terminal evidence.
- src/yidl_lifecycle/lifecycle_markers.py, lines 1–385.
- src/yidl_lifecycle/lifecycle_harvester.py, lines 44–189, 436–498, 548–627, and 669–711.
- src/yidl_lifecycle/lifecycle.py, lines 1–200.
- src/yidl_lifecycle/yidl/lifecycle_core.yidl, lines 410–490.
- src/yidl_lifecycle/yidl/lifecycle_managed.yidl, lines 205–390.
- src/yidl_lifecycle/yidl/lifecycle_transient.yidl, lines 185–310.
- src/yidl_lifecycle/yidl/lifecycle_default_factories.yidl, lines 1–210.
- src/yidl_lifecycle/yidl/lifecycle_const_static.yidl, especially lines 99–128.
- src/yidl_lifecycle/yidl/lifecycle_base.yidl and pyproject.toml.
- `astichi`: selected current-snapshot, governing-rule, executable-AST, and compile/build sections of dev-docs/AstichiSingleSourceSummary.md; dev-docs/AstichiCodingRules.md.
- `yidl`: dev-docs/YidlDesignSummary.md, lines 1–90.

`git -C MEMBER rev-parse HEAD` confirmed every pinned revision at both review boundaries. Only inspection commands were used. No writes, tests, builds, or Git mutations occurred. No other current-round reviewer prompt or report was inspected.

## 2. Invariant analysis

The following attacks failed to establish an open defect:

- **Idle materialization changes history:** The corrected rule caches nonversioned lazy data under the captured idle selection/state, requires no transaction, and expressly leaves history unchanged. It agrees with the existing shared lazy field policy.
- **Idle callback navigates or opens an edit:** The same-manager fence still rejects navigation and begin before lifecycle mutation. Failure leaves the target unset, making pure retry coherent.
- **Preparation requires an impossible state transition:** Callback ownership now follows the authorized candidate/preparation context. Final preparation remains fenced during completion; preview prepares a throwaway candidate and leaves the transaction active.
- **Original callback replaces transaction ownership:** Equality, truth conversion, and working factories remain covered. Results cannot migrate to a newly acquired token.
- **Retained scopes bypass the callback fence:** Guarded `bind_scope` callbacks check the Undoable fence before invoking the backend’s original token-bound completion. Stale-scope semantics remain preserved.
- **Construction publishes incomplete nodes:** Resolved private constructor baselines remain readable without thaw or managed writes. Unresolved/recursive providers fail contextually; only complete nodes register privately.
- **Partial publication across roots:** One aggregate participant prepares the complete replacement selection. Apply performs one reference assignment and invokes no application code.
- **Failed completion falsely certifies rollback:** Installed-selection identity and terminal completion evidence determine publication and cleanup. Unconfirmed state faults the manager instead of asserting restoration.
- **Abandoned future values reappear:** Branch preparation trims every field and presence history, including untouched fields. Histories without surviving baselines are removed; negative predecessor indexes mean unavailable.
- **Snapshots change after truncation:** Snapshots retain immutable epochs. Normalized committed containers do not retain mutable working storage.
- **Parent and child resolve different historical frames:** Current/working propagation remains explicit; last-visible descendants remain pinned to the fallback frame.
- **Unavailable handles resurrect abandoned data:** Aborted and future-only nodes without a surviving baseline cannot be attached. Previously visible absent nodes regain editability through working reachability.
- **Deferred resource ownership widens reversal claims:** Resource effects remain application-owned and outside undo. Snapshots exclude management storage, resources, lazy fields, user methods, and the live manager.
- **Source reuse implies unsupported compatibility:** Minimum-version tests, resource packaging, deterministic regeneration, and isolated installed-wheel smoke checks remain mandatory. The source tuple does not certify every existing distribution.

The full-contract review found no regression to topology, absence policies, joined transactions, immutable histories, generation boundaries, inheritance restrictions, or packaging gates.

## 3. Risks and next action

Linear history growth, snapshot retention, trusted callable purity, externally serialized access, and lack of durable recovery remain explicit accepted limits. Callback guards, backend cleanup handling, generated behavior, and packaging still require implementation evidence.

The next action is to record scope-limited design acceptance and proceed to the separate strict red/green/refactor implementation plan once the dual design gate is satisfied. This GO accepts the written design only; it does not certify a runtime or release.
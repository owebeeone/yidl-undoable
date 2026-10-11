# YIDL Undoable Design — CONSISTENCY-AXIS REVIEW

**Review object:** `README.md` and `dev-docs/UndoableDesign.md` at `616f2f65473b1240535a6317d8cc79d5cec18414`. Controlling design status: DRAFT, dated 2026-10-12. Design-stage API review only.

**Baseline:**

| Repository | Revision |
| --- | --- |
| `yidl_undoable` | `616f2f65473b1240535a6317d8cc79d5cec18414` |
| `yidl-lifecycle` | `230362f642d6e9205897698670fe5f87d2c905ce` |
| `yidl` | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| `astichi` | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| `yidl-cache` | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Object and substantive source bytes were read using `git show SHA:PATH`. Every listed HEAD matched the tuple at the start and end of this review.

**Date:** 2026-10-12

**Axis:** Consistency against the controlling document graph, including Surface regression and original-counterexample closure. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: GO** — no open P0, P1, P2, or P3 findings on this axis. Original Consistency closures remain valid. No new architectural root cause was established. This accepts the design contract only; another axis’s finding requires that reviewer’s independent disposition.

---

## Prior-finding closure table

| Prior finding | Independent retrace at this revision | Disposition |
| --- | --- | --- |
| Consistency P2-1 — Constructor factory reuse lacks a managed-read contract before initial publication | A setup node with managed `seed=3` and an opt-in self factory computing `self.seed + 1` obtains `4` from the resolved private constructor baseline, without requiring a committed frame. Named providers use the same table in dependency order. Provisional construction has the same explicit rule. Unresolved/self-recursive provider reads fail contextually without registering a partially initialized node or publishing values. The section-7 clarification preserves these construction contexts. | **Closed for design; closure preserved.** `dev-docs/UndoableDesign.md:217–236`, `354–358`, `720–722`. |
| Consistency P3-1 — First-use page omits the default field-kind policy | For an unmarked scalar beside a managed scalar, the README still predicts that the unmarked value survives rollback and undo. Reversible data explicitly requires `managed`. README bytes are unchanged from round 2. | **Closed; closure preserved.** `README.md:17–19`; `dev-docs/UndoableDesign.md:142–155`. |
| Consistency P3-2 — First-use page provides no nested-object inspection path | The unchanged parent/child example initializes the graph, edits through the propagated working child, inspects the committed child through `.current`, commits by scope exit, and then undoes/redoes. It identifies managed relationships as the historical membership boundary. | **Closed; closure preserved.** `README.md:58–87`; `dev-docs/UndoableDesign.md:204–209`, `283–304`. |
| Round-2 Consistency review | Its GO was reconsidered against the full revised contract and the new idle/preparation wording, rather than inherited automatically. | **GO retained.** No Consistency remediation remains. |

These dispositions follow the original sequences and corrected text, not the remediation plans’ claimed closures. Runtime regression evidence remains an implementation obligation.

## Changed-range analysis

A read-only comparison against `14de6f98cf2aca81d24acd3e20a959cdf795498f` found:

- **README:** No changes. The prior Surface corrections remain intact.
- **Section 7, lines 354–358:** Replaced the token-or-construction formulation with the original permitted operation context: editing token/overlay, private setup/construction context, healthy-idle state and published selection, or authorized candidate/preparation context.
- **Section 7, lines 371–385:** Made result installation context-specific. Idle lazy initialization requires no transaction, caches one shared result, and leaves history unchanged. Failed lazy factories leave the target unset for retry. Callback mutation fences remain mandatory in every context.
- **Section 13, lines 722–725:** Added canonical coverage for first idle lazy reads through all three views, one shared cached result, unchanged transaction/history state, rejected begin/navigation, and later pure retry.
- **Checkpoint:** Records the second bounded remediation and retains the separate implementation-plan gate after dual design acceptance.

The correction changes neither public API shape nor history/publication architecture. The full document was reviewed, including unchanged construction, preview validation, initialization, failure, and packaging provisions.

## 0. Evidence base

This continues the round-2 reviewer context as the focused prompt requires. The pinned README was read first in this round, before its design and remediation inputs; the original cold Surface pass remains available from the same independent context.

Fresh reads included:

- `README.md`, complete, lines 1–87.
- `dev-docs/UndoableDesign.md`, complete, lines 1–804.
- `dev-docs/CurrentProgramCheckpoint.md`, complete.
- `dev-docs/UndoableDesign-RemPlan-1.md`, complete.
- `dev-docs/UndoableDesign-RemPlan-2.md`, complete.
- `dev-docs/UndoableDesign-ReviewConsistency-2.md`, complete.
- `../yidl-lifecycle/docs/ManagedContextApiDraft.md`, lines 80–185, emphasizing live views, aggregate access, and lazy initialization.
- `../yidl-lifecycle/dev-docs/TransactionScopeOwnership.md`, lines 1–105.
- `../yidl-lifecycle/src/yidl_lifecycle/yidl/lifecycle_const_static.yidl`, lines 1–166 and 476–512: shared lazy storage, factory evaluation, assignment, and matcher selection.
- `../yidl-lifecycle/src/yidl_lifecycle/lifecycle_markers.py`, lines 144–166: lazy defaults and `static` alias.
- `../yidl-lifecycle/src/yidl_lifecycle/transaction_yidl.py`, lines 272–305, 608–632, and 698–765: scope binding, active tokens, preview validation, nesting, and final completion.

Evidence retained from the preceding review in this context includes:

- The original `dev-docs/UndoableDesign-ReviewConsistency.md`.
- Lifecycle’s complete API/view guide, field-kind matrix, scope-ownership contract, and developer index.
- Targeted pinned marker normalization, harvester inheritance/provider metadata, decorator assembly, transaction participant interface, and default-factory/transient/core/base YIDL resources.
- `../yidl/dev-docs/YidlDesignSummary.md`, sections 26–27 and concept-composition decision-ledger entries; `YidlCodingRules.md`.
- `../astichi/dev-docs/AstichiSingleSourceSummary.md` and `AstichiCodingRules.md`, targeted composition, hygiene, executable AST, layering, and ownership provisions.
- `../yidl-cache/README.md`, consumer/cache ownership boundary.
- Workspace and applicable member instructions.

Their repository revisions are unchanged and were verified again.

Inspection used pinned `git show`, `rg`, `git rev-parse HEAD`, and read-only Python. In-memory `difflib` compared the object and checkpoint. `ast.parse` successfully parsed the two README Python blocks and one design Python block; none was executed.

No files were written, no builds or tests were run, and no Git state was mutated. No other current-round reviewer prompt or report was inspected.

## 2. Invariant analysis

### Idle lazy materialization

The revised callback contract now agrees with the existing field-policy table and the pinned Lifecycle lazy implementation.

Consider an initialized healthy-idle manager and an unset nonversioned lazy `memo` field with a pure factory. Reading `document.current.memo`:

1. Captures the healthy-idle state and published selection.
2. Runs the factory under the callback fence.
3. Verifies that captured context.
4. Installs one shared nonversioned result.
5. Leaves the active transaction absent and history unchanged.

Subsequent default/current/working reads return that cached result. There is no longer a requirement to establish an editing token merely to install a lazy result.

If the factory attempts begin or navigation, the fence rejects the action before lifecycle state changes. Propagated factory failure leaves the target unset, permitting a later pure retry. This is consistent with shared nontransactional lazy storage and does not imply rollback of arbitrary external factory effects.

### Preparation, initialization, and preview

Preparation callbacks now have their own authorized candidate/preparation context instead of being required to satisfy editing-state postconditions.

This is consistent with the final commit path: conversion and validation occur before the single publication assignment, while completion and callback fences remain active. Candidate validators read frozen candidate values through all three views.

Initialization and explicit preview remain governed by their specific contracts. Initialization publishes frame zero only after complete validation and remains retryable on failure. Preview uses the same preparation work without publication, retains the active edit, and does not consume a frame ID. Capturing a preparation context does not authorize transaction completion or turn a preview into an accepted commit.

The implementation must preserve that distinction when representing preparation ownership; the adjacent Lifecycle contract keeps standalone validation separate from final completion and leaves terminal completion evidence unset for previews.

### Provider and callback regressions

The original provider exceptions remain explicit and take precedence over published-frame resolution. Setup/provisional self factories and named providers therefore remain satisfiable before publication.

The revised context wording does not weaken transaction-local ownership: those operations still verify their original token, overlay identity, and editing state. Lost ownership cannot be repaired by reacquiring a replacement token.

Comparison, truth conversion, working factories, converters, and validators remain fenced. Guarded token scope callbacks retain the same stale-token semantics supported by the pinned `bind_scope` and backend scope methods.

### Surface regression

The README continues to document initialization, editing, explicit abort/commit, context completion, undo/redo, and nested current/working inspection. Unmarked-field defaults and the managed relationship boundary remain stated.

Lifecycle pairs remain complete: begin/commit-or-rollback, undo/redo, and add-root/remove-root. Manager defaults and custom-key usage are unchanged. Unsupported features remain explicit scope decisions, with no new placeholder API.

The package is still clearly described as proposed. No installation or execution evidence was inferred from its examples.

### Whole-contract regression

The following attacks still fail:

- A negative predecessor index cannot select the last stored value.
- A commit after undo cannot retain an untouched field’s abandoned future version.
- Snapshot reads cannot silently switch to the live epoch after branch truncation.
- Last-visible descendants cannot mix historical parent data with a newer child frame.
- Removing one rooted path cannot erase membership provided by another path.
- Provisional construction cannot publish membership merely by producing a Python handle.
- Failed preparation cannot partially publish earlier nodes or discard redo.
- An exception after publication cannot be reported as proof of clean rollback.

The aggregate remains one backend participant, with one prepared selection and one publication assignment. Fault handling still uses terminal evidence and installed-selection identity.

Generation remains layered and matcher-selected, with plain generated classes and Undoable-owned history semantics. Harvester adaptation, wheel-safe resource reuse, cache boundaries, and package/regeneration gates are unchanged.

The checkpoint still requires design acceptance before the separate TDD plan and requires runtime acceptance independently. Deferred outcomes were not reported as missing implementation defects.

## 3. Risks and next action

The context-specific callback rules now form a coherent design contract. Runtime enforcement remains unproved, particularly across idle lazy reads, initialization, preview preparation, final completion, and callback failure.

The next action is to preserve the original provider/Surface regression cases and the added idle lazy cases in the separate TDD implementation plan, once the independent dual design gate is satisfied. No additional Consistency remediation is required at this tuple.
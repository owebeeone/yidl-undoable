# YIDL Undoable Design — SAFETY-AXIS REVIEW

**Review object:** `yidl_undoable` README.md and dev-docs/UndoableDesign.md at `dbd89160ed54d6bab5887ee43bb75c4217459d21`. Controlling design status: DRAFT, dated 2026-10-12. Design-stage API review only.

**Baseline:**

| Repository | Revision |
| --- | --- |
| `yidl_undoable` | `dbd89160ed54d6bab5887ee43bb75c4217459d21` |
| `yidl-lifecycle` | `230362f642d6e9205897698670fe5f87d2c905ce` |
| `yidl` | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| `astichi` | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| `yidl-cache` | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Object and source bytes were read using `git show SHA:PATH`. All five HEADs matched this tuple at both the start and end.

**Date:** 2026-10-12

**Axis:** Safety — attack what the text permits to go wrong, particularly publication, callback reentrancy, recovery, historical isolation, and compatibility. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: NO-GO** — one P2 finding blocks. I pre-commit to GO on a revision that resolves P2-1 as specified.

---

## 0. Evidence base

Read workspace AGENTS.md and AGENTS_GWZ.md, and the applicable AGENTS.md files in `yidl-lifecycle`, `yidl`, `astichi`, and `yidl-cache`. No member AGENTS.md was found in `yidl_undoable`.

Reviewed the pinned object:

- `yidl_undoable`: README.md, lines 1–52.
- `yidl_undoable`: dev-docs/UndoableDesign.md, sections 1–15, with numbered inspection of topology, stable values, histories, snapshots, publication, validation, and failure handling.
- `yidl_undoable`: dev-docs/CurrentProgramCheckpoint.md, including scope, acceptance gates, and the operator’s remediation-cap override.

Inspected pinned Lifecycle evidence:

- docs/ManagedContextApiDraft.md, lines 1–185.
- dev-docs/TransactionScopeOwnership.md, lines 1–105.
- dev-docs/README.md.
- src/yidl_lifecycle/transaction_yidl.py: token scope behavior, completion evidence, ownership checks, completion callbacks, nesting, enlistment, and finalization, particularly lines 175–304 and 330–805.
- src/yidl_lifecycle/lifecycle_markers.py: supported factories, managed/transient options, normalization, comparison defaults, and callable checks.
- src/yidl_lifecycle/lifecycle_harvester.py: declaration normalization, inherited facts, factory providers, transaction keys, and reserved-name checks.
- src/yidl_lifecycle/lifecycle.py, lines 1–197: harvesting, generation, execution, and builder binding.
- src/yidl_lifecycle/yidl/lifecycle_core.yidl, lines 439–464: active-transaction checks and working-token enrollment.
- src/yidl_lifecycle/yidl/lifecycle_managed.yidl, particularly lines 233–384: comparison guards and generated assignment/thaw ordering.
- src/yidl_lifecycle/yidl/lifecycle_transient.yidl, lines 64–190 and 193–305: provider normalization and working-factory materialization.
- src/yidl_lifecycle/yidl/lifecycle_default_factories.yidl: targeted inspection of factory evaluation and provider resources.
- src/yidl_lifecycle/yidl/lifecycle_base.yidl and pyproject.toml: composition and packaging patterns.

Only inspection commands were used. No tests, builds, writes, or Git mutations were performed. No other current-round review prompt or report was inspected.

## 1. Findings

### [P2-1] Transaction-local callback fencing excludes comparisons and working factories

**Location:** `yidl_undoable`: dev-docs/UndoableDesign.md, lines 161–169, 297–317, 414–419, and 448–462. Supporting reuse evidence: `yidl-lifecycle`: src/yidl_lifecycle/yidl/lifecycle_managed.yidl, lines 250–262 and 325–340; lifecycle_transient.yidl, lines 228–243; lifecycle_core.yidl, lines 439–464.

**Root cause:** The design fences converters and validators, but does not specify equivalent protection for other application code invoked while a generated operation is inspecting or materializing transaction-local state. Value comparison and `working_default_factory` are supported callback paths. Neither has an explicit prohibition on transaction completion/replacement or a requirement to bind the entire operation to its original token.

**Violated invariant:** An operation started under transaction T must not resume by installing pending state under replacement transaction U, or install an overlay after T’s completion cleanup. A generated read or comparison must not silently defeat the joined-transaction ownership boundary.

**Credible state sequence:**

1. Configure a managed field with pure thaw/freeze converters. Thaw returns a custom editable representation; freeze returns an admitted stable tuple. Custom working values are permitted by section 7, although custom stored values are rejected.
2. Begin T and perform an assignment using the default value-comparison guard.
3. The comparison invokes the editable object’s `__eq__`. That method calls `history.rollback()`, calls `history.begin()` to create U, and returns false.
4. The suspended setter resumes. The design requires checking that the backend token matches the overlay, but does not require that this still be the original T. A fresh check against U’s matching overlay can succeed, allowing the assignment begun in T to enter U.

This is a synchronous callback invoked by generated code. It does not depend on threads, escaped-list mutation, or an impure converter.

The pinned Lifecycle template demonstrates the hazardous ordering: it checks the active transaction, runs equality, then obtains the working transaction again before assignment. Its working helper checks the transaction active at that later point; it does not bind the setter to the token observed before comparison.

The same uncovered boundary exists when a transient `working_default_factory` completes T before returning its value. Lifecycle’s resource invokes the factory after enrollment and installs the returned working value afterward. Undoable must not inherit that ordering without guarding or rechecking the original operation ownership: completion cleanup can run before the value being cleaned up has even been installed.

**Impact:** A conforming implementation can transfer a pending operation into an unrelated replacement transaction, or leave transaction-local scratch state installed after completion. The latter contradicts the promised clearing of transient overlays; the former breaks transaction composition and can publish an edit that the initiating transaction rolled back.

**Required correction:** Specify an operation-owned callback boundary for generated comparison and transaction-local factory materialization. Capture the original token and overlay before invoking application code. Reject same-manager begin/completion/navigation that would invalidate the suspended operation, and verify original token, overlay identity, and editable state before installing its result. Specify that callback failure or ownership loss installs no new pending value. Include equality-result truth conversion in the comparison boundary.

This is a bounded missing fence, not evidence that immutable epochs or single-point publication require architectural redesign.

**Closure/regression test:** Extend canonical generated coverage with a custom editable value whose equality attempts rollback followed by replacement begin, and a transient working factory that attempts completion. Assert rejection before lifecycle state changes, unchanged published history and redo, no pending value transferred to another token, and no transient value surviving completion. Also verify that ordinary pure comparisons and provider-dependent working factories remain usable.

## 2. Invariant analysis

The following attacks did not establish additional defects:

- **Partial publication across roots:** One aggregate participant prepares the complete replacement selection. Apply performs one reference assignment and runs no converters or validators. A later-node preparation failure therefore cannot publish an earlier node.
- **Stale outer scope completing a replacement transaction:** Lifecycle’s token-bound scope callbacks distinguish the original token. The design expressly preserves this fencing.
- **Abandoned future values resurfacing:** Branch preparation trims every field and presence history, including untouched fields, and removes histories without a surviving baseline. Negative predecessor positions are explicitly unavailable.
- **Snapshot corruption through truncation or retained working lists:** Snapshots retain immutable epochs; publication privately normalizes containers. Completed working lists must be detached from committed state and subsequent edits.
- **Mixed historical parent/current child reads:** Current and working propagation is specified, and last-visible fallback pins descendants to the fallback frame.
- **Unsafe resurrection:** Future-only and aborted handles without a surviving baseline cannot be attached. Previously visible absent nodes must become reachable before editing.
- **False rollback after publication failure:** Installed-selection identity and terminal completion evidence control diagnosis. Unconfirmed ownership or cleanup faults the manager instead of certifying rollback or reuse.
- **Resource reversal and disclosure through snapshots:** Resource ownership is explicitly deferred. Snapshots expose managed data only and exclude management resources, caches, lazy fields, user methods, and the live manager.
- **Mixed-version reuse:** The design requires compatible minimum-version testing and installed-wheel smoke evidence; current source revisions are not represented as certification of every existing distribution.

These conclusions concern the written design. They do not certify a runtime.

## 3. Risks and next action

The documented linear-history memory cost, snapshot retention, trusted converters, externally serialized access, and lack of durable recovery remain accepted limits. Packaging and generation parity still require implementation evidence at their named gates.

The next action is one bounded design correction resolving P2-1, followed by review closure at a newly pinned revision. Runtime implementation should remain behind the design gate.
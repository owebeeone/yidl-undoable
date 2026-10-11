# Undoable Design Remediation — Round 1

Reviewed baseline: `dbd89160ed54d6bab5887ee43bb75c4217459d21`.
Status: one merged bounded correction; originating counterexamples require review.

| Finding | Disposition | Closure evidence required |
| --- | --- | --- |
| Consistency P2-1 | Define construction-only provider reads of resolved unpublished baselines in setup and provisional construction; unresolved/self-recursive providers fail contextually. No editing/publication is enabled. | Retrace both self/named setup and provisional factory examples against the corrected text; require canonical tests in the TDD plan. |
| Consistency P3-1 | Explain the plain/nontransactional default on the first-use page. | Cold managed/unmarked scalar walkthrough predicts rollback and undo behavior. |
| Consistency P3-2 | Add managed nested relationship and current/working child walkthrough. | Cold initialize/edit/inspect/commit/undo/redo walkthrough uses only documented accessors. |
| Safety P2-1 | Fence all transaction-local application callback paths, including equality/truth conversion and working factories, to the original operation token/overlay; forbid completion/replacement and reject lost ownership before installing results. | Retrace the original equality replacement and transient factory completion counterexamples; require adversarial canonical coverage. |

No blind convergence was observed: the two axes found independent lifetime
boundaries. Both reviewers classified their blocking roots as bounded contract
corrections, not a requirement to replace the history architecture.

The callback fence clarifies a mutation boundary, so two fresh reviewer contexts
replace the initial pair for the revised object. Each inherits closure of its
axis's original findings. Reports remain peer-blind; no third reviewer is added.

Design acceptance will not self-close these findings. The new reviewers must
verify the original counterexamples at the revised committed design.

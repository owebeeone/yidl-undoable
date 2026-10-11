# Implementation remediation plan — cycle 1

Status: required; runtime **NO-GO** at `a97e43e5010fd22a9bcd008f27072ca656b73f5b`.
Both independent reports are filed verbatim. No findings overlap: the two axes
found seven distinct P2 roots. All are accepted for bounded correction. Both
reviewers explicitly classified them as repairable under the accepted design;
no architectural redesign is indicated.

## One merged revision

| Origin / ID | Disposition | Required failing regression and closure |
| --- | --- | --- |
| Code P2-1 | Correct mandatory empty constructor parameter composition in owning YIDL resource; regenerate base, never patch generated output. | Canonical empty, local-store-only, classvar-only and init=False managed declarations construct with only required keyword transaction_manager and execute. No dummy field. |
| Code P2-2 | Add recursive exact built-in set projection, preserving working set identity for in-place use and leaving it unchanged for ordinary projection. | Canonical ordinary-after-thaw and working-from-assigned ordinary/current child handles; child reads do not thaw unexpectedly; nested containers and escaped set detachment. |
| Code P2-3 | Materialize named lazy constructor providers via existing fenced provider path; never pass MISSING. | Canonical const/managed dependencies, reversed declaration order, setup/provisional construction, shared single evaluation; narrow unresolved/recursive errors with no partial registration. |
| State P2-1 | Tie healthy discard to unchanged pre-completion selection, and changed selection to confirmed publication. | Fault after install/bookkeeping faults immediately; known installed history readable but begin/navigation blocked. Fault before bookkeeping blocks unconfirmed reads/snapshots. Ordinary discard/preparation failure remains healthy. |
| State P2-2 | Distinguish candidate pins from historical pins for transient reads, preserving active ordinary/working versus baseline current semantics. | Canonical validator/preview reads assigned transient, rejection preserves redo and repairability; working factory provider under validation and reentry fence. |
| State P2-3 | SnapshotNode equality/hash uses pinned-context and node identity, not recursive graph records. | Canonical node frozenset and nested mapping/tuple aliases, cached node membership/hash, old snapshot surviving live branch. |
| State P2-4 | Failed outer-begin setup always detaches overlay; abort failure/incomplete ownership evidence faults immediately and preserves causal failures. | Narrow failed enlist with abort failure before/after closure; no editable overlay or joining; old confirmed snapshot readable; begin/navigation reject. Successful abort remains retryable. |

The drafter owns implementation/tests and TDD handoff evidence only. Record actual
RED before fixes, then GREEN and refactor. Keep successful end-to-end cases in the
existing canonical harness; fault/diagnostic cases narrow. Run full tests,
canonical/base regeneration, three-version compatibility and rebuilt wheel smoke.
No neighbor source edits, Git operations, pushes/tags/releases or new agents.

These corrections implement existing declared boundaries; they do not change the
public API, backend integration, key policy, graph/history architecture or platform
assumptions. The same two reviewers will independently re-run their original
counterexamples and examine changed ranges. If implementation materially changes
a shared boundary or call graph beyond these bounded corrections, replace the
reviewers with two fresh axes as required by the skill. No self-closure is valid.

## Post-patch reviewer selection

Actual correction adds a constructor-provider call path through the existing lazy
getter and changes begin/completion legality predicates. Apply review-loop Step
5.5 conservatively: two fresh reviewers replace the original pair at cycle 1's
settled revision. They inherit all original same-axis counterexamples and must
file closure tables and changed-range analysis. No extra reviewer is added to
one revision; the accepted design itself has not changed or required redesign.

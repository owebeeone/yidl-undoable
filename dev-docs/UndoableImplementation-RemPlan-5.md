# Implementation remediation plan — cycle 5

Status: required; Code/Surface **GO**, State **NO-GO** at
`adcdc3071c00330787c12d05faeb381705215d2d`. All thirteen historical
counterexamples are independently closed. One bounded residual P2 remains.
Both complete reports are filed verbatim. No architectural failure was found;
this third extra bounded cycle uses the operator's explicit authorization.

| Origin / ID | Disposition | Actual RED and closure |
| --- | --- | --- |
| State round5 P2-1 | Carry requested commit/rollback through explicit and original token-bound scope completion. Validate the observed outcome against both original nesting and operation. Only joined commit may return a nonterminal exact decrement. Successful outer commit requires confirmed installed publication. Preparation-failure discard may close healthily only while propagating its failure. Rollback at any depth requires terminal complete discard and unchanged selection. Preserve existing exact authority, identity and persistent-fault checks. Any incompatible outcome faults immediately; retain actual confirmed publication rather than trying to rewind it. | Actual REDs for all four report rows through explicit and retained-scope entry: premature joined commit, joined rollback delegated to commit, outer rollback delegated to commit, and outer commit delegated to rollback. Assert HistoryFaultError, detached overlays, retained evidence/confirmed snapshot, and later mutation/navigation rejection. Preserve healthy inner/outer commit, rollback at multiple depths, failed preparation discard, stale exceptional scopes and unchanged pre-transition rejection. Include outcome-with-failure variants so a propagated exception does not authorize operation-incompatible publication. |

One merged TDD patch under the accepted design: write and execute genuine
failing tests before runtime changes; record timestamps, results and refactoring.
Use a coherent operation-specific transition predicate, not extra flags for
individual counterexamples. No API expansion, neighbor source edits, Git,
new agents or root-owned evidence writes by the drafter. Assigned evidence:
ImplementationDraft.md and TddEvidence.md.

Root repeats all supported-version and rebuilt isolated-wheel gates. The common
completion signature/call graph changes, so two fresh replacement reviewers must
review the next exact settled tuple. Each inherits all historical originals:
six Code findings and eight State findings. Prior Code GO does not accept changed
bytes. Acceptance requires both new verdicts GO; architecture failure requires
an explicit redesign before further implementation.

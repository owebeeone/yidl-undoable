# Implementation remediation plan — cycle 2

Status: required; dual **NO-GO** at `72e1433e1290cc41392223c9d5981847e396f68e`.
All seven cycle-1 original counterexamples are closed by fresh same-axis reviewers.
Three additional bounded P2 roots remain. Reports are filed verbatim. Neither
reviewer found an architectural root. This cycle is one merged TDD correction
under the unchanged accepted design. No self-closure or premature acceptance.

| Origin / ID | Disposition | Failing regression and closure |
| --- | --- | --- |
| Code round2 P2-4 | Recursively project raw provisional baseline child facades to requested parent view, under the existing operation fence. Preserve current provisional absence, no ordinary thaw, nested supported containers. | Canonical new parent with current/default child refs, before/after attachment; ordinary/default child sees pending edits without touching an untouched child field, working child thaws; nested containers; publication agrees. |
| Code round2 P2-5 | Fence provisional pre-thaw projection before application-backed mapping iteration; bind projection, thaw and installation to the original token/overlay. | Narrow first-iteration rollback, navigation, replacement begin and retained-scope completion attacks all reject before mutation; same token, pending root edits and untouched target remain; pure retry succeeds. Also cover new ordinary provisional projection. |
| State round2 P2-1 | Protect complete begin setup, including backend begin partial return, overlay allocation, aggregate enlistment and Undoable scope binding; capture pre-begin ownership. Always detach on setup failure; abort newly acquired/failed joined work only with confirmed evidence or fault with original causes. | Narrow backend begin raises after acquiring token, allocation MemoryError, wrapper bind failure, abort failures at these stages, and failed joined setup. Confirmed cleanup permits retry with exactly one committed frame/idle; unconfirmed cleanup faults immediately with no editable overlay. Retain all original enlist/abort and publication tests. |

Drafter writes source/tests/API and its TDD/implementation evidence only, with
actual RED before fixes and GREEN/refactor after. No Git, neighbor writes or new
agents. Root repeats full supported-version and rebuilt wheel checks. This changes
existing begin/read call paths, so two fresh reviewers replace cycle-1 reviewers
under Step5.5; each inherits every original and new same-axis counterexample,
closure tables and changed-range duties. No third reviewer of one revision.

The operator permits extra bounded cycles if required. A broken architecture
must instead receive explicit redesign and fresh design review. These findings
have been classified bounded by the reviewers and do not trigger redesign.

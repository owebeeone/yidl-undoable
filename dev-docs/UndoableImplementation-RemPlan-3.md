# Implementation remediation plan — cycle 3

Status: required; dual **NO-GO** at `38662bcbbe7758fb5f980859675fa9efcb41d614`.
All ten historical runtime counterexamples are closed by the fresh same-axis
reviewers. Two additional bounded P2 findings remain. Both reports are filed
verbatim. Neither reviewer found an architectural root. This is the first cycle
beyond the default two-cycle limit, expressly authorized by the operator for
bounded corrections. The accepted design remains unchanged.

| Origin / ID | Disposition | Failing regression and closure |
| --- | --- | --- |
| Code round3 P2-6 | Recursively project the thaw converter's output to the working view before installation/return, inside the original operation fence. Preserve owned container identity and install nothing on failure. | Canonical committed/provisional parents whose converters return default/current child handles; first working access sees pending child values and permits nested thaw; repeated access preserves container identity. Cover nested mapping/set containers and ordinary no-thaw reads. Narrow application-backed thaw-result traversal rejects completion/replacement reentry before mutation, retaining original token/pending data and leaving target untouched; pure retry succeeds. |
| State round3 P2-1 | Fence application-backed key comparison, truth conversion and diagnostics at manager and subsequent backend dispatch stages. Capture original ownership before callbacks, preserve custom hashable keys and reject same-manager mutation. Backend transition fencing must allow the intended transition rather than requiring its pre-state to remain unchanged. | Narrow custom key equality reproduces rollback/replacement during commit. Reentry rejects before mutation, retains token/nesting/pending value 7 and unchanged history; pure retry commits the original edit. Cover truth conversion, repeated comparison stages in begin/commit/rollback/enlist/read dispatch and retained scope callbacks, plus wrong-key ownership preservation. |

One drafter produces one merged test-led correction. Actual REDs precede changes;
GREEN/refactor follows. Existing historical regression coverage remains. No key
type restriction, token substitution, neighbor edits, Git operations or new
agents are permitted for the drafter. Root repeats supported-version and rebuilt
wheel checks, then settles one runtime checkpoint.

These changes affect callback boundaries and reviewed read/backend call paths.
Two fresh replacement reviewers will review that checkpoint under Step 5.5,
inheriting all original same-axis counterexamples and changed-range duties.
Acceptance remains blocked until both return GO on the exact corrected tuple.

The State reviewer initially ended with a service content-flag error before any
complete report or verdict. That attempt did not count as a review. The same
reviewer completed a read-only report on retry; the failed attempt and its
measured usage remain part of the experiment record.

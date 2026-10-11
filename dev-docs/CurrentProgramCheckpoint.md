# Current Program Checkpoint

Status: DRAFT design; review pending. No runtime implementation exists.

## Directive and scope

Prepare a detailed design for a single cohesive implementation of YIDL Undoable,
using Lifecycle's generation structure and reusable field/transaction concepts.
Run the operator-requested review-loop skill with two peer-blind reviewers.

After the design, prepare a separate implementation plan using strict
red/green/refactor TDD. Mirror Lifecycle's repository layout and its inheritable
YIDL feature layers, with matcher-selected behavior for composed field kinds.

The operator subsequently authorized autonomous completion while away: reviewed
design, separate TDD plan, implementation, tests, and final review. Passing the
design gate permits the planning step; runtime acceptance still requires its own
checks and review. No further routine confirmation is needed.

## Review object

- `dev-docs/UndoableDesign.md`, with the proposed first-use surface in `README.md`.
- Tier: dual document review; Consistency with Surface, and Safety.
- Exact committed revision is recorded in the filed review prompts and reports.
- The original concept note in `../yidl/dev-docs/YidlUndoRedoConcept.md` is
  background; this detailed proposal supersedes its one-root limitation,
  illustrative names, and prohibition of nested begins.
- Adjacent repositories and unrelated workspace changes are outside the patch.

## Lane state

- Initial drafting: in progress.
- Independent review: pending.
- Blocking findings: not yet assessed.
- Remediation rounds used: zero of two.
- Implementation: not started.
- Next action: settle the design checkpoint, then dispatch the two reviewers.

The [experiment ledger](ExperimentLedger.md) records timing, token observations,
API-equivalent cost estimates, remediation, and quality evidence. The experiment
tests autonomous completion from this directive, not zero internal iterations.

The loop's outputs are committed checkpoints, verbatim reports, any merged
remediation plan, and an explicit scope-limited acceptance record. No pushes,
tags, releases, or changes to neighboring packages are part of this directive.

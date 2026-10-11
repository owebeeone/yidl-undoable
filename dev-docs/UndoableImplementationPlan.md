# Undoable Implementation Plan

Status: authorized for autonomous TDD execution after design acceptance.
Controlling contract: `UndoableDesign.md` at
`616f2f65473b1240535a6317d8cc79d5cec18414`, accepted by both round-3 reviewers.
This plan changes no public interface or supported field policy.

## Workflow and ownership

One drafter implements the complete package without Git operations. The lane
owner maintains checkpoints, measures usage, verifies gates, commits through GWZ,
and dispatches two peer-blind runtime reviewers. No adjacent package edits.

Use strict red/green/refactor for each behavior tranche: write a failing canonical
scenario or narrow diagnostic/fault test, run it and record the actual failure,
implement the missing behavior, run the focused check to green, then refactor and
rerun. Record UTC timestamps, command, failure reason, and result in
`TddEvidence.md`. Do not reconstruct red evidence from memory or count a passing
test as red. An import failure is the initial red only, not proof for later
behavior. Materialize generated-source goldens after behavior assertions pass;
golden comparison then protects deterministic generation and composition.

## Test-led sequence

| Step | Red evidence and required behavior | Implementation / refactor |
| --- | --- | --- |
| 1 | Canonical scalar/collection declaration fails to import or generate; first-use construction and frame zero unavailable. | Package skeleton, reusable marker imports, definition errors, normalized harvester facts, plain generated state/facades. Establish YIDL Core and Astichi builder/AST pipeline. |
| 2 | Canonical writes outside an edit, rollback/commit/context behavior, committed versus working view checks. | Compose GroupTransactionManager with exactly one aggregate participant; guarded original scope callbacks; managed layer and overlay. |
| 3 | Narrow predecessor negative-index/truncation failures; canonical undo/redo boundaries, noops, redo preserved on abort, untouched future field leakage. | Immutable sparse field/node histories, monotonic IDs, selection cursor, private prepared epoch, one publication assignment. |
| 4 | Canonical multi-root/shared child edits, view propagation, creation/removal/reattachment/empty roots; foreign and cyclic topology diagnostics. | Graph traversal and final reachability, manager-local stable handles, provisional lifecycle, root operations, no stale reachability caching. |
| 5 | Canonical strict/last-visible absence and descendant pinning, abandoned/aborted handles, snapshots retained through branching. | Policy objects and availability checks; data-only snapshot nodes resolved exclusively in their pinned epoch/frame. |
| 6 | Canonical const/plain/local-store/binding/lazy/transient behavior; factories, initvar/classvar and inherited declarations; unsupported/reserved diagnostics. | Feature layers and matchers select constructor forms, kind/view access, lazy mutability and factory paths; reuse Lifecycle normalized metadata with Undoable inheritance adaptation. |
| 7 | Original design counterexamples: setup/provisional named/self factory reads; unresolved/recursive providers. | Private constructor read context, dependency ordering, complete-node-only registration; no frame or mutability from construction reads. |
| 8 | Original callback attacks: equality and truth conversion attempt rollback/replacement; transient factory attempts retained scope completion; idle lazy begin/navigation and pure retry. | Callback fences capture original allowed context; verify ownership before installation. Preserve nested provider materialization and pure comparison/factory success. |
| 9 | Canonical freeze/validator failure on a later node, preview repair, detached working lists, invalid frozen output, validator reentry. Narrow synthetic cleanup/ownership fault tests. | Stable recursive value normalization, frozen candidate validators, all-or-nothing prepare, completion evidence and faulted state behavior. |
| 10 | Layer/intermediate-concept generation and installed-resource checks; inheritance combinations and representative marker selection. | Complete inheritable YIDL chain, final assembly and deterministic checked-in generated base. Remove duplication only with focused/full green evidence. |

Successful behavior belongs in canonical generated-source fixtures under
`tests/data/gold_src/` with materialized output under `tests/data/golden/`.
Use the YIDL versioned harness pattern where practical. Narrow tests cover only
recognition, mechanics, errors and synthetic failures not cleanly expressed there.
Do not mirror each successful scenario in another unit test.

All twelve verification groups in design section 13 are mandatory. The table is
an implementation order, not permission to drop cases. Testing must execute
classes built by the real YIDL/Astichi path, not just handwritten history helpers.

## Repository and generator structure

Use `src/yidl_undoable`, `tests`, `docs`, `dev-docs`, examples and packaging
structure comparable to Lifecycle. Implement the module responsibilities and
inheritable YIDL chain listed in design section 12. Keep history, stable values,
schemas and manager state cohesive rather than accumulating them in one file.

Reuse Lifecycle markers and transaction runtime. Harvester adaptation must not
silently import Lifecycle's generated state or misuse its inheritance metadata.
Feature facts and matcher-selected contributions determine actual generated
constructor/property behavior, including kind, init/default/factory, view and
mutability. Generated classes are plain classes with declared slots; support
records may be dataclasses. Do not hand-patch the generated base.

## Verification gates

The drafter runs focused red/green checks and the final local suite. The lane
owner verifies the final package independently with these gates, using an
available environment with declared dependencies:

```sh
python -m pytest -q
python -m yidl_undoable.regenerate_undoable_base
uv build
```

Run generation twice and compare bytes. Inspect wheel and sdist contents for
Python modules, all YIDL resources and `py.typed`. Build/install the dependency
wheels into an isolated temporary environment; install Undoable's wheel there
and execute the first-use and nested example without sibling source paths or
editable installs. Check installed-resource regeneration from a different cwd.
Missing compatible published dependency versions must be reported honestly;
local dependency-wheel smoke proves the pinned tuple, not arbitrary PyPI parity.

Run supported Python interpreters when available, record their versions, and do
not claim a multi-version matrix from one runtime. Scan committed files for
machine-specific absolute paths, run compile checks, inspect the diff/status,
and preserve unrelated workspace work.

## Runtime acceptance review

Commit the passing implementation checkpoint via scoped GWZ. Generate two
prompts from the review-loop canonical template for the exact settled tuple:
Code with cold Surface walkthrough and State. Include accepted design, this plan,
TDD evidence, test/package results and original design counterexamples. Reviewers
are read-only and peer-blind; file their full reports verbatim. Two is the ceiling.

Any P0/P1/P2 blocks runtime acceptance. Merge all findings into one remediation
plan and patch; add failing regressions before correction and get originating
counterexample closure. Bounded extra cycles are operator-authorized. A broken
architecture requires explicit redesign and fresh review before implementation
continues. An accepted design is not an excuse to dispute a real runtime flaw.

## Experiment evidence and delivery

Record implementation start, TDD tranche completion, full tests, package smoke,
each review/remediation and final delivery in the experiment ledger. Capture
disjoint drafter/reviewer counters alongside the lane-owner counters. Report
elapsed time from both design start and autonomous go-ahead. Actual billing
remains unavailable; label Standard API-equivalent cost as an estimate.

Deliver a working local package, examples and concise user/LLM documentation,
accepted-through revision, verification evidence, known limits and measured
experiment summary. No release tag, push, remote repository or neighboring
package change is authorized by this plan.

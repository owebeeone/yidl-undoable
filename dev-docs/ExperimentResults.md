# YIDL Undoable experiment results

Status: **accepted at `9d18d60e2244183f3f4715577a1356bf85b517a9` after
[Code/Surface](UndoableImplementation-ReviewCode-6.md) and
[State](UndoableImplementation-ReviewState-6.md) both reported GO**. This accepts
the local serialized in-memory runtime and documented API at the pinned tuple.
The following evidence commit changes status/measurements, not runtime bytes.

## Delivered

A working generated transactional data-class package: explicit begin/commit/
rollback, nested Lifecycle joins, immutable sparse field histories, whole-root
undo/redo, multiple roots and child aliases, provisional objects, strict or
last-visible absence, pinned snapshots and candidate validation. Lifecycle's
field markers are reused; constants, ordinary fields, bindings, local stores and
lazy values remain nonversioned, and transient overlays clear on completion.

The actual native generation pipeline uses nine inheritable YIDL layers and
matcher-selected features. The [design](UndoableDesign.md), separate
[TDD plan](UndoableImplementationPlan.md), [implementation map](ImplementationDraft.md),
[API](../docs/API.md), [architecture](../docs/Architecture.md) and two executable
examples are delivered with the code. [TDD evidence](TddEvidence.md) distinguishes
observed REDs from fixture mistakes and records GREEN/refactor checkpoints.

## Timing

| Checkpoint | UTC |
| --- | --- |
| Design baseline | 2026-10-11T13:51:42.490Z |
| Autonomous go-ahead | 2026-10-11T14:02:52.177Z |
| Implementation drafter started after design acceptance/plan | 2026-10-11T14:22:48.193Z |
| Delivery measurement/documentation checkpoint | 2026-10-11T16:28:43.072956+00:00 |

Autonomous elapsed: **2h 25m 50s**. Design-to-checkpoint:
**2h 37m 0s**. The earlier **11m 9.687s** of design
preparation is included only in the latter baseline. Final response/landing after
this checkpoint is outside that duration. No further routine human decisions
were required after the go-ahead. “One-shot” here means one autonomous run;
internal TDD and review iterations are recorded explicitly.

## Observed tokens and cost

| Category | Autonomous baseline | Including earlier design preparation |
| --- | ---: | ---: |
| Input, including cached context | 98,353,563 | 101,097,031 |
| Cached input, subset of input | 95,402,112 | 98,047,104 |
| Cache-write input, subset of input | 0 | 0 |
| Output, including reasoning | 542,909 | 573,235 |
| Reasoning, subset of output | 192,974 | 200,356 |
| Total input + output | 98,896,472 | 101,670,266 |
| Standard API-equivalent USD | $20.87 | $21.64 |

These are latest observed disjoint counters for **18 actors**, with no
inherited parent usage or repeated checkpoint samples added twice. Cached input
counts repeated context reads, not unique product text. Reasoning is not added
to output a second time. Largest observed request input: **202,361 tokens**,
within the ordinary-context pricing assumption used here.

All recorded actors use GPT-6.1 Sol; effort is preserved in the raw observations.
Per-actor totals and estimates are in [autonomous JSON](experiment/final-autonomous.json)
and [design-baseline JSON](experiment/final-design.json); timestamped cumulative
samples and baselines are in [usage.jsonl](experiment/usage.jsonl).
Actors' final observation times range from 2026-10-11T14:06:27.121Z to 2026-10-11T16:28:19.016Z because earlier
actors finished earlier. Pending owner output after its last sample and the final
response are not counted. Missing billing information is unavailable, not zero.

**Actual Codex billing is unavailable.** These estimates apply Standard rates
checked in [official model documentation](https://developers.openai.com/api/docs/models/gpt-6.1-sol):
uncached input $2/M, cached input $0.10/M, cache writes $2.50/M and output $10/M.
They exclude unexposed tool/voice charges, subscriptions and mode/regional
premiums. The [ledger](ExperimentLedger.md) gives the method and checkpoint history.
The two baseline totals overlap and must not be added together.

## Quality evidence

- Design accepted after two bounded remediation cycles: five formal findings closed.
- Runtime accepted at the sixth dual gate after five bounded remediation cycles:
  fourteen formal P2 findings closed by original replay in replacement reviewers.
  The three extra cycles used the operator's authorization. No architectural root
  or redesign was established. There are no open P0/P1/P2 findings at acceptance.
- One State round3 report-delivery attempt ended with a service content flag;
  the same reviewer delivered its full report on retry. An unsuccessful attempt
  without a delivered report/verdict was not counted as an extra review. Its
  exposed usage is included. Every complete report is filed verbatim.
- **215 tests pass independently on Python 3.12.12, 3.13.12 and 3.14.3**. This
  includes twenty canonical executable scenarios and generated-source goldens,
  nine actual intermediate layer executions, and narrow diagnostics/fault tests.
- Independent rebuilt-wheel installation, both examples, generated-base checking
  and import isolation pass on all three versions. The wheel contains all nine
  YIDL resources, generated base and `py.typed`; the sdist contains the tests.
  Source/path/whitespace checks pass. [Verification details](VerificationEvidence.md).

## Other-LLM usability and limits

Fresh same-model Code/Surface reviewers read README/API/examples cold and executed
first-use and undo/redo paths successfully. They independently reconstructed
prior counterexamples from filed reports. This demonstrates procedural usability
by other fresh LLM contexts; it is not a cross-vendor or downstream-application
benchmark. The documentation explains the API, field choices, generated layout,
unsupported cases and canonical testing route.

Acceptance covers the pinned YIDL/Lifecycle/Astichi/YIDL Cache tuple recorded in
the reviews. It does not establish arbitrary older same-version wheels or public
registry installation. This remains a local unpublished member. Disk history,
concurrency/collaboration, multi-key atomic history, resource ownership hooks,
multiple generated bases and arbitrary stored custom-value adapters remain
outside the accepted version. Review/test success is not a guarantee of no
undiscovered defects. No tag, push or release was performed.

# Autonomous Undoable Experiment

Status: running; implementation and quality verdict pending.

## Measurement scope

Goal: determine whether one autonomous LLM-led run can produce a working,
reviewed YIDL Undoable package; measure elapsed time, token usage, estimated
cost, and usability for another LLM. The operator may leave while work continues.
Internal TDD iterations and bounded review remediation are allowed and recorded;
"one-shot" means no further routine human intervention, not a perfect first patch.

The operator permits extra remediation cycles for minor corrections. An
architecturally broken design must be replaced by an explicit redesign and fresh
review, never continued through accumulating patches. Additional rounds and
redesign time remain part of this experiment's cost and duration.

Design started at **2026-10-12 00:51:42 Australia/Sydney**
(`2026-10-11T13:51:42.490Z`), recovered from the first design-request message in
the current session log. Earlier discussion, repository creation, and release
documentation are excluded from this experiment baseline. Instrumentation was
requested during drafting, so the initial sample is retrospective and labeled.

The operator's explicit autonomous-run go-ahead is **2026-10-12 01:02:52
Australia/Sydney** (`2026-10-11T14:02:52.177Z`). Report elapsed time and usage from
that point separately from design preparation. Samples labeled `autonomous-*`
use this second baseline. Do not add their cumulative deltas to the overlapping
design-to-delivery deltas.

Main session: GPT-6.1 Sol, high reasoning, as reported by local session metadata.
Reviewer models/effort and costs are recorded separately when their session
usage is available. Frontend voice usage, unavailable tool fees, subscription
charges, and unrelated concurrent work are not included in backend token totals.

## Token and cost method

The local session log supplies cumulative input, cached-input, cache-write,
output, and reasoning-output counts. Samples record raw cumulative counters and
subtract the last observation before the experiment start. Reasoning output is
a subset of output and is never added twice. Repeated input context is counted
per model request; token totals are not the size of the final document/code.

Samples are written by `experiment/record_usage.py` to
`experiment/usage.jsonl`. Each actor has its own baseline and label. Report the
latest observed counters and their observation timestamp; a tool sample cannot
include the model output that has not yet finished. Missing data is unavailable,
not zero. Aggregate only disjoint actor usage, avoiding inherited parent counts.

Cost is **Standard API-equivalent USD**, not actual Codex billing. Rates checked
on 2026-10-12 in [official OpenAI model documentation](https://developers.openai.com/api/docs/models/gpt-6.1-sol):
uncached input $2/M, cached input $0.10/M, cache writes $2.50/M, output $10/M.
The estimate assumes ordinary-length Standard requests; mode, regional premiums,
and long-context multipliers require per-request evidence and are not silently
inferred. Actual billed cost is unavailable from these session counters.

For a delta with total input I, cached input C, cache writes W, and output O:
`estimate = ((I - C - W) * 2 + C * 0.10 + W * 2.50 + O * 10) / 1_000_000`.
The recorder rejects counter resets/negative deltas rather than inventing usage.

## Checkpoints and quality evidence

Record design start, initial draft settlement, each review dispatch/completion,
each remediation, accepted design, completed TDD plan, implementation start,
focused/full test checkpoints, package smoke, implementation review, and final
delivery. The JSONL observations supply numbers; this ledger supplies meanings.

| Phase | Outcome/evidence |
| --- | --- |
| Design | Both axes GO at `616f2f6` after two bounded remediation cycles. Initial review found constructor reads, callback fencing, and two Surface omissions; round 2 found idle-lazy wording. All five findings closed at design level. No architectural root or redesign. |
| Planning | Separate strict TDD plan created after design acceptance; runtime gate is dual Code/Surface plus State. |
| Implementation | Starting after accepted design and separate plan; outcome pending. |
| Quality | Record canonical tests, narrow fault tests, regeneration, wheel smoke, reviewer findings and verdicts. |
| LLM usability | Cold first-use walkthrough belongs to the Consistency/Surface reviewer; document unsupported behavior and complete examples. |

No success, completion duration, or total cost is claimed until the relevant
work and observations are actually complete.

# GitHub publication

On 2026-10-12 (Australia/Sydney), the operator authorized creating the public
[owebeeone/yidl_undoable repository](https://github.com/owebeeone/yidl_undoable),
configuring Git origin, registering it with GWZ and pushing the member history.
This is subsequent to the completed autonomous experiment.

The publication contains the full member commit history and these records:

- [Original concept](archive/YidlUndoRedoConcept.md), archived with a notice that
  the accepted design supersedes its illustrative API.
- [Detailed design](UndoableDesign.md) and [separate TDD plan](UndoableImplementationPlan.md).
- All verbatim design/runtime review reports, generated reviewer prompts and
  merged remediation plans in this directory.
- [Timestamped TDD evidence](TddEvidence.md), [implementation map](ImplementationDraft.md)
  and [independent verification](VerificationEvidence.md).
- [Experiment ledger](ExperimentLedger.md) and [final results](ExperimentResults.md):
  timing, quality, fresh-LLM usability, observed tokens, cost method and billing limits.
- [Raw sanitized usage observations](experiment/usage.jsonl), both final aggregate
  JSON files and the scripts used to record and summarize those observations.
- Runtime code, nine YIDL generation layers, twenty canonical scenarios and
  generated-source goldens, narrow tests, examples and API/architecture docs.

Runtime sources, tests, package configuration, API documentation, the accepted
design and TDD plan remain unchanged from the independently accepted runtime at
`9d18d60e2244183f3f4715577a1356bf85b517a9`. This publication adds documentation
and remote registration; it does not change behavior or establish a package
registry release. The verification scope remains the pinned dependency tuple.

Original timing and cost baselines close at the recorded experiment checkpoint.
Later API discussion and repository publication are outside those measurements;
recorded estimates are Standard API-equivalent USD, not actual Codex billing.

# Constructor annotation review checkpoint

Date: 2026-10-24. Status: **accepted at
`b50445618cc772cd2a451da66cf1112247269466` after
[Code](ConstructorAnnotations-ReviewCode.md) and
[State](ConstructorAnnotations-ReviewState.md) independently reported GO;
acceptance covers this constructor-annotation fix only**.

## Acceptance ledger

| Object | Code / Surface | State | Owner disposition |
| --- | --- | --- | --- |
| `ca68b8271841931506297db316911fe0ed3ad332..b50445618cc772cd2a451da66cf1112247269466` | GO; no findings | GO; no findings | Accepted in the first review round; no remediation required. |

The two peer-blind reviewers assessed the same committed 40-file object and
verified the complete reference tuple at start and end. Both independently
confirmed live identity and unevaluated strings, exact constructor parameter
parity, generated-artifact equivalence apart from annotation metadata, localized
component scope and unchanged baseline capture limitations. There was no defect
convergence requiring remediation; no finding was self-closed by the implementer.

Each independently ran the focused 25-test module on CPython 3.12.12: Code used
explicit Python, State used explicit native-rust. Both confirmed actual engine
selection without fallback and performed non-writing baseline/patched probes.
State additionally checked per-class dictionary isolation, callbacks, provider
timing, rollback and history. Full-suite, regeneration and Python 3.13/3.14 runs
remain author evidence, clearly distinct from reviewer execution. This does not
qualify other platforms or untested interpreter/backend combinations.

Reports are filed verbatim. Canonical prompts are
[Code](ConstructorAnnotations-PromptCode.md), SHA-256
`7c92535bf8044a07f77c676e13c5c078c4e8d870ff1f78f72302d1bc3f987cb6`,
and [State](ConstructorAnnotations-PromptState.md), SHA-256
`ceaffefdbdf52932ec0884daad0ad2df3b5f87ac88ddbf462a388d186eeea194`.
Both derive from the review-loop canonical template, SHA-256
`3b10ae89cf101c6273d34668eaaeaebf7e030a4c132406e0b234a846665eca58`.
Subsequent audit-only commits do not change the reviewed source bytes.

Reference-only source tuple:

- YIDL: `30eb0d4768f411d8ef1865feb68877017634a401`.
- Astichi: `ce47c629973d8e5a6340ceaa89b0bc3e8788d5fe`.
- Lifecycle: `e979f2412b809e2a8a60eefb942790cef1e715ff`.
- Cache: `f8d883a40d49105ba37fcfdf76d38d1b23af6ea8`.
- Dataclass: `202b01c879eb0ffb724158efe783b379fe522031`.

The fix and review audit may be committed locally under this review directive.
No push, dependency change, tag, deployment or release is authorized by this gate.
The original author record's uncommitted/no-commit status describes its earlier
handoff; this later owner-authorized settled review does not rewrite that history.

## Separate confirmed follow-up

Both reviewers reproduced the existing `schema` capture collision on baseline
and patch. Coverage included schema-named fields/classvars, and Code additionally
confirmed a class itself named `schema`. The practical impact is that otherwise
usable declaration names can fail with `NameError` during generation. A separate
capture-isolation change with canonical class-name and field/classvar collision
coverage is suggested. It demonstrably does not block annotation preservation on
working declarations and is not implemented or authorized by this review.

## Operator authority and scope

The operator identified missing type annotations on Undoable's generated
constructor after comparing it with the corrected Lifecycle constructor. They
requested a separate agent to preserve those annotations and add regression
coverage, then explicitly requested review of the completed fix. Parameters and
runtime behavior must remain unchanged. TDD evidence is recorded in
`ConstructorAnnotations.md`; it is evidence, not independent acceptance.

Deliverables: a committed local review checkpoint, two independent peer-blind
reports, a merged verdict and at most two bounded remediation rounds if needed.
Editable components are Undoable's authored YIDL, necessary owned generation
wiring, generated base/goldens, focused tests, canonical story and related docs.
YIDL, Astichi, Lifecycle, Cache, Dataclass, Pyrolyze, GEARU and GWZ implementation
are reference-only. Supported GWZ operations may settle the local review/audit
commits; this review request does not authorize pushing, tagging or release.

The separate pre-existing classvar named `schema` capture collision is recorded
in `ConstructorAnnotations.md`. Its discovery does not authorize repair here.
Reviewers must distinguish an unchanged baseline defect from a regression or new
annotation-specific collision; the latter remains in scope. Astichi 3.11 stays
proposed. No broader platform qualification or release readiness is asserted.

## Object and gate

Baseline: Undoable `ca68b8271841931506297db316911fe0ed3ad332`.
The local review commit contains the bounded annotation fix, generated artifacts,
API explanation, canonical story, focused regressions, author evidence and this
brief. Record the settled revision in both canonical reviewer prompts; acceptance
must name that exact revision. No unrelated source edits may enter the object.

Gate: dual Code (including Surface) and State review. At most two reviewers per
revision. Original reviewers continue for local corrections; materially changed
architecture/interface premises require replacement reviewers. File complete
reports verbatim; any P0/P1/P2 blocks. Merge all findings into one remediation
patch, with originating-counterexample closure and changed-range analysis.

## Invariants and evidence boundaries

Live annotation objects preserve identity; explicit/postponed strings remain
unevaluated. Effective inherited/overridden constructor fields are included;
non-init fields, classvars and local stores are excluded. Do not invent annotations
for self, the transaction manager or return. Constructor parameter names/order,
required/keyword-only/default/factory behavior, application defaults/factories,
class/schema annotations and transaction/view semantics remain unchanged.

Read the public API cold on the Code/Surface axis. Check the existing supported
capture route and regeneration rather than proposing SDK changes. Assess test
coverage against canonical successful flows and narrow mechanical/negative tests.
Verify initial and final repository revisions. Reference dependencies and previous
platform evidence are read-only; their acceptance does not accept this fix.
Author reports Mac source tests on Python 3.12–3.14 and both engines on 3.12;
reviewers must distinguish recorded execution from their own checks. No claim
extends this to other platforms or untested native/Python combinations.

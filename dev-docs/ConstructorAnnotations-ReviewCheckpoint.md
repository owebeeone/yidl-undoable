# Constructor annotation review checkpoint

Date: 2026-10-24. Status: awaiting a settled review revision and dual review.

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

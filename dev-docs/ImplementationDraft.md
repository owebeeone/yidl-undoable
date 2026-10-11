# Complete implementation draft

Controlling design: `UndoableDesign.md` accepted at
`616f2f65473b1240535a6317d8cc79d5cec18414`. This document records the
implementation drafter's handoff, before independent runtime acceptance.

## Delivered shape

`src/yidl_undoable` contains the decorator, Lifecycle marker exports and schema
adapter, generated base and regenerator, nine inheritable YIDL resources,
transaction coordinator, immutable sparse histories, live facades, candidate
reads, callback fences, stable-value normalization, graph traversal, absence
policies, binding adapters, snapshots, state behavior and named errors.

The pipeline harvests normalized declarations into typed YIDL facts, populates
the generated base container, asks Astichi for executable Python AST and executes
the resulting builder. Matchers select required/default/factory constructors,
field kinds, lazy mutability and default/factory access, transient factory paths,
binding shape, and managed current/working/thaw access. Each intermediate feature
concept executes in the layer fixture. The final generator emits three slotted
facade classes. No handwritten model wrapper or patched generated-base shortcut
is used.

One Lifecycle group manager and one aggregate participant prepare a complete
immutable candidate epoch. Publication replaces one selection reference.
Original backend token-bound scope callbacks are captured, fenced and delegated.
Touched managed fields receive versions; every field and presence history is
trimmed when branching. Snapshots retain prior epochs. Callback installation
checks the original selection, edit, state and backend ownership. Fault diagnosis
distinguishes confirmed publication from unknown state and drops escaped overlays.

`README.md`, `docs/API.md`, `docs/Architecture.md` and two executable examples
explain use and limits. Packaging includes resources and typing metadata with
relative sibling development sources. The minimum tested Astichi is 1.1.3.

## Mandatory design coverage

Every successful story executes actual generated classes before comparing the
materialized executable source in `tests/data/golden`. The numbered rows map
design section 13's groups to canonical stories in `tests/data/gold_src`.

| Group | Canonical evidence |
| --- | --- |
| 1 | `01_initial`: scalar/collection baseline, frame zero, generated declarations. All stories plus generator checks cover deterministic source. |
| 2 | `02_transactions`, `06_field_policies`: explicit/scope completion, managed write guards, nonversioned changes surviving abort and navigation. |
| 3 | `04_topology`: several roots, shared children, add/remove/move edges, alias presence and empty roots. |
| 4 | `02_transactions`, `12_completion_and_containers`: joined nesting, inner commit/abort, stale normal and exceptional scope exits against replacement tokens. |
| 5 | `03_sparse_branch`: sparse predecessor, separate token/cursor/frame identities and touched-only equal versions; narrow history tests cover negative indexes. |
| 6 | `03_sparse_branch`: boundaries, navigation rejection during edits and trimming untouched future histories and presence. |
| 7 | `03_sparse_branch`, `09_atomic_validation`: abort/failure preserves redo, later-node freeze/validation failure publishes no partial state, preview repair. |
| 8 | `04_topology`, `05_absence_snapshots`, `10_stability_and_providers`: all live view propagation, shared-path reachability, strict/fallback absence and descendant fallback pins. |
| 9 | `04_topology`, `05_absence_snapshots`, `12_completion_and_containers`: provisional editing/attachment, removed final nodes, aborted/omitted/future-only handles, unavailable resurrection and foreign-manager edges. |
| 10 | `08_callback_fences`, `09_atomic_validation`, `10_stability_and_providers`, `12_completion_and_containers`: recursive/container stability, detached lists, converter/equality/truth/scope attacks, validator reentry, invalid freeze, managed cycles and immutable nested mappings/frozensets. |
| 11 | `05_absence_snapshots`: prebranch snapshots, nested aliases/pins, strict snapshot absence, unknown fields and exclusion of nonmanaged resources. |
| 12 | `06_field_policies`, `07_construction_providers`, `08_callback_fences`, `10_stability_and_providers`, `11_layers`, `12_completion_and_containers`: all scoped markers, transient baseline/factory/cleanup, lazy policies and idle first reads through every view, named/self providers and contextual recursion, inheritance, native feature layers and pure retry after blocked lazy reentry. Definition tests cover unsupported hooks/ownership and reserved names. |

Narrow tests additionally cover binary search/trim mechanics; binding and schema
recognition; reserved and incompatible inheritance diagnostics; public marker
error parity; stable objects with misleading private attributes; contextual
validator error grouping; application-backed immutable proxy read fences; installed-layout generation; setup/configuration
diagnostics; and synthetic enlist, ownership, publication and cleanup faults.
These do not duplicate each successful canonical story.

## Bounded runtime remediation

The two first runtime reviews were NO-GO at
`a97e43e5010fd22a9bcd008f27072ca656b73f5b`. One merged correction implements
the seven accepted P2 roots; it does not claim originating reviewer closure.

| Finding | Correction and regression |
| --- | --- |
| Code P2-1 | Owning core YIDL supplies explicit empty constructor parameters; normal regeneration. Canonical 13 executes empty, scratch-only, classvar-only and init=False managed schemas with only required transaction_manager. |
| Code P2-2 | Exact working sets recursively project views, preserving the working object and avoiding ordinary mutation of it. Canonical 14 covers both directions, nested sets, untouched child reads and detached escaped sets. |
| Code P2-3 | Named lazy constructor dependencies use the generated/fenced materialization path and never supply unset storage. Canonical 15 covers const/managed consumers, reversed order, setup/provisional creation and single evaluation; narrow errors reject unset/recursive dependencies without registration. |
| State P2-1 | Healthy discard requires unchanged selection; changed selection requires publication evidence. Fault tests distinguish installed identity bookkeeping from unconfirmed assignment, block future mutation and retain known history reads. |
| State P2-2 | Candidate pins preserve active ordinary/working transient behavior; current/historical reads retain baseline behavior. Canonical 16 covers validator rejection, preview repair, redo preservation, factories and fenced scope/write attacks. |
| State P2-3 | SnapshotNode equality/hash uses snapshot-context identity and node ID. Canonical 17 covers frozenset nodes, nested tuple/mapping aliases, cached membership/hash and old snapshots across a branch. |
| State P2-4 | Failed enlist always detaches the overlay; abort failure or incomplete ownership evidence faults with causal failures and available terminal evidence retained. Narrow tests cover abort failure before/after closure and successful abort permitting retry. |

All successful added cases execute the same native YIDL/Astichi path and compare
generated-source goldens. Cycle 1 produced 17 canonical stories and 55 passing local
tests. Earlier three-interpreter evidence applies to the pre-remediation draft;
the lane owner will independently repeat matrix/build/smoke gates for this merged
revision. `TddEvidence.md` records the observed cycle's red/green results.

## Runtime remediation cycle 2

Both second runtime reviews at `72e1433e1290cc41392223c9d5981847e396f68e`
closed all seven original counterexamples, then issued NO-GO for three bounded
remaining roots. This merged correction retains the original regression suite.

| Finding | Correction and regression |
| --- | --- |
| Code round 2 P2-4 | Raw provisional baselines use recursive view projection under the existing fence. Canonical 18 covers current/default input children before/after attachment, nested tuple/mapping/frozenset aliases, pending values, an untouched no-thaw child field and current provisional absence. |
| Code round 2 P2-5 | Provisional projection and thaw run inside one operation-owned call, before touched installation. Ten narrow proxy cases exercise ordinary/working rollback, navigation, begin, rollback/replacement and retained-scope attacks, preserve the original token/root edits and permit pure retry. |
| State round 2 P2-1 | One pre-owned guard covers backend begin, allocation, enlist and wrapper binding. One shared abort helper closes newly acquired or failed joined work only under verified token ownership and terminal evidence; all failures detach overlays. Twenty-one setup/abort cases cover clean retry publishing one frame without hidden nesting, abort failure before/after closure, partial backend return, both scope-bind stages and joined failures. Complementary tests cover unexpected nesting fault persistence and unconfirmed selection after abort failure. |

The local native suite now has 18 canonical stories and 89 passing tests.
No API, YIDL architecture or backend callback authority changed. The guard
captures pre-begin ownership even when backend begin raises before returning its
new token, and keeps ordinary setup exceptions distinct from detected ownership
faults. Current provisional absence and stale backend scope behavior remain as
designed. Root repeats independent supported-version/build/wheel checks and fresh
dual runtime review; no originating closure or acceptance is claimed here.

## Verification and limits

`TddEvidence.md` records actual red/green/refactor tranches, including behavioral
reds after bootstrap, and final commands. Local native Python 3.12.12 suite:
Before runtime remediation, 44 tests passed on Python 3.12.12, 3.13.12 and 3.14.3. The matrix exposed and
test-led correction fixed deferred class annotation recognition on 3.14 through
`inspect.get_annotations`, retaining the native pipeline. Base regeneration,
canonical source checks, compile checks,
wheel/sdist build and content inspection passed. An isolated installed-wheel
environment ran both examples and resource/base checks from a different cwd.
Cold relative-source uv setup passed. Dual runtime review is owned by the lane
owner and is not claimed here.

Limits follow the accepted design: in-memory linear history; one key and one
cursor; explicit lifecycle-managed resource ownership/hooks unsupported;
single generated-base inheritance; no custom immutable-value adapters,
cross-manager edges, persistence, multi-key atomic coordination or concurrent
thread/task isolation. Bindings remain application owned and use Lifecycle's
BindingBase/BindingDict policy. Definition errors alias Lifecycle's type so
re-exported marker factories retain immediate validation. YIDL and Lifecycle
currently use version 0.1.0; dependency wheel evidence applies to the pinned
source tuple, not arbitrary older same-version distributions. This is a complete
local draft for review, not a release or runtime acceptance claim.

# Root-based initialization helper

Status: proposed bounded API addition after the completed implementation experiment.
Operator requested `undoable_leaf(document)`, variadic roots, and rejection of
repeated roots. The original design/runtime acceptance and experiment measurements
remain historical; this change has its own focused dual review.

## Contract

Export `undoable_leaf(root, *roots) -> None` at the package root. The required
first argument prevents an empty call. Each argument must be a constructed
Undoable live handle; ordinary, current and working handles are accepted.
Snapshots and arbitrary objects are invalid and raise TypeError before publication.

Infer the owner from the first root's framework state. All supplied roots must
belong to that same manager; a mismatch raises ForeignManagerError before any
manager is initialized. Repeated roots raise ValueError. Identity is the underlying
node state, so two different views of one node count as a repeat. Distinct nodes
with equal values are permitted. Shared descendants and overlaps between distinct
roots remain supported; only repeated supplied root identities are forbidden.
Validation must not invoke application equality/hash or lookalike manager/state
properties on invalid objects.

Delegate exactly once to the inferred manager's existing `initialize(*roots)`.
Keep its return value None and its initialization, validation, topology, callback
fencing and atomic publication behavior. Successful initialization remains once
per manager; rejected initialization remains retryable. Retain the existing
manager method for compatibility. Later root changes still use add/remove inside
an edit. The helper marks history roots and does not require terminal graph leaves.

## Implementation and verification

Add the helper alongside the public decorator and export it from __init__.
No YIDL resource, generated field accessor or transaction completion changes.
Update README/API and both examples to show the root-based helper. Preserve
original experiment measurements, reports and historical design/plan bytes.

Strict TDD: one new canonical generated-class story proves multiple distinct
roots, nested/shared descendants, successful frame zero, commit, undo/redo and
retry after failed initial validation. Focus narrow tests on repeats (including
view aliases), mixed owners, invalid/empty input, protocol-safe identity checks,
repeated successful initialization and same-manager factory reentry rejection.
Generate only the new golden after its behavior succeeds; existing goldens must
remain unchanged. Run the full suite, generation/base checks and examples; the
owner verifies supported-version and isolated-wheel gates as appropriate.

Review tier: focused dual Code plus cold Surface, and State, at one committed
tuple with this contract as the controlling amendment. At most two reviewers;
NO-GO while any P0/P1/P2 is open. Subsequent user-authorized publication of this
repository permits landing the accepted change on its public origin. This is
outside the original autonomous experiment's measurements.

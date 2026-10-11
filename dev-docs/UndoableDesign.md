# YIDL Undoable Detailed Design

Status: DRAFT for dual review. All APIs and modules in this document are proposed.
Date: 2026-10-12. This is a design for implementation, not a claim of existing
behavior or parity certification.

## 1. Purpose and controlling decisions

Generate ordinary application data classes with Lifecycle-style field policies,
transactional edits, and committed history. A manager selects a frame. Managed
fields resolve their latest stored value at or before that frame. Editing creates
working values; commit publishes another frame; rollback discards the working
values. Undo/redo navigate existing committed frames rather than replay commands.

Operator decisions incorporated here:

1. Begin, commit, and rollback belong to the transaction manager. Managed fields
   are editable only while their transaction is active.
2. A manager coordinates one or more roots and their nested objects. Reading
   from those roots resolves the relationships and values visible in the
   selected committed frame.
3. Historical absence is an accessor policy: raise, or read the last value that
   was visible at or before the selected point.
4. Working access may mark a field as touched without proving a mutation.
5. Store sparse field histories ordered by committed-frame number, with
   predecessor lookup. An ordered array is the first implementation; a B-tree
   remains a possible storage replacement.
6. Constants, local storage, and management data need not be versioned. File
   descriptors and resource bookkeeping must not masquerade as reversible user
   data.
7. Use YIDL/Astichi generation and reuse applicable Lifecycle concepts. Prepare
   enough detail for one cohesive implementation, with adversarial review gates.

This proposal replaces the smaller background concept's one-root scope,
`history=` constructor spelling, `versioned` example marker, and rejection of
nested begins. It keeps successful scope exit committing and exceptional exit
rolling back, as in Lifecycle. The chosen names are `transaction_manager=`,
`managed`, and manager-owned completion. The detailed design is authoritative
for Undoable; it does not amend Lifecycle's own contract.

## 2. Initial scope and explicit limits

Initial implementation includes generated declarations, inherited fields,
constructor defaults, constants, plain fields, local storage, constructor-only
inputs, class values, lazy fields, bindings, transient fields, managed fields,
rooted nested objects, two
absence policies, pinned read-only snapshots, sparse histories, joined nested
transactions, validation, and canonical generated-source coverage.

Each manager has exactly one transaction key and one history cursor. The key
defaults to Lifecycle's `DEFAULT_TRANSACTION`; a caller may configure another
hashable key. Every managed field attached to that manager must use its key.
This retains Lifecycle's single-key nesting and completion semantics. It does
not claim Lifecycle's complete multi-key interface: independent histories use
separate managers. Multi-key atomic history and simultaneous edits under
different keys are deferred. A wrong or unknown key fails before changing state.

History is in memory and linear. A new commit after undo discards redo. Disk
storage, bounded retention, collaborative/selective undo, arbitrary frame
checkout, serialization, change notifications, revision tokens, and resource
ownership protocols are deferred. Deferral does not leave placeholder public
methods that silently do nothing.

Object topology may share a child between parents or roots; aliases retain one
node identity. Cycles in managed child relationships are rejected during
initialization and commit. Single-threaded, externally serialized access is the
contract; there is no thread/task isolation or durable crash recovery.

## 3. Public surface

Distribution: `yidl-undoable`. Import package and member repository:
`yidl_undoable`. Public imports come from its package root.

```python
@undoable
class Node:
    label: str = managed(default="")
    children: tuple["Node", ...] = managed(default=(), thaw=list, freeze=tuple)
    identifier: str = const()
    cache: dict[str, object] = local_store(default_factory=dict)


history = UndoRedoManager()
root = Node(identifier="root", transaction_manager=history)
history.initialize(root)

with history.begin():
    child = Node(identifier="child", transaction_manager=history)
    root.working.children.append(child)
    child.label = "first"

assert history.undo()
assert root.children == ()
assert history.redo()
assert root.children[0].label == "first"
```

Creating an object within a transaction creates a provisional node. It can be
edited before being attached, but only nodes reachable from committed roots
become visible in the published frame.

### Manager methods and defaults

| Member | Contract |
| --- | --- |
| `UndoRedoManager(*, tx_key=DEFAULT_TRANSACTION, absent_policy=None)` | Creates a setup manager. `None` selects `RaiseAbsent()`. The policy is fixed at construction. |
| `initialize(*roots) -> None` | Publishes frame zero from one or more roots; exactly once. Freezes/validates the complete initial graph before publication. |
| `begin(tx_key=DEFAULT_TRANSACTION) -> LifecycleTransaction` | Opens or joins the manager's key. Returns the existing Lifecycle scope/token. Requires initialization. |
| `commit(tx_key=DEFAULT_TRANSACTION) -> int \| None` | Completes one begin. Inner completion returns `None`; outer completion returns the transaction token ID and publishes one frame. |
| `rollback(tx_key=DEFAULT_TRANSACTION) -> int` | Discards the whole joined transaction and returns its token ID. Requires an active transaction. |
| `validate(tx_key=DEFAULT_TRANSACTION) -> None` | Prepares and validates a preview without publishing or closing the active transaction. |
| `active_transaction_for(tx_key=DEFAULT_TRANSACTION)` | Returns the backend's active token for the configured key, or `None`; wrong key raises. |
| `undo() -> bool`, `redo() -> bool` | Moves one frame if possible. Returns `False` at the boundary; requires initialized, healthy, idle state. |
| `can_undo() -> bool`, `can_redo() -> bool` | Reports whether navigation can currently succeed. Returns `False` during editing; uninitialized/unhealthy state raises. |
| `add_root(node) -> None`, `remove_root(node) -> None` | Modifies the working root set in an active transaction. Identity-based, idempotent for an already-added/already-removed same-manager root. Wrong manager raises. |
| `roots` | Immutable tuple of ordinary live root facades: working roots while editing, committed roots otherwise. |
| `current_roots` | Immutable tuple of current facades for selected committed roots, including during edits. |
| `cursor` | Zero-based position in the surviving linear history. Remains unchanged while editing. |
| `frame_id` | Selected frame's immutable ID, distinct from the cursor and transaction token. |
| `frame_count` | Number of surviving frames, including the initial frame. |
| `snapshot() -> FrameSnapshot` | Pins the selected committed epoch/frame, even during editing; never captures pending values. |

For a custom key, callers must pass that key to begin/commit/rollback/validate,
as with Lifecycle's keyed operations. Public `commit_only` is deliberately not
exposed: publication always validates. No generated model convenience methods
delegate completion; completion belongs to the manager only.

Ordinary `with history.begin(key):` behavior is Lifecycle's: normal exit calls
commit; exceptional exit rolls back. Do not manually complete a transaction
inside its scope and then expect successful normal exit: its token is stale and
normal exit raises. Exceptional exit after that same transaction was already
aborted preserves the original body exception, following Lifecycle fencing.

## 4. Field policies and nonversioned storage

Reuse the supported marker factories from `yidl_lifecycle.lifecycle_markers`,
re-exported through Undoable. Do not clone a second set of marker objects. A
consumer adapter translates normalized declarations into Undoable facts.

| Marker | Storage and mutation | Undo/redo effect |
| --- | --- | --- |
| `managed` | Sparse frozen history plus transaction-local overlay; setters require the active key. | Restores the selected historical value. |
| `const` | One instance value; no replacement after construction. Contents are not automatically frozen. | None: reads the same instance reference at every frame. |
| `field` | Ordinary shared instance value, immediately mutable through any facade. | None, including transaction rollback. |
| `binding` | Nonversioned stored binding/resource reference with Lifecycle's declaration/type checks. No generated resource ownership protocol. | None. |
| `local_store` | Shared scratch object; no constructor argument; zero-argument factory evaluated once at construction. | None. |
| `lazy` / `static` | Per-instance first-read storage; write-once reference by default, immediately replaceable with `mutable=True`. | None; first access may initialize it even through a current facade. |
| `initvar` | Constructor-only input; not a facade field. | None. |
| `classvar` | Class storage; no instance constructor parameter. | None. |
| `transient` | Construction baseline plus a token-local working value, optionally created by `working_default_factory`; working setters require the active key. | Clears token-local values on completion; no historical versions. |

Unmarked annotated fields retain Lifecycle's plain `field` interpretation.
Transactional user data must therefore explicitly use `managed`. The compiler
reports the supported marker surface clearly, so an unmarked field is not
silently mistaken for historical data.

`owned`, transaction hook markers other than
`validate_commit`, and `commit_order_key` are rejected with a definition error
in the first version. Resource-bearing values can be explicit `field`, `const`,
or `local_store` management data. Deferring ownership and transient behavior is
a stated scope boundary, not a claim that those Lifecycle features are absent.

Transient fields preserve the executable Lifecycle behavior: current access and
idle ordinary/working access return the construction baseline. Active ordinary/
working access creates the token-local value on first use, using the working
factory if supplied, otherwise the baseline reference. Constructor options and
retained initvar factory providers follow Lifecycle normalization. The baseline
is not replaced on commit. Without a factory, mutable baseline contents remain
shared; use a working factory for fresh mutable scratch data. Neither transient
baseline nor overlay establishes historical child membership. Completion clears
all transient overlays, including on nodes removed from the final graph. A
transient-only edit still produces the ordinary empty managed-history frame.

Defaults/factories are per-instance. Explicit constructor values bypass their
factories. Missing required inputs, conflicting default/default_factory, invalid
local-store options, unsupported kinds, reserved names, and incompatible
inheritance overrides fail at decoration or construction with field context.
Normal factory provider ordering follows Lifecycle's declaration/dependency
rules, including opt-in `allow_self_factory`; first-read lazy factories use
access-time providers. Reuse its harvester's normalized facts where compatible,
with a translation layer and tests rather than unreviewed duplication.

File descriptors are application-owned. Undo, rollback, and branch truncation
do not close or reopen them. A mutable `const` value can still change internally;
the documentation must say reference-constant, not recursively immutable.
Nonversioned fields containing node references do not establish historical
membership. Consumers should put user-visible topology in managed fields.

## 5. Runtime identities and views

`NodeState` has a manager identity and a monotonically assigned node ID. Neither
is reused after rollback or branch truncation. Different managers' equal-looking
IDs never identify the same node. Comparing generated handles uses manager plus
node identity; no structural field equality is implicit. User methods remain
on generated live facades; frame snapshots are data-only objects.

The ordinary generated object is a stable live handle. Its properties resolve
working values while its transaction is active and committed values otherwise.
`node.default` is that same ordinary view. `node.current` always resolves the
selected committed frame. `node.working` requests the transaction overlay;
outside editing it reads the selected committed representation, as Lifecycle
does, and rejects managed writes. Holding these facades does not pin a frame.

Resolving a managed child reference propagates the view: a current parent returns
current child facades; a working parent returns working child facades; ordinary
parent access returns ordinary children. Thus child field access cannot quietly
use a newer frame than its parent. Shared child references resolve to the same
node state, not duplicated data. Container wrappers may be reconstructed, but
node identity remains stable.

Every node exposes read-only `node_id` and `present`. `present` is working graph
membership for ordinary/working views while editing, and committed membership
for current views or idle access. Identity, manager diagnostics, and
nonversioned management fields remain accessible when the node is absent.
Presence policy applies specifically to managed field reads.

### Absence policies

Policies are behavior objects, not enums or magic strings. `AbsentReadPolicy`
is an ABC with a read-resolution method; initially ship two built-in concrete
policies. Arbitrary third-party policy subclasses are not a supported extension
point in v1; the manager checks for the supported implementations.

- `RaiseAbsent()`: an absent managed read raises `ObjectAbsentError`, including
  node and selected-frame context. This is the proposed default, not an earlier
  operator decision about the default.
- `ReadLastVisible()`: find the greatest surviving frame ID at or before the
  selected frame in which this node was reachable, then resolve its managed
  fields at that frame. Never consult a future or abandoned frame. Descendants
  reached through this fallback are pinned read-only to that fallback frame,
  preventing a historical parent/current child mixture. If no such frame
  exists, raise `ObjectAbsentError`.

Neither policy makes an absent node editable. To restore it, insert its handle
into a managed edge/root set during a transaction; it becomes editable when
reachable in the working graph. Nodes created in that active transaction are
the sole exception: provisional nodes can be initialized/edited before reachability.
Retained nodes with no initial/history value at or before the selected frame
cannot be resurrected from the redo tail or an aborted creation; attachment
raises `UnavailableNodeError`.

Management fields deliberately describe today's management state even on an old
live view. This is why live views are not promised as complete historical
snapshots of every attribute.

## 6. Roots, topology, and creation

The manager starts in setup. Constructors using it register initial nodes but
do not publish history. `initialize(*roots)` freezes all managed data reachable
from the supplied roots, validates keys, topology, and node validators, and
publishes frame zero once. It requires at least one root. Failure leaves setup
unchanged and retryable. No snapshots/navigation/editing are available before
successful initialization.

After initialization, construction with that manager requires an active
transaction. Objects created in setup but omitted from the initial rooted graph
have no published baseline and cannot later be attached; construct fresh nodes
inside an edit instead. Newly created nodes keep their constructor values as
private provisional baselines until commit; they are never inserted into the
current frame merely because they exist in Python.

All recursively encountered generated nodes in managed values are managed child
edges. Supported containers are tuples, frozensets, and immutable mappings;
working conversions may use lists/dicts. Immutable mapping keys cannot be nodes;
mapping values may contain them. Sharing is supported; cross-manager edges and
cycles fail validation. Nonversioned fields do not count as edges. No parent
pointer is automatically generated; an application wanting one must keep it
nonversioned or avoid creating a managed cycle.

During editing, traversal uses pending managed values with committed fallback,
and provisional constructor values where appropriate. Read-only traversal does
not itself thaw every field. Compute reachability with a visited set; reject
cycles in final validation, allowing temporarily incomplete topology during an
edit. Recompute working membership when needed rather than trusting a cached
index after an escaped list mutates. This is deliberately simple for v1.

Candidate roots may be empty after root removal. Removing a child/root changes
reachability; it does not destroy its Python handle or close its management
resources. Removal from one parent does not make a node absent if another
rooted path reaches it. Parent fields, membership, and child values publish
together. The final graph determines membership; touched values on previously
present nodes that end the transaction unreachable are not published. Their
last visible committed values remain their restoration baseline.

## 7. Stable values, thaw/freeze, and touch tracking

The baseline of a managed field must be a stable value. The default admissible
values are `None`, booleans, numbers, strings, bytes, recursively stable tuples
and frozensets, framework-created immutable mappings, and internal node
references. Mutable lists/dicts/sets and arbitrary custom values require a
declared conversion that returns a supported stable representation. The
framework validates the result recursively, detects container cycles, and
encodes node references before installing it. The first version rejects custom
objects in stored managed values even if the caller claims they are immutable;
custom stable adapters can be added later under an explicit contract.

For `managed(thaw=list, freeze=tuple)`, working access thaws the committed tuple
once per field/token and records a touched overlay. Repeated access returns the
same working list. Direct assignment records a pending replacement, with
Lifecycle's `compare="value"` or `compare="identity"` replacement guard. These
guards may skip an equal/identical setter operation; touching via thaw does not
claim exact change detection. Scalars without thaw can be read without creating
an overlay. Ordinary reads never initiate thawing.

On assignment, mutable incoming values are transaction-local; publication never
installs the caller's mutable reference. The conversion result is normalized
into privately owned immutable containers, including a fresh backing mapping
when using a read-only mapping wrapper. Working views decode internal node
references to working handles before conversion; frozen storage encodes them
again afterward. Those handles' mutability is controlled by the transaction,
not by the outer tuple/list alone.

Thaw must produce editable data sufficiently separated from its frozen source.
The framework checks that stored baselines use only admitted stable values;
converters remain trusted callables that must not mutate their inputs, produce
external side effects, reenter the manager, or depend on being called once.
Conversion/validation errors carry node/field context.

A retained raw working list may still be mutated after completion, because it
is an ordinary Python list. It has been detached from field-owned state and
must not affect any committed value or next transaction. Generated field
assignment outside editing raises. This intentionally matches Lifecycle's
reference limitation; the API does not promise revocable Python container
references. A retained live child handle still applies current write guards.

Every successful outer commit creates one frame, even when there are no touched
fields or all values compare equal. Each touched, finally reachable field gets
one version record. Untouched fields reuse predecessor values. No-op suppression
and exact mutation instrumentation are optional future optimizations.

## 8. Sparse storage and frame lookup

Handwritten support records are dataclasses, frozen where appropriate. Generated
classes remain plain Python classes with declared slots; no dataclass decorator
is added to generated output.

| Record/object | Owned information |
| --- | --- |
| `FrameRecord` | Immutable frame ID, root node IDs, and reachable node IDs. |
| `FieldHistory` | Immutable sorted frame-ID sequence and corresponding stable-value sequence for one node/field. |
| `NodeHistory` | Field histories and ordered frame IDs in which this node was present; generated schema and stable node identity. |
| `HistoryEpoch` | Immutable mapping of node histories, immutable frame sequence, and any immutable lookup indexes. |
| `NodeState` | Identity, schema, nonversioned slots, and manager link; history access resolves through the manager epoch. |
| `EditOverlay` | Base epoch/frame, token, working roots, touched field values, and provisional nodes. |
| `PreparedCommit` | Complete replacement epoch and next cursor, ready for publication. |
| `PublishedSelection` | Immutable epoch plus cursor; one manager-owned reference is the publication point. |

A node's sparse field history might contain frame IDs `[0, 3, 8]`. At frame ID
6, binary search chooses position `bisect_right(ids, 6) - 1`, thus the value at
3. A negative position is unavailable, never a request for Python's last element.
Node presence uses the frame membership set; last-visible fallback uses the
node's ordered presence history, then field predecessor lookup.

Frame IDs are monotonically allocated integers and never reused, even after
branch truncation or failed preparation. They are not transaction token IDs.
Cursor positions are contiguous within the surviving frame sequence; frame IDs
need not be contiguous. Frame IDs, node IDs, and tokens are manager-local.

An ordered array is sufficient for append-oriented history and logarithmic
lookup. Candidate publication replaces histories rather than mutating arrays
seen by an existing snapshot. Unchanged histories can be shared between epochs;
touched histories get new arrays. This is structural sharing at the storage
boundary, not a dependency on Pyrsistent or a B-tree package.

Complexity: field lookup is logarithmic in that field's stored versions; undo
and redo replace the selection in constant time. Accessing/traversing the tree
still costs the nodes/fields read. Initialization and commit traverse the final
graph. Copying an immutable epoch's outer dictionaries costs its recorded node
count; copying a touched history costs that history's length. Membership history
may grow with every frame a node is present. These are acknowledged v1 costs,
not claims of constant-time commits or bounded memory.

## 9. Branch truncation and snapshots

On commit from a nonterminal cursor, prepare a new epoch containing only the
selected frame and its predecessors, plus the new frame. Trim every field
history and presence history after the selected frame ID, including untouched
fields. Remove node histories with no remaining baseline. Never select a value
by frame-number order across abandoned branches.

Example: a future frame changes field B; undo before that frame, then edit only
field A. The new commit must eliminate B's future version too. Subsequent reads
of B use the surviving predecessor. A failed commit or rollback preserves the
entire redo tail.

`FrameSnapshot` retains its original epoch and selected frame. It exposes
`frame_id`, `roots` (a tuple of `SnapshotNode`), and `node(node_id)` for nodes
present in that snapshot. Missing nodes raise `ObjectAbsentError`, independently
of the live manager's absence policy. `SnapshotNode` exposes `node_id` and
`get(field_name)` for managed fields only. Nested values contain snapshot nodes
resolved within the same pinned epoch/frame. Unknown or nonmanaged field names
raise `AttributeError`.

Snapshots expose no user methods, lazy fields, caches, file descriptors, or live
manager. They cannot be edited or used as live nodes in new topology. They remain
readable after live branch truncation because their old epochs are retained.
Their memory stays allocated until the snapshot is released; discarding redo
does not promise reclamation while clients pin it.

Retained live nodes from discarded future-only frames become unavailable, while
retained snapshot nodes remain readable in their pinned history. A snapshot is
not an API to reactivate an abandoned branch.

## 10. Transaction ownership and publication

Compose, rather than subclass and expose, Lifecycle's `GroupTransactionManager`
for the configured key. Each `UndoRedoManager` enlists exactly one
`HistoryParticipant` when its outer begin succeeds, even for an empty edit.
Generated nodes stage through the Undoable manager and never enlist separately
in the backend. Foreign Lifecycle participants and a generic Lifecycle manager
are rejected at the binding boundary. This gives one completion participant
for all roots/nodes and avoids partial per-node frame publication.

The returned `LifecycleTransaction` owns token fencing and nested scope behavior.
Generated write guards confirm that the backend's active token still matches the
overlay, and that the manager is in editable state. Nested begins join the token;
inner commit decrements the nesting count and publishes nothing. Rollback at
any depth aborts the whole joined edit. A new begin after a caught abort uses a
new token; a stale outer scope cannot commit that replacement transaction.

The aggregate implements Lifecycle's participant callbacks and ordering:

1. `commit_order_key_for` returns a fixed empty tuple; there is only one
   participant. No user-defined ordering is needed.
2. `requires_validation_for` returns false because final frozen-candidate
   validation is performed during prepare, not on a pre-freeze overlay.
3. `_prepare_commit_tx_by_key` freezes touched/provisional data, validates the
   complete rooted graph and generated validators, prepares truncation/new
   histories, and allocates the complete replacement selection. Nothing in
   the published selection is mutated.
4. `_apply_prepared_commit_tx_by_key` installs that one prepared selection by
   assigning the manager's published-selection reference. No converter,
   validator, user hook, or per-node publication runs here.
5. `_rollback_tx_by_key` discards private overlays/prepared state whether called
   after success or failure; it never rewinds an already installed selection.
6. After callbacks contain no user code. They finalize internal bookkeeping
   only; user commit/rollback hooks are not in v1.

Wrap backend scope completion carefully: it must invoke the same aggregate
callbacks as explicit manager commit/rollback. Do not create an outer context
wrapper that bypasses token-bound Lifecycle fencing. Reads after backend scope
completion must not find stale overlays; use its active-token state and the
participant cleanup contract together.

### Validation

Support Lifecycle's `validate_commit` method marker for the manager's key.
Run validators once per reachable node on a read-only prepared-candidate facade
after all conversions and structural validation. Its default/current/working
managed reads all resolve the frozen candidate and never thaw. Nonversioned
fields retain their ordinary semantics, but validators are required to be pure.
Managed writes, topology edits, begin/completion, and navigation from converters
or validators raise `ReentrantOperationError`. Validator false results and
exceptions reject publication. Multiple validator failures are collected in a
`BaseExceptionGroup`, preserving original exceptions and node context.

`validate()` uses the same preparation path for a throwaway preview, leaves the
transaction active, and does not reserve an accepted result. A later commit
prepares and validates again because working values may have changed. Preview
does not consume a frame ID; final prepare may consume one even if it fails.
Preparation uses a guard so converters cannot silently mutate staged data via
generated accessors; arbitrary external mutation is outside serialized access.

## 11. Failure state machine and diagnostics

Manager states are represented by behavior-bearing classes, not enums or string
tags: setup, healthy idle, editing, completing, and faulted. A failed begin must
not leave an editable overlay; aggregate enlistment is rolled back if begin
setup fails. Frame preparation failure publishes nothing and backend completion
discards the edit. For explicit `validate()` failure, only the preview is
discarded and editing remains active.

| Event | Published history | Transaction | Subsequent behavior |
| --- | --- | --- | --- |
| Initialization fails | No initial selection installed | Setup | Caller may correct inputs and retry initialization. |
| Thaw/setter conversion fails | Unchanged | Editing remains active; failed field creation is not touched | Caller can repair or rollback. |
| Preview validation fails | Unchanged | Editing remains active | Caller can repair or rollback. |
| Outermost commit prepare/validation fails | Old cursor/epoch and redo preserved | Aborted and closed by backend | New edit allowed after cleanup is verified. |
| Successful commit | Complete new epoch installed | Closed | Undo can select its predecessor. |
| Rollback | Unchanged, including redo | Whole joined edit closed | New begin gets a fresh token. |
| Unexpected backend ownership/cleanup failure | Determine from token completion evidence and installed selection identity | Faulted | Reject edits/navigation; preserve last confirmed selection for snapshots/diagnostics. |

Expected cleanup uses only framework-owned references and does not invoke user
teardown hooks. Unexpected internal failures are not reported as a clean rollback
when publication happened. Retain the Lifecycle transaction's terminal
`TransactionCompletion` evidence and the prepared/installed selection identity.
If the selected history or cleanup cannot be confirmed, enter faulted state and
raise `HistoryFaultError`; do not guess that the old state was restored.

In faulted state, live managed reads and snapshots are permitted only when the
published selection is confirmed intact; otherwise they raise too. Nonversioned
diagnostics remain accessible. There is no reset/recovery method in v1. Recovery
requires a new manager populated from a confirmed snapshot or application data;
it cannot reconstruct unconfirmed external effects.

Named public errors: `UndoableDefinitionError`, `TransactionRequiredError`,
`ObjectAbsentError`, `UnavailableNodeError`, `ForeignManagerError`,
`GraphCycleError`, `FrozenValueError`, `ReentrantOperationError`, and
`HistoryFaultError`. Definition errors subclass `ValueError`; transaction/state
errors subclass `RuntimeError`; stable-value errors subclass `TypeError`.
Wrap backend errors only where adding context is needed; preserve causes and
original exception groups. Commit's integer result remains a transaction token,
not a frame number. Identity/presence/frame diagnostics do not expose raw mutable
storage dictionaries.

## 12. Generation and reuse architecture

Follow Lifecycle's stages: marker declarations -> harvesting -> typed YIDL facts
-> feature composition through Astichi -> executable AST -> generated builder
with current runtime defaults/converters -> plain generated state/facades.
Do not implement the public feature merely by a handwritten dataclass wrapper
or descriptors while claiming YIDL generation.

Proposed files are relative to this repository:

| Module/resource | Responsibility |
| --- | --- |
| `src/yidl_undoable/__init__.py` | Deliberate public exports; no magic forwarding of unsupported markers. |
| `undoable.py` | Decorator, generated builder binding, AST assembly; parallels Lifecycle's decorator. |
| `undoable_markers.py` | Supported Lifecycle marker adapter and definition diagnostics. |
| `undoable_harvester.py` | Undoable-specific facts, generated reserved names, key/topology/validator metadata. |
| `policies.py` | Presence/absence resolution behavior objects. |
| `history.py` | Epochs, field histories, binary search, snapshots, truncation. |
| `transaction_yidl.py` | Manager, aggregate participant, state transitions, token checks. |
| `values.py` | Frozen-value normalization and node-reference/view conversion. |
| `regenerate_undoable_base.py` | Deterministic YIDL generation/check command. |
| `yidl/undoable_core.yidl` | State/facade/constructor facts and base production. |
| `yidl/undoable_const_static.yidl` | Const and lazy/static feature layer. |
| `yidl/undoable_managed.yidl` | Versioned properties and write guards. |
| `yidl/undoable_default_factories.yidl` | Default-factory dependencies and constructor evaluation. |
| `yidl/undoable_transient.yidl` | Token-local values and working-default factories. |
| `yidl/undoable_binding.yidl` | Nonversioned binding declarations. |
| `yidl/undoable_local_store.yidl` | Shared scratch storage. |
| `yidl/undoable_views.yidl` | View propagation, presence, and candidate validation binding. |
| `yidl/undoable_base.yidl` | Final assembly. |
| `_generated_undoable_base.py` | Checked-in generated runtime/compiler base; regenerated, never hand patched. |

All Python module rows except `__init__.py` are under `src/yidl_undoable/`.
The layout is a cohesion guide; adjust boundaries if implementation shows a
better split without moving generic history behavior into YIDL itself.

Reuse decisions:

- Depend on Lifecycle for its marker factories, normalized declaration concepts,
  transaction scope/manager implementation, and completion evidence.
- Use its harvester as an adapter input for supported metadata. Reject unsupported
  metadata before constructing generation facts. Do not feed Undoable-generated
  bases into its Lifecycle-inheritance lookup: translate and preserve Undoable's
  own schema metadata for inherited classes.
- Reuse YIDL/Astichi compiler entry points and sentinels. Emit Undoable-specific
  history access and state, rather than importing Lifecycle's private generated
  current/working slots into historical storage.
- Review const/local-store/core YIDL templates as semantic and assembly patterns.
  Direct YIDL resource import is allowed only if declared package-resource lookup
  works in a wheel and no private target path or Lifecycle-only generated names
  leak. Otherwise use a small Undoable-owned composition implementing the same
  field behavior, with explicit parity fixtures. No broad Lifecycle extraction
  is required or authorized by this design.
- Do not reuse Lifecycle ownership/binding implementations for rewindable
  resources. Do not require a UI, Pyrolyze, or Pyrsistent dependency.

Packaging uses Python 3.12+ and named distribution dependencies on `yidl`,
`astichi`, and `yidl-lifecycle`, with relative sibling development sources in
`tool.uv.sources`. Include YIDL resources and the generated base in wheels and
source distributions. Lifecycle's transitive cache dependency does not establish
an Undoable cache contract; a dedicated compiled-code-cache adapter is deferred.
Pin/test compatible minimum versions before publication; current source revisions
are evidence baselines, not a promise about all existing 0.1.0 distributions.

Inheritance preserves node identity and one underlying state per instance.
Single generated inheritance is supported; multiple generated bases are rejected
in v1. Stable field IDs survive compatible overrides. An override cannot change
managed/nonmanaged kind or transaction key; compatible annotation/default changes
follow normalization rules and explicit fixtures. Reserved view names,
infrastructure names, and generated storage prefixes cannot be user fields.

### Inheritable YIDL feature layers and matchers

Mirror Lifecycle's incremental concepts, instead of one monolithic management
module. The proposed extension chain is:

```text
UndoableCore
  -> UndoableConstStatic
  -> UndoableManaged
  -> UndoableDefaultFactories
  -> UndoableTransient
  -> UndoableBinding
  -> UndoableLocalStore
  -> UndoableViews
  -> UndoableBase (final assembly)
```

Each feature extends the preceding concept and adds variants to the shared field
family, typed/computed collections, resources, contributions, and matchers.
Match by normalized field facts such as kind, init/default/factory presence,
freeze/thaw availability, view, and mutability. Use YIDL's matcher rules to select
the required/default/factory constructor forms, const versus mutable-lazy
setters, managed current versus working access, and transient factory paths.
Do not substitute a large Python string-template switch for these selections.

Contribution identity/order uses stable field IDs/orders. Production extensions
name explicit phase dependencies for state slots, builder arguments, constructor
evaluation, facade properties, and candidate validators. New feature layers
inherit prior behavior; no layer may silently replace another kind's property
or accidentally duplicate a constructor parameter. Emit current/default/working
facades from the same normalized schema with view-specific matcher selection.

The final generated base contains the full composed consumer. Golden fixtures
exercise intermediate concepts and representative field combinations as well
as the final decorator. Python class inheritance and YIDL concept inheritance
are separate: both must preserve fields, but the latter is the feature-composition
mechanism requested here.

## 13. Canonical verification and implementation planning

After design acceptance, create a separate detailed implementation plan. That
plan must specify a strict red/green/refactor TDD sequence, concrete canonical
fixtures and narrow mechanics tests, commands, dependencies, and acceptance
evidence. The operator authorized autonomous end-to-end completion after adding
this ordering requirement; proceed through the plan and implementation gates
without routine confirmation, preserving any mandatory review-loop stop.

The intended implementation then builds a coherent runtime and generator together;
internal ordering is not a requirement for multiple public rollout phases.
Use test-led work. Add failing canonical fixtures before behavior, implement the
minimal complete path, then regenerate and run focused/full checks. Reviews
must judge actual YIDL-generated behavior, not just handwritten history helpers.

Canonical generated-source fixtures cover:

1. Scalar and collection initial values; first frame; generated source/regeneration.
2. Explicit begin/commit/rollback, context success/exception, write guards, and
   nonversioned changes surviving rollback/navigation.
3. Grouped changes across several roots and shared nested children; add/remove/
   move relationships and empty root sets.
4. Joined nested begins; inner commit does not publish; inner abort closes the
   entire edit; stale scopes cannot complete a replacement transaction.
5. Sparse predecessor reads, absent-history negative indexes, distinct tokens/
   cursor/frame IDs, and touched-only reads creating valid equal-valued versions.
6. Undo/redo boundaries, active-edit navigation rejection, and commit after undo
   trimming untouched future field/presence histories.
7. Failed commit and rollback preserving redo; freeze/validator failure on a later
   node proving no partial publication of earlier nodes.
8. Live current/working/default propagation; strict and last-visible absence;
   shared-path presence; last-visible descendants pinned to the fallback frame.
9. Provisional creation, removed final nodes, rollback-invalidated handles,
   discarded future-only handles, unavailable resurrection, and cross-manager edges.
10. Container/nested stability, retained working lists after completion, converter
    reentry, candidate validator reentry, invalid freeze output, and managed cycles.
11. Snapshots before branch truncation, pinned nested aliases, absence and unknown
    field errors, and management resources excluded from snapshots.
12. Constants, scratch stores, bindings, transient baseline/working-factory/cleanup
    behavior, lazy write policies, factories/provider dependencies,
    inheritance, unsupported markers, and reserved-name diagnostics.

Narrow tests cover binary-search/truncation edge cases, schema recognition,
diagnostic grouping, and synthetic backend ownership/cleanup faults that the
canonical harness cannot express. Do not duplicate all successful golden stories
in bespoke unit tests.

Named implementation gates (commands planned, not run yet):

```sh
uv run --with pytest python -m pytest -q
uv run python -m yidl_undoable.regenerate_undoable_base
uv build
```

Use an isolated temporary environment to install the built wheel and import/run
the first-use example without sibling source paths. Verify packaged YIDL resources
and regenerate/check from the installed package where supported. Run supported
Python-version checks separately when their interpreters are available; do not
claim a matrix from one local interpreter.

Acceptance requires canonical behavior checks, deterministic regeneration,
package smoke evidence, and a dual implementation review at a settled revision.
A passing design review accepts this contract only. It is not runtime acceptance,
a release, or permission to modify adjacent packages silently.

## 14. Review process and evidence baseline

The operator invoked the personal `review-loop` skill. Apply two peer-blind axes:
Consistency plus Surface, and Safety. Settle a committed design revision, record
the exact object and source revisions, file complete reports verbatim, merge
blocking findings into one remediation patch, and permit at most two remediation
rounds. The checkpoint records verdicts and the accepted scope. Interface or
architectural changes replace the two reviewers with fresh contexts; closure
duties stay within those two reviewers, never an extra axis.

No workspace-specific program process documents existed for this new member at
drafting time. This document and `CurrentProgramCheckpoint.md` supply the local
contract; the operator-invoked skill supplies review procedure. Unrelated staged
workspace membership changes and other member work are outside the design commit.
Use GWZ for scoped staging/commits and preserve that other work.

Source evidence inspected at these committed revisions:

| Repository | Revision |
| --- | --- |
| `../yidl-lifecycle` | `230362f642d6e9205897698670fe5f87d2c905ce` |
| `../yidl` | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| `../astichi` | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| `../yidl-cache` | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Relevant Lifecycle references:

- [API/view and keyed completion guide](../../yidl-lifecycle/docs/ManagedContextApiDraft.md).
- [Field-kind matrix](../../yidl-lifecycle/dev-docs/YidlLifecycleFieldKindMatrix.md).
- [Scope ownership and terminal completion evidence](../../yidl-lifecycle/dev-docs/TransactionScopeOwnership.md).
- [Decorator assembly](../../yidl-lifecycle/src/yidl_lifecycle/lifecycle.py).
- [Marker normalization](../../yidl-lifecycle/src/yidl_lifecycle/lifecycle_markers.py).
- [Transaction runtime](../../yidl-lifecycle/src/yidl_lifecycle/transaction_yidl.py).
- [YIDL layered resources](../../yidl-lifecycle/src/yidl_lifecycle/yidl/lifecycle_base.yidl).

The matrix includes older ownership language; current executable code and the
scope/evidence documents control reuse decisions. No promise of safe reversal
of resource acceptance is imported from that older row.

## 15. Proposed choices to confirm before implementation

The review should attack these choices rather than leaving them implicit:
strict absence default; explicit initial-root publication; one key per history;
acyclic managed topology with aliases allowed; built-in stable managed values
only; single generated inheritance; no resource ownership/hooks in
v1; every outer commit creating a frame. These are bounded design defaults, not
claims that the operator individually approved every detail during the discussion.

The design and its review results make those choices reviewable together. If
review finds a required architectural change, revise the design before trying to
force a one-shot implementation around an unsettled contract.

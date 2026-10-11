# API and field guide

Decorate a declaration with `@undoable`, and construct it with the required keyword
`transaction_manager=manager`. Defaults and factories are per-instance; explicit
values bypass factories. Constructor fields are keyword-only. Generated classes
have declared slots and ordinary application methods; support records use dataclasses.
Single generated inheritance preserves field IDs. Kind/key overrides and multiple
generated bases fail at decoration. A declaration without constructor fields,
including an empty declaration, still requires only `transaction_manager=`.

## Manager operations

`UndoRedoManager(tx_key=DEFAULT_TRANSACTION, absent_policy=None)` fixes its key and
absence policy. `None` chooses `RaiseAbsent()`; the other supported policy is
`ReadLastVisible()`. Initialize exactly once with `initialize(*roots)` and at least
one root. Setup views expose constructor baselines without creating history.

`begin(key)` opens or joins a Lifecycle transaction token. `commit(key)` completes
one begin: inner completion returns `None`, outer completion returns the token ID.
`rollback(key)` closes the entire joined edit and returns its token ID.
`validate(key)` freezes/validates a preview and keeps editing; commit validates again.
Pass a custom hashable key explicitly. Its comparison, truth conversion, hashing
and manager/backend diagnostics run inside the same-manager mutation fence.
`active_transaction_for(key)` reports the active token and remains a permitted
read during application callbacks. Authorized backend transitions may change
transaction ownership while retaining this fence.
Normal token scope exit commits; exceptional exit rolls back. Manually completing a
scope makes its subsequent normal exit stale. A stale exceptional exit preserves
the body's exception and cannot abort a replacement edit.

Every successful outer commit publishes a frame, including untouched and transient-only
edits. `cursor` is the surviving zero-based position, `frame_id` is a monotonically
allocated ID and `frame_count` includes frame zero. These IDs differ from transaction
and node IDs. `undo()`/`redo()` return false at boundaries and reject editing.
`can_undo()`/`can_redo()` return false while editing.

`add_root(node)`/`remove_root(node)` edit root membership by identity. `roots` returns
ordinary live roots for the pending graph while editing; `current_roots` always
returns committed current roots. `node.present` follows the corresponding graph;
`node.node_id` and `node.transaction_manager` are read-only diagnostics.

## Fields

| Marker | Reads and writes | Historical behavior |
| --- | --- | --- |
| `managed` | Active ordinary/working setters; current is read-only. Working read optionally thaws once. | Sparse stable frozen versions. |
| `const` | One construction reference; replacement rejects. | Same reference across history; mutable contents remain mutable. |
| `field` | Shared immediate instance storage; unmarked annotations use this policy. | Survives rollback/navigation. |
| `binding` | Shared `BindingBase` or None; map annotations accept `BindingBase` values, normalized to `BindingDict`. | No generated acceptance/ownership actions. |
| `local_store` | No constructor parameter; zero-argument factory evaluated once. | Shared scratch. |
| `lazy` / `static` | One first-read result, through any view; write-once unless `mutable=True`. | No frame or transaction change. Failed factory leaves the target unset. |
| `transient` | Baseline through current/idle; token-local value through active ordinary/working. | Baseline never replaced; overlays cleared on every completion, including removed nodes. |
| `initvar` | Constructor-only input, retained privately for factory dependencies. | Not accessible as a facade field. |
| `classvar` | Class storage; no constructor input. | Nonversioned. |

Managed stable values admit exact built-in scalar types, recursive tuples/frozensets,
framework-owned immutable mappings and node references. Mutable/custom input needs a
`freeze` conversion to this surface. Read-only mapping wrappers are copied into private
immutable backing stores. Mutable working containers can be created with `thaw`. The first working read
recursively projects the converter result's child handles to working views,
including nested containers, before installation. Repeated reads preserve the
owned mutable container; ordinary reads project children to ordinary views.
Result traversal shares the converter's fence, and a failed traversal installs
no touched value, permitting a pure retry.
`compare="value"` compares and truth-converts under the callback fence; `"identity"`
skips only the same reference. Touching via thaw records a version even if equal.

Named factory parameters refer to fields/initvars, `cls`, or opt-in `self`.
Construction evaluates named dependencies in their required order, materializing
a named lazy provider once when needed. An unset lazy provider fails contextually.
Self reads can
only access already-resolved private baselines through all three views; unresolved
and recursive reads fail contextually. Access-time factories can materialize another
provider under the same operation. Controlled nested construction is supported.

`validate_commit(key)` methods run once per reachable node against a complete frozen
candidate. Managed reads through every candidate view read that candidate and
never thaw. Other field policies retain their usual semantics: active ordinary
and working transient reads use token-local values, while current reads use the
baseline. Exact `False`
results and exceptions reject publication; failures are grouped with node context.
Validators, converters and factories must remain pure. The same-manager callback fence
rejects begin/completion, navigation, root changes and managed/transient writes before
changing state. Arbitrary external side effects or escaped mutable-object changes are
outside the serialized purity contract.

## Absence, snapshots and failures

Only managed edges establish membership. Nonversioned references and transient
values do not. Previously visible absent handles can be reattached in an edit; objects
omitted from initialization, aborted creations and future-only objects at an earlier
cursor cannot be resurrected. Removed nodes' touched data is discarded; restoration
starts from their last visible committed baseline.

`RaiseAbsent()` rejects absent managed reads. `ReadLastVisible()` uses only surviving
frames at or before the cursor; descendants are read-only facades pinned to that frame.
Neither policy permits absent managed writes. Management fields remain accessible.
New provisional parents propagate ordinary/working child views before attachment
as well as afterward. Their current managed view remains absent until publication.

`FrameSnapshot.frame_id`, `.roots` and `.node(node_id)` expose only the pinned graph.
A `SnapshotNode` has `.node_id` and `.get(field_name)` for managed fields. Unknown or
nonmanaged fields raise AttributeError; missing nodes raise ObjectAbsentError.
Snapshot nodes have no application methods or setters.
Node equality and hashing use the snapshot instance and node ID; nested aliases
within one snapshot resolve to its cached node, including inside frozensets.

Preparation failure publishes nothing and aborts final commit while preserving redo.
Preview failure leaves editing repairable. Initialization failure remains retryable.
`HistoryFaultError` signals unexpected backend ownership/cleanup evidence. Confirmed
live data and snapshots can remain readable; unconfirmed publication blocks them.
There is no reset/recovery API. `last_completion` retains Lifecycle terminal evidence.
A rejected key callback before backend acquisition preserves the original edit
and nesting unchanged. Once setup has acquired or joined a token, failed begin
setup detaches its private overlay, including when it joined
an existing edit. That joined edit is aborted as a whole. Retry is permitted only
after confirmed clean closure, with no hidden nesting left behind; abort failure
or incomplete ownership evidence faults immediately. Discard cleanup after an incomplete installed publication also
faults, even when the known installed selection remains readable.

Other public errors are `TransactionRequiredError`, `ObjectAbsentError`,
`UnavailableNodeError`, `ForeignManagerError`, `GraphCycleError`, `FrozenValueError`,
and `ReentrantOperationError`. `UndoableDefinitionError` is the public alias of
Lifecycle's ValueError declaration class, preserving immediate errors from the exact
re-exported marker factories. Decoration and provider diagnostics add field/class context.

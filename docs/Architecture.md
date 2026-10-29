# Generation and history architecture

This page describes 0.1.2 and current main. Specialized accessors and compiled-builder
caching were added after version 0.1.1.

Undoable declarations wrap the actual Lifecycle marker factories with immutable
logical comparison/write-policy facts. Lifecycle marker objects and APIs are unchanged. The harvester supplies a
synthetic declaration without generated bases to Lifecycle normalization, then
translates the result and applies Undoable's schema/inheritance checks. Inherited
Undoable field IDs survive compatible overrides.

Typed facts enter the generated YIDL container and Astichi assembly. The assembly
emits an executable builder AST; the builder binds the schema/defaults/converters and
creates three plain facade classes. Generated properties use field-specific straight-line bodies alongside shared runtime
mechanics; field kinds, constructor shapes, lazy policies, binding shape, transient
factory presence, and managed view/thaw selection are chosen by YIDL matchers.

The concept chain is `UndoableCore -> UndoableConstStatic -> UndoableManaged ->
UndoableDefaultFactories -> UndoableTransient -> UndoableBinding -> UndoableLocalStore
-> UndoableViews -> UndoableComparison -> UndoableBase -> SpecializedUndoable`. Extensions add variants, computed collections,
resources, contributions, matchers and ordered phases. Canonical intermediate-layer
fixtures compile and execute each concept independently. `_generated_undoable_base.py`
and `_generated_specialized_base.py` are generated from packaged Undoable resources plus the authoritative comparison
resource loaded from pinned installed Dataclass at regeneration time; the command checks
by default and writes only with `--write`.

`UndoableComparison` inherits Dataclass's neutral `ComparisonCore`, adapting three
facade class surfaces and direct public attribute operands. Globally unique view/
operand ordinals retain per-view field order while avoiding duplicate queued
binding identities in the original Python backend. No handwritten method-source
emitter, AST repair or generic tuple-comparison helper generates the methods. Per-view adapter matching indexes shared productions; explicit outer-binding
references connect class registry/results. The consumer unhashability resource
keeps the public `__hash__` slot under both original backend source profiles.
The generated base records source/resource digests and authority version; its
embedded source needs no runtime Dataclass lookup or manually maintained asset copy.

An adapter-selected equality prelude reads a private ContextVar and delegates an
active marker to the captured historical RuntimeFacade.__eq__ function. It runs
before shared structural guards/operands. An authored constant-True statement
carrier preserves the original hole's statement cardinality; bytecode verification
shows no extra runtime branch. Dataclass selects the empty shared prelude. The
scope helper performs native bool(old == value), closes its bool-only marker and
resets its token inside the existing manager callback fence. There is no recursive
comparator, payload rebuilding, proxy adapter, hash switching or class mutation.

`history.py` owns immutable sparse field/node records, epochs and selection records.
`values.py` owns stable-value normalization and handle projection; `graph.py` traverses
managed edges. `facades.py` owns construction/provider and shared nonversioned mechanics.
`transaction_yidl.py` coordinates one aggregate participant through Lifecycle's
GroupTransactionManager. It captures the original backend token-bound scope callbacks,
fences them, delegates them and diagnoses retained terminal completion evidence.

Preparation freezes and validates a complete rooted candidate, trims every future
field/presence history, and builds a replacement immutable epoch privately. Publication
assigns one manager selection reference. Cleanup discards overlays independently from
that publication; it never undoes an installed epoch. Snapshots retain prior epochs,
so abandoned branches stay readable only through their pinned snapshots.

Lookup uses binary predecessor search, explicitly rejecting negative positions.
Undo/redo select a new cursor over the same epoch. Commits copy outer mappings and
touched version arrays; traversal, node retention and presence histories are unbounded
in this first in-memory implementation. Working membership is recomputed because raw
lists may escape. Converters are trusted to return separated editable/stable data;
completion freezes private immutable copies before detaching working references.

Operation-owned fences capture selection, state, overlay and token identity, nesting
count and token key before calling application code. Nested provider reads share that
context. Results install only if the captured context remains intact. Behavior-bearing
Setup/Idle/Editing/Completing/Faulted state objects control lifecycle transitions.
Unexpected completion failures retain confirmed history and reject further editing.

Compiled model-builder code optionally uses YIDL Cache; see [cache controls](Cache.md).
The package has no GUI, ownership protocol, history persistence, notification or recovery
facility. Lifecycle resource bindings remain nonversioned and application-owned.

Comparison captures use private generation-only aliases disjoint from all three
public class identifiers. Internal ClassId/CmpClassId associations select direct
authored references to an immutable carrier of the original ContextVar and
historical equality/hash/order descriptors. No field-name dispatch, callback
substitution or descriptor rebinding occurs. Class creation keeps public names,
including observations by supported subclass hooks/metaclasses.

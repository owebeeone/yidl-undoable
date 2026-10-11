# Generation and history architecture

Declarations use the actual Lifecycle marker factories. The harvester supplies a
synthetic declaration without generated bases to Lifecycle normalization, then
translates the result and applies Undoable's schema/inheritance checks. Inherited
Undoable field IDs survive compatible overrides.

Typed facts enter the generated YIDL container and Astichi assembly. The assembly
emits an executable builder AST; the builder binds the schema/defaults/converters and
creates three plain facade classes. Generated properties call cohesive runtime
mechanics; field kinds, constructor shapes, lazy policies, binding shape, transient
factory presence, and managed view/thaw selection are chosen by YIDL matchers.

The concept chain is `UndoableCore -> UndoableConstStatic -> UndoableManaged ->
UndoableDefaultFactories -> UndoableTransient -> UndoableBinding -> UndoableLocalStore
-> UndoableViews -> UndoableBase`. Extensions add variants, computed collections,
resources, contributions, matchers and ordered phases. Canonical intermediate-layer
fixtures compile and execute each concept independently. `_generated_undoable_base.py`
is generated exclusively from packaged YIDL resources; the regeneration command checks
by default and writes only with `--write`.

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

The package has no cache, GUI, ownership protocol, persistence, notification or recovery
dependency. Lifecycle resource bindings remain nonversioned and application-owned.

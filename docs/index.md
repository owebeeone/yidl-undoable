# Make a change. Undo it. Redo it.

YIDL Undoable generates Python model classes with transactional managed fields
and frame-based history. A committed edit becomes one history step across your
managed object graph. You choose which fields participate; management state can
remain outside history.

Begin with [your first undo](GettingStarted.md). You need ordinary Python classes
and a `with` statement; no YIDL or Lifecycle knowledge is required.

| You want to… | Read |
| --- | --- |
| Try a complete example | [Getting started](GettingStarted.md) |
| Understand what undo restores | [Frames, fields and views](Concepts.md) |
| Append or remove collection items | [Collections](Collections.md) |
| Group edits and reject invalid candidates | [Transactions](Transactions.md) |
| Add children, remove roots, retain handles | [Object graphs](ObjectGraphs.md) |
| Compute initial values from other fields | [Initialization](Initialization.md) |
| Keep values after navigation or branching | [Snapshots](Snapshots.md) |
| Choose value equality or identity | [Comparisons](Comparisons.md) |
| Control class-generation caching | [Cache](Cache.md) |
| Look up every operation and field rule | [API reference](API.md) |

A transaction's rollback discards pending managed changes. Undo selects an older
committed frame. Neither reverses external I/O, closes resources, nor restores
ordinary nonversioned fields. This is an in-memory model facility, not a database
or a persistence system.

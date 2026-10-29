# YIDL Undoable

> **Full documentation:** [User guides and API reference](https://owebeeone.github.io/yidl-undoable/).

Make an edit to a Python model, undo it, and redo it. Declare which fields belong
to history; Undoable supplies guarded transactions and a shared history for the
root objects and their managed descendants. You do not need to write YIDL.

```python
from yidl_undoable import UndoRedoManager, managed, undoable

@undoable
class Document:
    title: str = managed(default="Draft")

history = UndoRedoManager()
document = Document(transaction_manager=history)
history.initialize(document)
with history.begin():
    document.title = "Ready"
assert history.undo() and document.title == "Draft"
assert history.redo() and document.title == "Ready"
```

Install with `python -m pip install yidl-undoable`. The package targets CPython
3.12–3.15; see the [installation qualification](docs/GettingStarted.md#installation)
for platform/dependency limits.

Start with [your first undo](docs/GettingStarted.md), then learn
[frames and views](docs/Concepts.md), [collections](docs/Collections.md), and
[nested objects](docs/ObjectGraphs.md). The [public API](docs/API.md) gives the
complete contract. The searchable documentation site is
[owebeeone.github.io/yidl-undoable](https://owebeeone.github.io/yidl-undoable/).

History is in memory and linear. A new commit after undo discards redo.
Only managed data is restored; caches, ordinary fields and external resources
are not rewound. Live handles follow the selected frame; use a
[snapshot](docs/Snapshots.md) to retain old committed managed values.

Version 0.1.2 adds field-specific generated accessors and optional
[compiled-builder caching](docs/Cache.md). Version 0.1.1 does not include these
additions; the transaction API remains the same.
The [original experiment](dev-docs/ExperimentResults.md),
[accessor experiment](dev-docs/SpecializedAccessorExperiment.md) and
[cache probe](dev-docs/SpecializedAccessorCacheProbe.md) preserve separate evidence
and measurement limits. Contributor details live in [CONTRIBUTING.md](CONTRIBUTING.md);
releases use [Gearu](RELEASE.md).

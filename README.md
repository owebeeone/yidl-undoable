# YIDL Undoable

Generate application data classes with transactions and frame-based undo/redo.
Managed data has immutable sparse histories; caches, constants and resources have
shared nonversioned storage. Python 3.12 or newer is required.

The implementation is accepted after independent Code/Surface and State
review. See the [experiment results](dev-docs/ExperimentResults.md) for the
TDD evidence, Python-version checks, elapsed time, observed cost and scope.

```python
from yidl_undoable import UndoRedoManager, const, local_store, managed, undoable

@undoable
class Document:
    name: str = const(default="document")
    items: tuple[str, ...] = managed(default=(), thaw=list, freeze=tuple)
    cache: dict[str, object] = local_store(default_factory=dict)

history = UndoRedoManager()
document = Document(transaction_manager=history)
history.initialize(document)
with history.begin():
    document.working.items.append("first")
assert history.undo() and document.items == ()
assert history.redo() and document.items == ("first",)
```

The manager owns begin, commit, rollback and validation. A successful outer scope
exit publishes one frame; an exceptional exit rolls back the entire joined edit.
Unmarked annotations are ordinary `field` values. Use `managed` for data that
rollback and navigation must restore.

`node.default` is the ordinary live handle. It reads pending values while editing.
`node.current` reads the selected committed frame; `node.working` may thaw a field
once in the active transaction. Child views propagate through managed relationships.
Holding these handles follows the cursor. `history.snapshot()` instead pins committed
managed data, including nested aliases, across later edits and branches.

Initialize one or more same-manager roots after setup construction. New objects
require an edit after initialization; provisional objects can be edited before
attachment. Managed relationships must be acyclic; aliases and empty final root
sets are supported. Strict absent reads raise by default. `ReadLastVisible()`
resolves prior visible data and pins descendants to that fallback frame.

Supported markers are Lifecycle's `managed`, `const`, `field`, `binding`,
`local_store`, `lazy`/`static`, `transient`, `initvar`, and `classvar`.
`validate_commit(DEFAULT_TRANSACTION)` marks a pure candidate validator.
Constants keep one reference; their contents can still change. Bindings require
Lifecycle `BindingBase` values (or mappings of them). Resources remain application-owned;
undo never closes, accepts, reopens or rewinds them.

History is in-memory and linear. Committing after undo discards redo; prior snapshots
retain their original epoch. One manager has one key and cursor. Disk persistence,
resource ownership/hooks, multiple generated bases, custom stored stable-value
adapters, thread/task isolation and multi-key atomic edits are outside this version.
Callbacks must be pure; same-manager transactional reentry is rejected. Escaped
working containers remain ordinary Python objects but are detached on completion.

See the [API and field guide](docs/API.md), [generation architecture](docs/Architecture.md),
[executable examples](examples/first_use.py), and [TDD evidence](dev-docs/TddEvidence.md).

Development uses relative sibling sources with `uv`. The tested dependency tuple is
YIDL and Lifecycle source revisions recorded in the accepted design, plus Astichi
1.1.3. Both YIDL and Lifecycle currently identify as 0.1.0; local wheel tests establish
that pinned source tuple, not compatibility with every older wheel bearing the same
version. No package release is claimed.

```sh
uv run --with pytest python -m pytest -q
uv run python -m yidl_undoable.regenerate_undoable_base
uv run python tests/regenerate_golden.py
uv build
```

## Autonomous implementation experiment

The [experiment results](dev-docs/ExperimentResults.md) record **2h 25m 50s**
from autonomous go-ahead (**2h 37m** including earlier design preparation),
**$20.87 Standard API-equivalent estimated cost**, and **215 tests passing**
on Python 3.12–3.14. Actual Codex billing is unavailable. Final Code/Surface and
State reviews both reported GO after five bounded runtime correction cycles.

The [complete experiment record](dev-docs/README.md) includes the archived
original concept, design, TDD plan and observed red/green evidence, every
review/report/prompt/remediation plan, supported-version and isolated-wheel
verification, timestamps, raw sanitized token counters and cost calculations.
The [publication record](dev-docs/Publication.md) distinguishes this later
GitHub upload from the completed experiment's measurements.

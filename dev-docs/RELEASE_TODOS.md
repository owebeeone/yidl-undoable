# Release readiness — 27 October 2026

Initial audit baseline: `db7f004`. The later operator-authorized Python 3.15 pass
is complete and **0.1.1 is published**. See `Python315Release.md` for the release
commit, successful publication workflow, dependency tuple and verification.

## Completed release work

- [x] Check source behavior on CPython 3.12–3.15 with both explicit backends.
  Every cell passed **376 tests**, in both Gearu candidate and exact-commit rounds.
- [x] Align the optional shared comparison authority with published Dataclass
  **0.1.1**, preserving SHA256
  `2f7e6df989b0714d8764de84d8a6f6b03f39c3ad7f57dba5e55f5131b8354eef`.
  Regeneration changed only its version provenance comment.
- [x] Generate the four 3.15 canonical source outputs through the normal helper.
- [x] Verify wheel/sdist metadata, fresh installed examples and regeneration on
  all four minors and both backends.
- [x] Configure Gearu and `publish.yml`; publish through the operator's trusted
  publisher for `owebeeone/yidl-undoable`, workflow `publish.yml`, environment Any.
- [x] Verify the published four-package tuple outside the workspace on final
  CPython 3.15.2, with both backends. Commit/rollback, undo/redo, branching,
  shared comparisons and installed regeneration passed.
- [x] Include README metadata, public documentation, the first-use example and
  experiment records in the appropriate distributions. Historical acceptance,
  time and token/cost records retain their original scope.

The qualified tuple is YIDL 0.1.2, Lifecycle 0.1.1, Astichi 1.1.3, yidl-cache
0.1.0 and compat-sentinel 0.1.2. Dataclass 0.1.1 is an optional regeneration-time
authority, not a required runtime dependency. Existing runtime dependency ranges
were retained. Initial 3.12–3.14 source runs also passed 376 tests per minor; the
3.15 baseline initially had nine missing-golden/old-authority failures, resolved
by the changes above rather than counted as passing.

## Known field-name limitation

A declared field named `schema` still collides with a generated capture:

```python
from yidl_undoable import undoable, managed

@undoable
class Model:
    schema: int = managed(default=1)
# NameError: name 'schema' is not defined
```

This pre-existing issue is documented in README/API and
`ConstructorAnnotations.md`; it was not fixed or hidden by this compatibility
pass. Use a different field name. A future bounded consumer-owned capture
isolation fix is preferable to changing YIDL/Astichi.

## Paused feature

`undoable_leaf(root, *roots)` remains a proposal in `UndoableLeaf.md`, neither
exported nor implemented. The operator paused that discussion; release work did
not resume it. The public API remains `history.initialize(*roots)`. If resumed,
its duplicate check must compare underlying node identity, including aliases
through different views, rather than application equality.

## Evidence boundary

The initial audit changed no production files. The later authorized release
updated the regeneration pin/header, tests, documentation, metadata and release
automation; transaction/runtime semantics are unchanged. The package now caps
Python below 3.16. Current evidence covers 3.12–3.15 locally and on Ubuntu, not
Windows 3.15. Astichi 1.1.3 has cp312/cp313/cp314 Windows wheels but no cp315 or
Windows abi3 wheel; a source build was not qualified. No Astichi/Cache change was
implemented as a hidden release prerequisite.

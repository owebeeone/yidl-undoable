# Release readiness — 27 October 2026

Reviewed member: `db7f004` on `main`. Scope: inspect current Undoable behavior,
tests and release packaging; record findings. This pass does not implement the
paused root helper or modify the transaction runtime, SDKs or Lifecycle.

## Verification

| Source run | Result |
| --- | --- |
| CPython 3.12.12, automatic native-rust selection | 376 passed |
| CPython 3.13.12, automatic native-rust selection | 376 passed |
| CPython 3.14.3, automatic native-rust selection | 376 passed |

Selection probes report native-rust without fallback. Source and freshly installed
wheel regeneration pass with the original Dataclass 0.1.0.dev0 regeneration
authority. Wheel and sdist build successfully. A fresh temporary environment
installed this wheel and the Dataclass candidate from local artifacts, resolving
all runtime dependencies from published wheels: YIDL 0.1.0, Astichi 1.1.3,
Lifecycle 0.1.0, yidl-cache 0.1.0 and compat-sentinel 0.1.2.

Installed-wheel transactions, commit/rollback, undo/redo, branching and snapshot
creation passed. The 25 constructor-annotation tests also passed against the
installed wheel on the explicit Python lowering backend. These are current local
checks, not new independent review or a new cross-platform campaign.

## Findings and release tasks

- [ ] Resolve or explicitly document the existing `schema` field-name collision.
  This fails during decoration, even using the installed wheel:

  ```python
  from yidl_undoable import undoable, managed

  @undoable
  class Model:
      schema: int = managed(default=1)
  # NameError: name 'schema' is not defined
  ```

  The generated class body uses an outer `schema` capture while defining a field
  with that same name. This is the pre-existing issue recorded in
  `ConstructorAnnotations.md`, not an annotation regression. A bounded
  consumer-owned capture-isolation fix is preferable to changing YIDL/Astichi.
  Alternatively state the name restriction clearly for this release; passing the
  suite does not mean arbitrary field names are supported.

- [ ] Align the optional regeneration authority with the final Dataclass release.
  `pyproject.toml`'s `regenerate` extra and
  `src/yidl_undoable/regenerate_undoable_base.py` currently require exactly
  `yidl-dataclass==0.1.0.dev0`. The proposed first Dataclass release is 0.1.0.
  Update both pins together, retain/check the authoritative comparison digest,
  regenerate the provenance header, then verify regeneration with the released
  wheel. This affects regeneration, not Undoable's runtime dependencies.

- [ ] Confirm the runtime dependency tuple for publication. The existing tuple
  installs successfully; Lifecycle 0.1.0 and Dataclass's current supported route
  pin YIDL 0.1.0 even though YIDL 0.1.1 is now available. Supporting the newer YIDL
  is a separate compatibility decision, not a reason to modify dependencies.

- [ ] Prepare Undoable's own publication workflow/trusted publisher when it is
  selected for release. The publisher supplied by the operator in this session
  is for `owebeeone/yidl-dataclass`, not this repository. PyPI returned no
  `yidl-undoable` project during this check.

## Paused feature, not a hidden release prerequisite

`undoable_leaf(root, *roots)` is proposed in `UndoableLeaf.md` but is not exported
or implemented. The current public API remains `history.initialize(*roots)`.
The operator previously paused that discussion; this audit does not resume it or
silently add it to the release requirements. If resumed, its supplied-root
duplicate check must compare underlying node identity, including aliases through
different views, rather than application equality.

## Boundary and evidence limits

No production files changed in this member during the audit. No SDK/Lifecycle
changes, tag, push or registry publication were performed. The package's
`requires-python >=3.12` has no upper bound, while current evidence covers
3.12–3.14; do not imply that later minors were tested.

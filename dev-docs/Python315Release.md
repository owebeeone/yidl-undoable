# Python 3.15 release qualification

The operator included Undoable in the four-package compatibility/patch release
pass. Target version: **0.1.1**, its first PyPI publication. Release tooling is
Gearu; trusted publishing uses repository `owebeeone/yidl-undoable`, workflow
`publish.yml`, and no named GitHub environment.

On final CPython 3.15.2, the unchanged source baseline passed **367 tests**. Nine
failures identified missing 3.15 canonical files and the unavailable old
Dataclass 0.1.0.dev0 regeneration authority; they are not recorded as passing.
The release updates the optional authority pin to the published Dataclass 0.1.1,
checks its unchanged SHA256, regenerates provenance and adds 3.15 canonical
outputs before full verification on both backends and all four minors.

The existing `schema` field-name collision is documented as a release limitation;
this compatibility pass does not silently change field semantics or implement the
paused root helper. Astichi and Cache remain reference-only. Final source,
installed-artifact and publication results will be recorded after verification.

The selected publication tuple is YIDL 0.1.2, Lifecycle 0.1.1, Astichi 1.1.3,
yidl-cache 0.1.0 and compat-sentinel 0.1.2. Dataclass 0.1.1 is required only by
the regeneration extra and release checks. The existing runtime dependency
ranges remain unchanged; this record identifies the exact qualified tuple.
MacOS/Linux qualification does not certify Windows 3.15: the pinned Astichi
release has cp312/cp313/cp314 Windows wheels but no cp315/Windows abi3 wheel.
That separate dependency packaging finding is documented in Dataclass's
`dev-docs/Python315DependencyFindings.md`; no Astichi edit is included here.

## Published authority and 3.15 verification

The clean regeneration environment resolved the published YIDL 0.1.2, Lifecycle
0.1.1 and Dataclass 0.1.1 tuple, checked the comparison digest, and regenerated
the base. Only the provenance version comment changed; all generated
implementation bytes and the authoritative shared-resource SHA256 are unchanged.
The four new 3.15 source goldens were generated through the canonical helper.
The complete 3.15.2 suite then passed on each explicit backend: **376 passed**
for Python lowering and **376 passed** for native Rust lowering.
The workflow YAML, release-only upload condition and embedded shell syntax were
checked before the Gearu release gate.

## Completed publication

Published **0.1.1** using Gearu 0.1.1. Release commit:
`44e1a2fbc2ad3563d4f76c1016f2185a7705ca7e`.

- GitHub release: https://github.com/owebeeone/yidl-undoable/releases/tag/v0.1.1
- Successful trusted publication: https://github.com/owebeeone/yidl-undoable/actions/runs/40498363068
- PyPI wheel and source distribution: https://pypi.org/project/yidl-undoable/0.1.1/

Candidate and exact-commit checks passed for every declared Python minor.
Local and Ubuntu source matrices include 3.12, 3.13, 3.14 and 3.15.
Both explicit Python and native Rust lowering backends passed.

A fresh registry-only installation of all four released packages passed the
combined integration probe on CPython 3.15.2 with each explicit backend. It
verified freezing, Lifecycle fields/annotations, transactions, rollback, history
navigation/branching, shared comparisons and installed Dataclass/Undoable
regeneration. The previously excluded YIDL downstream Lifecycle smoke separately
passed against the published pair on 3.15.2.

The cross-package evidence, per-cell counts, workflow/tag checks and PyPI artifact
SHA256s are recorded at:
https://github.com/owebeeone/yidl-dataclass/blob/main/docs/validation/releases/python315.json

These are qualification results, not new independent reviews or new performance/
cost measurements. Windows 3.15 remains outside this pass: Astichi 1.1.3 has no
cp315 Windows wheel. No Astichi implementation change was made.

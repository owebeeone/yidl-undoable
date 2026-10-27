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

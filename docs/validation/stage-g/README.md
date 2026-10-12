# Undoable Stage G distribution support

Only consumer packaging and test inspection changed; runtime source/resources
remain exact owner-verified E/F bytes. Public README/API/Architecture and the
existing first-use example are now wheel resources under documentation/, retaining
their docs/examples relative layout. New sdists include public consumer material,
not private validation/experiment archives or unrelated paused UndoableLeaf docs.
Those original files remain untouched. Original SDK/Lifecycle wheels were not
changed or rebuilt.

G01 records an actual independently built-wheel missing-public-resource RED and
same-target GREEN. Later relative-link layout assertions are verification. Source
inspection uses the imported package's resources; installed child smoke defeats
source PYTHONPATH when wheel-installed. Missing-authority diagnostics are later
verification, not a manufactured RED. Source gates pass (distribution plus eleven
comparison/source/authority targets). Runtime correctness was not changed.

The paired Dataclass-owned Stage G installed gate verifies this consumer from
external test-only trees and isolated -I original-SDK environments on all three
minors/both backends. With build authority, 341 runtime tests pass in each run;
with Dataclass distribution absent, 334 pass in each, with explicit build-only/
cross-consumer exclusions. Packaged regeneration/authority failures run in the
with-authority corpus. Both consumer wheels reproduce byte-identically from their
sdists, and final package/example/regeneration smokes pass all six selections.
The Dataclass-owned paired artifact tuple and installed JUnit preserve exact
provenance; this owning folder preserves Undoable's source/packaging evidence.

No dependency build, publication, benchmark result or new runtime capability is
claimed. SDKs/Lifecycle and paused Undoable docs remain outside the writer scope.
Cold public-only authoring and H/final review remain owner work. Raw bytes remain
externally content-addressed at external:yidl-undoable-stage-g-raw; this folder's
QA/manifest validates each own sanitized/raw hash and unchanged E/F source tuple.

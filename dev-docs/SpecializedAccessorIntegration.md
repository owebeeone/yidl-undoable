# Specialized accessor and code-cache integration

User authorization, 29 October 2026: integrate the new Undoable implementation,
reuse the existing regression suite, add the necessary cache checks, then move
on. Dataclass documentation proceeds independently in its own repository.

## Boundary and requirements

Editable: Undoable's authored YIDL, generated builder artifacts, decorator/cache
adapter, explicit cache dependency, relevant existing tests/goldens, focused
cache integration coverage, and user/developer documentation. SDKs, Cache,
Lifecycle and Dataclass implementation remain reference-only. No package release
or dependency version upgrade is authorized or needed. The pre-integration
uncommitted experiment is preserved as a patch and untracked-file snapshot under
ignored scratch storage; its original measurement records retain their scope.

- Normal `undoable` selects field-specific accessors with existing public API,
  field policies, facades, snapshots, transactions and comparison semantics.
- Ship a pre-generated specialized builder; runtime use must not require the
  optional Dataclass regeneration authority or compiling the YIDL extension.
- Use existing `yidl-cache` for compiled model-builder code, never live classes,
  namespaces, schemas, callbacks or defaults. Hits execute/bind fresh runtime
  objects. Retain generated-source inspection on hits.
- Capture producer dependencies before generation; fingerprint only audited
  structural inputs. Unknown identity/storage safely bypasses. Support explicit
  disable and directory controls, and observable cache diagnostics/maintenance.
- Existing semantic/canonical tests remain the primary regression coverage.
  Update source goldens because accessor bodies intentionally change. Add narrow
  cold/warm/fresh-process, runtime-rebinding and invalidation coverage.
- Independent review precedes pushing. Package publication remains separate.

The bounded [cache probe](SpecializedAccessorCacheProbe.md) establishes mechanism
and timings for one model; it does not substitute for this integration's tests.

## Delivered implementation and regression evidence

The normal decorator now selects the shipped specialized builder and optional
compiled-builder cache. Cached code includes inert generated-source metadata, so
hits preserve source inspection while executing a fresh namespace and binding the
current schema, defaults, annotation objects and callbacks. The original dynamic
adapter remains an explicit experimental route; the production path does not
compile its extension at import. YIDL, Astichi, Lifecycle and Cache sources were
not changed. Cache is now an explicit pinned dependency at its already-used 0.1.0.

The original prototype's subsequently edited source is preserved in
[the archive](archive/specialized-prototype/README.md); raw measurements remain
unaltered. New source goldens reflect the intentionally specialized bodies.
Three stories additionally preserve exact native source, whose private capture
alias spelling differs from Python lowering; no normalization hides that source.
This SDK hygiene difference is not a demonstrated semantic defect or a blocker;
no SDK change was needed.

Validation on macOS arm64, using published dependency packages:

| CPython | Python backend | Native Rust backend |
| --- | --- | --- |
| 3.12.12 | 414 passed | 414 passed |
| 3.13.12 | 414 passed | 414 passed, installed built wheel |
| 3.14.3 | 414 passed | 414 passed |
| 3.15.2 | 414 passed | 414 passed |

These are the same 414 tests repeated per configuration, not 3,312 distinct tests.
The existing semantic/canonical stories are unchanged. New focused checks cover
cold misses, memory hits, fresh-process disk hits with assembly forbidden, fresh
runtime defaults/factories/annotations/classes, source inspection, structural
identity, clearing, disabled caching and unavailable-storage bypass. The full
3.12 Python suite also passed a second cache-enabled run. Historical prototype
behavior tests continue to exercise its explicit dynamic route.

Two initial verification issues were resolved without runtime changes: source
goldens needed updating for new accessor bodies; old local 3.13/3.14 environments
had the wrong regeneration authority. Isolated environments with the declared
Dataclass 0.1.1 build extra passed. Native-only private alias spelling was recorded
in explicit goldens rather than represented as behavior failure.

All eight public examples and eighteen guide code blocks pass against source and
the built wheel. The strict site has fourteen HTML pages, 434 local links/assets
and 35 search entries. Independent adversarial review reports
[GO](documentation/AdversarialReview.md), with three documented wording/reference
fixes and no established cache-seam defect. No new performance claim is made by
these regression timings; the earlier bounded measurements retain their limits.

Publication here means GitHub main and the documentation site. The current PyPI
0.1.1 package predates this integration; a separate Gearu patch release is required
to publish the updated package. No release tag or registry publication is included.

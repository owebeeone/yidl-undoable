# Constructor annotation preservation

## Authorized boundary

Deliverables: a TDD fix for annotations on the actual generated constructor,
regenerated owned base/canonical outputs, regression coverage, and verification
evidence. Changes are limited to Undoable authored resources, necessary local
schema/builder wiring, owned generated files, tests, and related documentation.
YIDL, Astichi, Lifecycle, Cache, Dataclass, Pyrolyze, GEARU, and GWZ are reference-only.
No dependency changes, commits, pushes, tags, or publication are authorized.

## Implementation and provenance

The requested behavior is preservation of field annotations in
`__init__.__annotations__` and ordinary `inspect.signature(Model)` introspection.
The core YIDL class template now assigns a new annotation dictionary after
defining `__init__`, reading live annotation objects from the already captured
schema's effective field facts. No new schema, builder argument, literal binding,
dependency, or runtime type enforcement is needed.

The mapping includes inherited fields, overrides, constructor-only inputs,
required fields, defaults, factories, and lazy fields. It excludes non-init
fields, classvars, and local stores. Live built-in and application types retain
identity; explicit and postponed strings retain their original contents without
evaluation or additional quoting. Class/schema annotation behavior is unchanged.
Parameter names/order, keyword-only status, required/default/factory sentinels,
live defaults/factories, and the transaction-manager parameter remain unchanged.
No annotations are invented for `self`, `transaction_manager`, or the return.

## TDD evidence

Tests preceded the production edit. The regression module deliberately has no
future-annotations import; the postponed case uses explicit compilation with
`dont_inherit=True`.

| Stage | CPython / explicit engine | Result |
| --- | --- | --- |
| Initial focused RED | 3.12.12 / python | 23 failed on missing annotations, 1 passed |
| Canonical story RED | 3.12.12 / python | Live `Payload` signature annotation assertion failed |
| Initial focused GREEN | 3.12.12 / python | 24 passed |
| Canonical story GREEN | 3.12.12 / native-rust | Construction, factory bypass, default identity, undo/redo passed |

The initial RED command was:

```sh
ASTICHI_LOWER_ENGINE=python YIDL_LIFECYCLE_CACHE=off PYTHONDONTWRITEBYTECODE=1 \
  ../.venv/bin/python -m pytest tests/test_constructor_annotations.py -q
```

The focused assertions cover seven field families through required/default/factory
paths, inheritance/overrides and exclusion, explicit/postponed unresolved strings,
zero constructor inputs, annotation identity, signature metadata, and unchanged
class/schema metadata. A later focused case also covers mutable lazy fields.
One initial test assumption about parameter order was corrected to match the
existing signature: `transaction_manager` precedes the generated field parameters.
No production parameter ordering was changed.

The canonical `25_constructor_annotations.py` story verifies required and defaulted
values, live default/factory identity, initvar factory providers, explicit factory
bypass, construction, current/working views, undo, and redo.

## Regeneration and final verification

Baseline: Undoable `ca68b8271841931506297db316911fe0ed3ad332` plus this uncommitted
patch. Host: macOS 26.6.2, arm64. Reference packages report YIDL 0.1.0,
Astichi 1.1.3, Lifecycle 0.1.0, and regeneration authority Dataclass 0.1.0.dev0.
The Python 3.12 environment uses the reference workspace sources, including the
Lifecycle annotation fix at `77b0dd574404e314fecc46069a54f8fcedb9555d`.

All final full runs use `python -m pytest tests -q`,
`YIDL_LIFECYCLE_CACHE=off`, and `PYTHONDONTWRITEBYTECODE=1`:

| Interpreter | Environment | Explicit engine | Result |
| --- | --- | --- | --- |
| CPython 3.12.12 | `../.venv` | python | 376 passed |
| CPython 3.12.12 | `../.venv` | native-rust | 376 passed |
| CPython 3.13.12 | `.venvs/py313` | python | 376 passed |
| CPython 3.14.3 | `.venvs/py314` | python | 376 passed |

Set `PYTHONPATH=src` on the 3.12 commands so standalone regeneration imports this
checkout rather than its installed package copy. The existing 3.13/3.14
environments use this same reference-source tuple:

```sh
PYTHONPATH=src:../yidl-lifecycle/src:../astichi/src:../yidl/src:../yidl-cache/src:../yidl-dataclass/src
```

Each route's `select_effective_lower_engine().snapshot()` reports the explicit
requested engine as selected, with `fallback_scope=None`, `reason_key=None`, and
`reason_detail=None`. The 3.12 native extension passes `native_self_test()` and has
SHA-256 `8266d234e9de1767b04c7a8291727b70164d3e6376f2562651252fa363f895c5`.
No native build or dependency installation was performed.

The generated base and 3.12 canonical outputs were regenerated through the existing
commands with explicit native-rust:

```sh
python -m yidl_undoable.regenerate_undoable_base --write
python tests/regenerate_golden.py --write
```

The four version-specific comparison stories were also regenerated using their
existing 3.13/3.14 Python environments. All 32 changed existing canonical ASTs
match their baseline after removing only the new constructor annotation assignment.
The new canonical golden was generated from its passing story. Full suites verify
canonical equality and generated-base reproducibility. `git diff --check` and
Black's Python-3.12 check of both new authored Python files pass.

The patch is ready for review; it is uncommitted. These local runs do not qualify
Windows/Linux or native engines for Python 3.13/3.14. Original-candidate platform
results remain separate. No further implementation is required for this fix.

## Separate finding outside this fix

**Confirmed existing capture-name defect; does not block this fix.** A declaration
containing `schema: str = classvar(default="shadow")` and
`value: int = managed(default=2)` raises `NameError: name 'schema' is not defined`
while building the generated class. A bounded probe generated the same declaration
with the committed HEAD base loaded through `build_composable(...,
generation_module=...)` and the patched base; both failed identically. The class
attribute shadows the runtime schema capture. This limits an otherwise accepted
field name. A separate change should isolate captures from declaration names and
add canonical collision coverage. No collision policy or adjacent generator code
was changed here.

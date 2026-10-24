# Constructor annotations — CODE-AXIS REVIEW

**Review object:** Undoable `b50445618cc772cd2a451da66cf1112247269466`, the complete 40-file change from `ca68b8271841931506297db316911fe0ed3ad332`, including controlling DRAFT `dev-docs/ConstructorAnnotations-ReviewCheckpoint.md`. Locally committed, awaiting independent acceptance.
**Baseline:** Undoable `ca68b8271841931506297db316911fe0ed3ad332`; reference sources: YIDL `30eb0d4768f411d8ef1865feb68877017634a401`, Astichi `ce47c629973d8e5a6340ceaa89b0bc3e8788d5fe`, Lifecycle `e979f2412b809e2a8a60eefb942790cef1e715ff`, Cache `f8d883a40d49105ba37fcfdf76d38d1b23af6ea8`, Dataclass `202b01c879eb0ffb724158efe783b379fe522031`. Baseline bytes were read with `git show`; settled sources were inspected in their unchanged checkouts.
**Date:** 2026-10-24.
**Axis:** Code, including Surface: architecture, interfaces, generated artifacts and compatibility. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: GO** — no P0, P1, P2 or P3 findings against this patch.

---

## 0. Evidence base

Read the workspace `AGENTS.md` and `AGENTS_GWZ.md`, then `dev-docs/CurrentProgramCheckpoint.md` for historical boundaries. Read `docs/API.md` cold before implementation or design material. Subsequently read the complete Code assignment, review-loop skill and canonical template, `ConstructorAnnotations-ReviewCheckpoint.md`, and `ConstructorAnnotations.md`. The assignment’s SHA-256 matched `7c92535bf8044a07f77c676e13c5c078c4e8d870ff1f78f72302d1bc3f987cb6`.

Inspected:

- `src/yidl_undoable/yidl/undoable_core.yidl:40–194`, particularly the new assignment at lines 63–67 and constructor matchers at lines 170–176.
- The complete generated-base diff, including its embedded template and provenance digest.
- `src/yidl_undoable/undoable.py:25–145`, `undoable_harvester.py:57–156`, and `undoable_markers.py:20–100`.
- Lifecycle’s effective-field harvesting, constructor-annotation filter, marker normalization and collision checks at the pinned source revision.
- All 140 lines of `tests/test_constructor_annotations.py`, the new canonical story and its 119-line golden.
- Existing layer/removal stories, canonical capture and regeneration wiring, and generated-base verification wiring.

Executed the expressly permitted focused test:

```sh
PYTHONPATH=src:../yidl-lifecycle/src:../astichi/src:../yidl/src:../yidl-cache/src:../yidl-dataclass/src \
ASTICHI_LOWER_ENGINE=python YIDL_LIFECYCLE_CACHE=off \
PYTHONDONTWRITEBYTECODE=1 PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
../.venv/bin/python -B -m pytest tests/test_constructor_annotations.py -q -p no:cacheprovider
```

Result: **25 passed in 0.68s**.

Additional permitted, non-writing, in-memory probes established:

- Python **3.12.12**; requested and selected engine both `python`; `fallback_scope`, `reason_key` and `reason_detail` all `None`.
- All **32 changed existing golden files**, containing **209 new assignments**, are otherwise AST-identical to baseline after removing only constructor-annotation assignments.
- The generated base’s embedded ClassBundle AST matches the authored YIDL template, and its resource SHA-256 matches the source.
- Normalizing embedded source locations and removing that one assignment makes the complete generated-base AST equal to baseline.
- Baseline constructors lack annotations; patched constructors preserve annotation identity and identical parameter names, kinds and defaults.
- Four capture-related class names and three classvar names introduce no new collision. Fourteen marker/init combinations maintain exact parameter/annotation-set parity.
- A nested `typing.Annotated`/`ForwardRef` object retains identity without resolution.
- A first-use construction, factory-bypass, current/working-view and undo/redo probe passes. An explicitly mismatched constructor value remains accepted, confirming absence of new runtime type enforcement.

The initial class-name sweep stopped on `schema`; a comparative rerun confirmed the same failure on both exact generated bases.

No full suite, regeneration, builds, installations or network operations were performed. The author’s 376-test Python 3.12–3.14 runs and native-engine results remain recorded author evidence, not independently rerun results.

All six repository revisions matched the required tuple at both start and end. Final dependency statuses were clean. Undoable had no tracked modifications and only the two authorized reviewer prompt files untracked. No files were modified.

## Problem, requirement provenance, and scope

The operator identified that Undoable accepts constructor field parameters but omits their declared types, and requested preservation with regression tests. The separate review request authorizes independent assessment of that fix. Preserving parameter and transaction behavior is an explicit requirement; broader generator or dependency work is not.

The baseline omission was reproduced using the baseline generated base loaded in memory through the existing `build_composable(..., generation_module=...)` route. The patched route preserves live objects already available in effective schema facts. Thus the existing supported capture route demonstrably works: no SDK, dependency or infrastructure prerequisite is necessary.

The remedy is localized to Undoable’s authored core template. Its generated base, canonical outputs, focused metadata regressions, successful canonical story and related documentation fall within the stated component boundary. No schema/builder implementation or reference dependency changed. A broader annotation transport mechanism would add unnecessary scope here.

The tests follow the workspace coverage rule: metadata recognition and exclusion mechanics receive focused tests, while successful construction and history behavior are represented in the canonical story.

The recorded schema-classvar capture defect was independently reproduced unchanged on baseline and patch. It neither results from this change nor prevents annotation preservation for supported declarations. It remains a separate improvement, not a prerequisite. No unsupported scope expansion or blocking requirement-provenance gap was found.

## 2. Invariant analysis

### Effective fields and live annotation identity

The assignment reads each annotation directly from `schema.fields`; it does not render, quote, evaluate or reconstruct annotation objects. The harvester merges inherited annotations and overrides before producing those effective facts.

The filter includes init-enabled constructor fields and excludes classvars and local stores. Source inspection of constructor matchers, the focused tests and fourteen additional marker/init combinations found no mismatch between annotations and actual constructor parameters. Required, defaulted, factory, lazy, constructor-only, inherited and overridden fields are covered. Explicit and postponed unresolved strings retain their original contents.

The dictionary is freshly created for each generated constructor. The focused inheritance test also confirms that generating a child leaves its base’s constructor annotations unchanged.

### Surface

The cold API description at `docs/API.md:3–15` accurately describes the changed introspection surface and its limits.

`inspect.signature(Model)` exposes effective field annotations while retaining:

- Required `transaction_manager`, with no invented annotation.
- Existing field order and keyword-only status.
- Required/default/factory sentinel behavior.
- Unannotated `self` and return value.

No new public argument, command or lifecycle operation is introduced. The first-use probe exercised the documented constructor and manager route through initialization, mutation, undo and redo without needing an additional API. Annotation metadata does not enforce types.

### Runtime and generated-artifact compatibility

The production change executes once during generated-class construction, after defining `__init__`. It does not alter the constructor body, defaults, factories, schema metadata, manager calls or facade properties.

The 32-file canonical AST comparison provides direct evidence that existing generated behavior changed only by addition of annotation metadata. The complete generated-base AST comparison also rules out an unrelated generated implementation change beyond embedded source-location offsets.

The authored/generated template match and resource digest support generated-base parity. Full regeneration and canonical execution remain author evidence because this review’s command boundary excludes rerunning them.

### Capture names and errors

The new comprehension variable does not collide with tested class or classvar names `fact`, `fields` or `annotation`. Tested class names also included `__init__`. Forward-reference contents are not used as executable names.

The documented `schema` classvar failure occurs identically on baseline and patch. A class itself named `schema` also fails identically on both, with a free-variable `NameError`. These are existing capture limitations, not new annotation regressions.

### Scope and standing source rules

The full committed range stays within Undoable-owned resources, generated artifacts, tests and related documentation. Added committed lines contain no machine-absolute path matches. No C-style control-flow or conditional-compilation migration is claimed or required by the modified code.

## 3. Risks and next action

Independent execution covers Python 3.12.12 with the explicit Python engine only. Python 3.13/3.14, native-engine execution, full-suite results and regeneration are supported by the author’s recorded evidence, with its stated platform limits.

The unchanged `schema` capture limitations remain suitable for a separately authorized follow-up: isolate generator captures from declaration names and cover both classvar and class-name cases canonically. Both failures were reproduced on baseline and patch; they limit usable names but do not block this deliverable.

**Review finished; no user decision or remediation is required by this axis.** Return this report through the subagent callback for verbatim filing and the lane owner’s verdict merge. This GO applies only to the exact reviewed tuple and bounded annotation change; it does not authorize publication or release.
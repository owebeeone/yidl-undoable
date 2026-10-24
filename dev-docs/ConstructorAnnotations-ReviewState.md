# Constructor Annotations — STATE-AXIS REVIEW

**Review object:** Undoable `b50445618cc772cd2a451da66cf1112247269466`, the complete 40-file range `ca68b8271841931506297db316911fe0ed3ad332..b50445618cc772cd2a451da66cf1112247269466`. Locally committed, not pushed. Controlling DRAFT: `dev-docs/ConstructorAnnotations-ReviewCheckpoint.md` at the reviewed revision.

**Baseline:** Undoable `ca68b8271841931506297db316911fe0ed3ad332`. Reference-only sources: YIDL `30eb0d4768f411d8ef1865feb68877017634a401`; Astichi `ce47c629973d8e5a6340ceaa89b0bc3e8788d5fe`; Lifecycle `e979f2412b809e2a8a60eefb942790cef1e715ff`; Cache `f8d883a40d49105ba37fcfdf76d38d1b23af6ea8`; Dataclass `202b01c879eb0ffb724158efe783b379fe522031`. Sources were read from the working trees, verified against the settled HEADs; baseline generated sources were read with `git show`.

**Date:** 2026-10-24

**Axis:** State: annotation/schema isolation, capture hazards, construction and provider semantics, views, transactions and history compatibility. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: GO** — zero P0, P1, P2 or P3 findings.

---

## 0. Evidence base

Read before reviewing:

- `dev-docs/CurrentProgramCheckpoint.md`, establishing the historical acceptance boundary and subsequent additions.
- Root `AGENTS.md` and `AGENTS_GWZ.md`.
- The complete canonical STATE assignment, whose SHA-256 independently matched `ceaffefdbdf52932ec0884daad0ad2df3b5f87ac88ddbf462a388d186eeea194`.
- The supplied review-loop skill and review-prompt template.
- `dev-docs/ConstructorAnnotations-ReviewCheckpoint.md`, `dev-docs/ConstructorAnnotations.md` and `docs/API.md`.

Inspected the complete changed-file inventory and production diff, including:

- `src/yidl_undoable/yidl/undoable_core.yidl:40–81`, constructor generation, annotation installation and generated views; constructor matchers and phases at lines 141–191.
- The generated-base change and its embedded template provenance.
- `tests/test_constructor_annotations.py:1–140`.
- `tests/data/gold_src/25_constructor_annotations.py:1–50` and its complete generated golden.
- All 32 modified existing golden ASTs.
- Unchanged implementation context: `undoable.py:25–145`, `undoable_harvester.py:39–156`, `facades.py:9–95`, canonical harness selection/capture, and relevant Lifecycle normalization and field-fact construction.

Executed the permitted focused command with the specified source `PYTHONPATH`, cache disabled, bytecode disabled, plugin autoload disabled and explicit native engine:

```text
../.venv/bin/python -B -m pytest tests/test_constructor_annotations.py -q -p no:cacheprovider
25 passed in 0.33s
```

Independent engine inspection reported CPython 3.12.12, requested and selected engine `native-rust`, `fallback_scope=None`, `reason_key=None`, `reason_detail=None`; `native_self_test()` returned `True`.

Read-only in-memory analyses established:

- All 32 changed existing golden ASTs equal their baseline ASTs after removing only the new annotation assignment: 209 assignments removed.
- All 210 annotation assignments across changed goldens, including the new story, have the exact intended comprehension.
- Generated-base AST equivalence after removing that assignment from embedded template source and normalizing shifted source-line metadata.
- The authored core resource hash matches generated provenance.
- No machine-absolute paths occur in added lines.
- `git diff --check` passed.

In-memory baseline/patched differential probes used the committed baseline generated module loaded without creating files and supplied explicitly through `build_composable(..., generation_module=...)`. They exercised capture names, providers, defaults, lazy timing, constructor rejection, views and history.

The initial and final HEAD checks matched every required revision. Reference working trees were clean. Undoable contained only the two authorized untracked reviewer-prompt outputs; no tracked changes appeared. No files were modified.

## Problem, requirement provenance, and scope

The operator observed that Undoable accepts generated constructor field parameters but omits their declared types from constructor introspection. The requested outcome is preservation of those annotations, with regression coverage, while parameter and runtime behavior remain unchanged. The subsequent review directive authorizes this independent review and the local checkpoint.

The remedy is localized: after defining each generated constructor, install a fresh dictionary containing effective constructor fields’ annotation objects from the already captured schema. The existing supported schema-capture and generation route delivers the requested result. The focused tests and baseline/patched probes demonstrate feasibility without dependency or infrastructure changes.

An additional builder argument or annotation serialization route is unnecessary: schema facts already retain the live objects. Reading those facts avoids introducing evaluation or reconstructing annotation expressions.

All changed components fall within the authorized boundary: Undoable’s authored generation resource, generated base, owned canonical outputs, focused tests, canonical story and related documentation. No neighboring implementation changed. Dependencies remained reference-only at the exact tuple. No unsupported prerequisite or unauthorized scope expansion was found.

The existing `schema` capture-name limitation is independently confirmed below. It restricts an existing declaration name, but does not prevent this annotation outcome on working declarations. It supplies no authority to change capture policy or dependencies during this fix.

The successful runtime story uses the existing canonical harness; bespoke coverage concentrates on metadata mechanics and exclusions. Historical platform acceptance was not treated as acceptance of this patch.

## 2. Invariant analysis

**Fresh dictionaries and schema isolation.** The comprehension creates a new dictionary for each generated constructor. Independent probes confirmed distinct dictionaries for a base, decorated child and unrelated model. Replacing, adding and deleting dictionary entries did not alter peer dictionaries, schema annotation mappings or field facts. A subsequently decorated grandchild still obtained the original effective schema annotations. Annotation values intentionally retain shared object identity; dictionary isolation does not imply deep copying those values.

**Effective inheritance and exclusions.** The focused tests passed for inherited fields, overridden types, an override becoming non-init, constructor-only inputs, hidden fields, classvars, local stores and a declaration with no constructor inputs. The mapping follows the schema used by constructor generation. It does not invent annotations for `self`, `transaction_manager` or return values.

**Identity and evaluation hazards.** Live annotations retain identity through `__init__.__annotations__` and `inspect.signature`. Explicit and postponed unresolved strings remain unchanged without evaluation. An additional opaque annotation whose repr, equality and hash operations raise survived decoration, construction and signature inspection; the new assignment invoked none of those operations.

**Capture collisions.** Baseline/patched differential probes covered fields and classvars named `schema`, `fact`, `fields`, `annotation`, `field_kind`, `state`, `_HAS_DEFAULT_FACTORY`, `base_cls` and `Model`, plus class names overlapping relevant captures. Outcomes matched. In particular, the comprehension variable `fact` did not interfere with declaration fields or classvars.

A `schema` field or classvar reproduced the existing `NameError` on both baseline and patch. The already recorded classvar case therefore remains an unchanged limitation, rather than an annotation regression. Other tested names construct successfully and expose annotations. This limitation does not block the requested outcome. A separately authorized capture-isolation change could address it with canonical collision coverage.

**Constructor and provider behavior.** Required arguments, keyword-only boundaries and default/factory sentinels passed the focused tests. Differential runtime probes preserved default object identity, named initvar providers, explicit factory bypass and deferred lazy evaluation. Constructor-only inputs remained hidden from facade access. Actual baseline and patched builders also preserved retry after an initial lazy-factory exception. Missing-manager and positional calls still raised `TypeError` without changing the history cursor or frame count.

**Views and history.** Differential probes initialized a model, edited managed and transient fields, read current and working views, committed, undid, redid, rolled back an exceptional scope, and constructed an additional root inside an edit. Values, callback counts and transient reset behavior matched baseline. Reading a lazy value through different views materialized it once.

**Mutation and transaction call graphs.** The annotation assignment runs during generated class creation. It reads immutable schema containers and stores metadata on the new constructor function. It adds no manager operation, provider invocation, instance mutation, transaction transition or history publication. Independent AST comparison confirms unchanged constructor bodies, accessors and other executable golden behavior after removing the metadata assignment. Shared runtime implementation is unchanged.

There is no persistence change or new filesystem state machine in this object. Crash durability and restart protocols would be unrelated requirements.

## 3. Risks and next action

Independent execution here covers CPython 3.12.12 with native-rust on the current host. The author’s recorded full-suite, regeneration and Python 3.13/3.14 results remain author evidence; I did not rerun those gates. This review does not qualify other platforms or untested interpreter/backend combinations.

The unchanged `schema` capture limitation remains a separate follow-up opportunity. No defect found in this review requires remediation.

The STATE review is finished, with no blocker or user decision required. The next action is for the lane owner to file this report verbatim and merge the two independent verdicts for the exact reviewed revision. This final report is returned through the subagent callback; no Codex thread was messaged.
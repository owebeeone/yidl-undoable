# TDD execution evidence

Commands below run from this member repository with the workspace Python environment.
Only observed failing runs are counted as red; generated source is materialized after behavior passes.

- 2026-10-11 14:23:42 UTC — RED 1: `PYTHONPATH=src ../.venv/bin/python -m pytest -q tests/test_canonical.py`.
  Canonical `01_initial` failed importing `undoable`; package did not exist. This initial import red covers bootstrap only.
- 2026-10-11 14:26:40 UTC — GREEN 1: canonical bootstrap passed through native Astichi executable AST.
  Refactor: optional additive holes receive explicit template fallbacks; deterministic generated base regenerated.
- 2026-10-11 14:26:40 UTC — RED 2: focused `-k 02` failed at missing `UndoRedoManager.begin`.
  Implemented one Lifecycle aggregate and joined scope completion; green initially exposed stale overlays after success.
- 2026-10-11 14:27:31 UTC — GREEN 2: `PYTHONPATH=src ../.venv/bin/python -m pytest -q tests/test_canonical.py`: 2 passed.
  Refactor: successful aggregate completion drains the same private overlays as rollback; retained lists detached.
- 2026-10-11 14:27:45 UTC — RED 3: canonical `-k 03` failed at missing `can_undo`; separate `tests/test_history.py` failed at missing `FieldHistory.trim` (negative predecessor already rejected).
- 2026-10-11 14:27:56 UTC — GREEN 3: full suite 4 passed. Refactor: immutable histories trim all fields and node presence before appending a branch; no mutation of prior epoch.
- 2026-10-11 14:28:13 UTC — RED 4: topology story failed shared child presence after initialization (only roots were recorded).
- 2026-10-11 14:29:00 UTC — GREEN 4: full suite 5 passed. Refactor: shared graph traversal supports final cycle rejection and read-only working membership without thaw; original Lifecycle scope callbacks captured and delegated. Test expectations corrected to preserved single backend exceptions, rather than invented groups.
- 2026-10-11 14:29:23 UTC — RED 5: absent policy export missing; after snapshot/policy scaffolding and correcting the fixture's edit-before-removal order, the behavioral assertion failed: absent parent's child resolved the child's newer value rather than the parent's fallback frame.
- 2026-10-11 14:30:09 UTC — GREEN 5: full suite 6 passed. Refactor: a single committed resolver accepts immutable fallback pins; snapshots use data-only cached node aliases. Reattached working nodes bypass committed absence only when actually reachable.
- 2026-10-11 14:30:32 UTC — RED 6: new field-policy canonical failed class-value generation (conflicting ident/external binding name); after correcting the YIDL port, failed calling missing `_u_read_static`.
- 2026-10-11 14:30:53 UTC — GREEN 6: full suite 7 passed. Refactor: shared nonversioned storage, token-local transient scratch, lazy single materialization; normalized inherited facts preserve stable field IDs.
- 2026-10-11 14:31:15 UTC — RED 7: constructor-provider story exposed a managed assignment reaching normal absent-node handling while the private constructor was unfinished.
- 2026-10-11 14:31:24 UTC — GREEN 7: full suite 8 passed. Refactor: generated managed setters reject construction writes contextually; named dependencies resolve privately in dependency order, self reads use only already-resolved baselines, failed constructors register no node.
- 2026-10-11 14:31:54 UTC — RED 8: thaw callback rolled back its owning transaction; expected `ReentrantOperationError` was not raised.
- 2026-10-11 14:32:27 UTC — GREEN 8: full suite 9 passed. Refactor: operation-owned callback capture wraps thaw/freeze, comparison including truth conversion, factories and original retained-scope callbacks. Nested providers share ownership; constructors' factory writes now reject as reentry.
- 2026-10-11 14:33:08 UTC — RED 9: synthetic cleanup/ownership tests raised raw backend failures and did not enter diagnosed faulted state. Validator story initially used an invalid Lifecycle marker spelling; after using its explicit key, initialization never invoked the declared validator (behavioral red).
- 2026-10-11 14:34:03 UTC — GREEN 9: full suite 12 passed. Refactor: frozen candidate read context validates every reachable node before replacement-epoch publication; preview shares the path without consuming frame IDs; backend completion evidence is checked for explicit and original scope callbacks. Faulted reads/snapshots require confirmed selection identity.
- 2026-10-11 14:34:27 UTC — RED 10: generation selection test found one facade class instead of three and no view/mutability/factory-specific contributions.
- 2026-10-11 14:36:42 UTC — GREEN 10: native full suite 13 passed. Refactor: typed view facts select generated current/working/thaw properties; lazy getter/setter and transient factory templates selected by matchers; inherited factory layer adds constructor matching. Used block return contribution to avoid native expression-hole relocation across multiple inserted statements.
- 2026-10-11 14:38:21 UTC — RED 11: new narrow definitions/type tests exposed accepted named local-store factory providers, accepted invalid binding values, and leaked constructor-only declaration markers.
- 2026-10-11 14:38:54 UTC — GREEN 11: full suite 28 passed. Refactor: Lifecycle BindingBase/BindingDict type parity with scalar/map matcher-selected setters, zero-argument scratch factories enforced, generated constructor-only properties explicitly reject facade access. Custom objects with a coincidental `_u_state` are rejected without probing attributes.
- 2026-10-11 14:39:27 UTC — RED 12: thawed children leaked working child facades through ordinary parent access.
- 2026-10-11 14:39:55 UTC — GREEN 12: full suite 29 passed. Refactor: pending container projection preserves the owned working list and propagates child view mode; generated thaw selection is now explicit; setter comparisons do not trigger thaw. Recursive transient providers reject before installing an overlay and permit a pure retry.
- 2026-10-11 14:40:20 UTC — RED 13: fault-injection replacing the publication reference with `None` was incorrectly treated as a confirmed selection because the prior installed identity was also `None`; configuration was mutable and setup diagnostics leaked AttributeError.
- 2026-10-11 14:40:38 UTC — GREEN 13: full suite 33 passed. Refactor: publication confirmation is bound to the completing token, configuration is read-only, all historical diagnostics require initialized/confirmed selection, and faulted live baseline reads/construction fail explicitly.
- 2026-10-11 14:41:23 UTC — RED 14: `PYTHONPATH=src ../.venv/bin/python -m pytest -q tests/test_canonical.py -k 11` failed intermediate-layer generation: the final decorator did not expose a selectable generation module for independently executable feature concepts.
- 2026-10-11 14:41:32 UTC — GREEN 14: the same focused command passed. Refactor: the composable builder accepts the selected generated module; the canonical layer story compiles and executes each feature concept rather than substituting runtime stubs.
- 2026-10-11 14:42:40 UTC — RED 15: `PYTHONPATH=src ../.venv/bin/python -m pytest -q tests/test_definitions.py` failed the direct invalid marker factory diagnostic: Lifecycle's immediate definition error did not match the public Undoable name.
- 2026-10-11 14:42:46 UTC — GREEN 15: definition diagnostics passed. Refactor: the public definition-error name aliases Lifecycle's error, preserving exact marker reuse and immediate validation semantics.
- 2026-10-11 14:43:05 UTC — RED 16: focused definition tests exposed a nonclass decorator input and AST assembly failure escaping without contextual definition diagnostics.
- 2026-10-11 14:43:15 UTC — GREEN 16: focused definitions passed after input recognition and contextual assembly error wrapping; no fallback handwritten class path was introduced.
- 2026-10-11 14:47:08 UTC — RED 17: `PYTHONPATH=src ../.venv/bin/python -m pytest -q tests/test_generation.py -k layout` failed: moving YIDL resources changed emitted source-origin IDs from the canonical logical names to their physical installation layout.
- 2026-10-11 14:48:58 UTC — GREEN 17 recorded: the same layout command passed (1 passed, 1 deselected). Refactor: compilation uses stable logical resource IDs while reading resources from their actual source or installed location.
- 2026-10-11 14:52:09 UTC — RED 18: `PYTHONPATH=src ../.venv/bin/python -m pytest -q tests/test_adversarial_diagnostics.py -k backing` failed: a MappingProxyType backed by an application Mapping ran iteration outside the callback fence during initial normalization. Its begin attempt raised a setup RuntimeError rather than ReentrantOperationError.
- 2026-10-11 14:52:24 UTC — second RED 18: focused `-k proxy` failed both initial normalization and pending proxy traversal. An iteration callback rolled back the owning edit during a managed read and a later iteration raised no-active-transaction RuntimeError.
- 2026-10-11 14:52:47 UTC — GREEN 18 recorded: focused proxy checks passed (2 passed, 3 deselected), followed by **43 passed in 6.80s** locally. Refactor: stable normalization, working graph traversal and pending child projection use the same operation-owned callback fence, because an immutable proxy may invoke code in its backing mapping.

## Final local gates

- A broad formatter invocation changed generated goldens; canonical comparison failed in all twelve stories while their behavioral assertions completed. This is tooling damage, not a behavioral TDD tranche. `tests/regenerate_golden.py --write` restored exact generator output. Generated files must be excluded from formatting.
- 2026-10-11 14:49:37 UTC — initial final `PYTHONPATH=src ../.venv/bin/python -m pytest -q`: 41 passed in 5.98s, using Python 3.12.12 and native Astichi 1.1.3. The additional red/green normalization tranche above raises the settled count to 43.
- `PYTHONPATH=src ../.venv/bin/python -m yidl_undoable.regenerate_undoable_base`: generated base matches. Golden regeneration/check and byte comparison are repeated at handoff.
- `../.venv/bin/python -m compileall -q src tests examples`: passed.
- `uv build`: wheel and sdist built successfully. Both contain all nine YIDL layers and `py.typed`.
- 2026-10-11 14:50:16 UTC — separate temporary Python 3.12.12 virtual environment installed Undoable plus the four pinned dependency wheels. From a different cwd, the installed package import, nine resources, installed base regeneration check, and both `examples/first_use.py` and `examples/nested.py` passed, without editable or sibling imports.
- Cold `uv sync --extra dev` with a separate temporary project environment passed, then that environment's base check passed. The ephemeral lockfile was removed. Top-level sources include the transitive `yidl-cache` sibling because dependency projects' source tables are not used by uv.
- 2026-10-11 14:53:30 UTC — settled handoff checks recorded: full suite repeated after targeted formatting (**43 passed in 6.52s**), compile checks passed, final wheel/sdist rebuilt and reinstalled into the separate wheel environment. Installed base check, both examples and nine-layer/typing contents passed again. Earlier two native base renders matched byte for byte and checked-in source; canonical generated-source check matched. Absolute machine-path scan across implementation, tests, docs, examples, packaging and drafter evidence returned no hits.

The wheel smoke establishes the pinned source tuple documented by the accepted design with Astichi 1.1.3. It does not establish compatibility with every earlier distribution using YIDL/Lifecycle's same 0.1.0 version, and it is not a Python-version matrix or runtime review acceptance.

## Python 3.14 recognition correction

The lane owner's independent initial matrix passed 43 tests on Python 3.12.12
and 3.13.12, but Python 3.14.3 failed collection at native scope materialization.
The following investigation used the lane owner's isolated pinned-wheel Python
3.14 interpreter, with no dependency source edits or engine fallback.
Commands below use `python3.14` as a portable name for that supplied interpreter.

- 2026-10-11 14:54:24 UTC — reproduced RED with `PYTHONPATH=src python3.14 -m pytest -q tests/test_generation.py`: collection failed with native materialization not producing a composable.
- Direct native assignment/function/class AST materialization and compilation succeeded independently of Undoable. Observing the native exception in the failing generated scope exposed `ValueError: native schema error: mandatory parameter holes remain unresolved: init_params`.
- A minimal declaration showed `Node.__dict__.get('__annotations__')` was None and harvested fields were empty on 3.14, while `inspect.get_annotations(Node, eval_str=False)` returned the declared field. Python 3.14's deferred annotation storage caused missing facts, rather than an unsupported native interpreter.
- 2026-10-11 14:55:33 UTC — narrow RED: `PYTHONPATH=src python3.14 -m pytest -q tests/test_annotation_recognition.py`: expected one local managed field, obtained no fields.
- 2026-10-11 14:55:53 UTC — GREEN recorded: the narrow test passed, then `PYTHONPATH=src python3.14 -m pytest -q` passed **44 tests in 5.92s**. Refactor: collect only local annotations through `inspect.get_annotations(..., eval_str=False)` and pass them to the unchanged Lifecycle normalization adapter. No bounds or semantics were substituted.
- 2026-10-11 14:56:24 UTC — compatibility gates recorded: Python 3.12.12 full suite **44 passed in 5.99s**; Python 3.13.12 pinned-wheel suite **44 passed in 6.61s**; Python 3.14.3 checked-in base regeneration matched. All use the same native generator architecture.

These are actual three-interpreter test results for the pinned dependency tuple.
Independent runtime review acceptance remains pending.

## Runtime remediation cycle 1

Both runtime reviews at `a97e43e5010fd22a9bcd008f27072ca656b73f5b`
were NO-GO. The merged plan accepts seven distinct bounded P2 roots. All
corrections below preserve the accepted native generator, API and backend
composition; originating reviewer closure is still required.

- 2026-10-11 15:07:33 UTC — RED: `PYTHONPATH=src ../.venv/bin/python -m pytest -q tests/test_canonical.py -k '13 or 14 or 15 or 16 or 17'`: five failed, twelve deselected. Actual failures were empty declaration materialization (Code P2-1), working child leaked through ordinary set access (Code P2-2), named lazy dependency supplied unset storage (Code P2-3), candidate transient reads returned baseline instead of active values (State P2-2), and snapshot frozenset hashing reached unhashable graph records (State P2-3).
- 2026-10-11 15:07:55 UTC — RED: `PYTHONPATH=src ../.venv/bin/python -m pytest -q tests/test_remediation_faults.py tests/test_remediation_diagnostics.py`: five failed, one passed. Apply failure after internal publication bookkeeping raised raw RuntimeError and left healthy state (State P2-1); failed enlist with abort failure before and after token closure raised raw cleanup error and/or retained overlay (State P2-4); unset and recursive named lazy dependencies did not reject construction (Code P2-3). The pre-bookkeeping corruption diagnostic already passed and is retained as a complementary check, not counted as red.
- 2026-10-11 15:08:54 UTC — narrow diagnostics/faults GREEN: six passed. Clean discard now requires unchanged pre-completion selection. Failed begin always detaches its overlay; unconfirmed abort evidence or abort exceptions fault with the original enlist and cleanup failures preserved. Named lazy providers enter the existing generated getter/fenced materialization path and reject unset dependencies contextually before node registration.
- Refactor: an explicit empty parameter supply contribution in `undoable_core.yidl` consumes the mandatory constructor hole while preserving the required keyword transaction_manager. Its phase uses the owning production's existing class input; a duplicate-input compiler diagnostic was corrected before normal base regeneration. No generated output was manually patched.
- Refactor: exact built-in sets recursively project child view modes; in-place working projection preserves the set object and replaces equal-valued facade objects by identity through clear/update. Ordinary projection creates its own set when view conversion is needed. Candidate pins retain active transient semantics while historical pins/current reads retain baseline semantics. Snapshot nodes hash by their snapshot-context identity and node ID, without traversing epoch records.
- The provisional lazy fixture initially tried reading the current committed facade after construction but before attachment/publication. That assertion was corrected to ordinary/working provisional reads, retaining the accepted current absence contract. It was a fixture error, not a runtime change.
- 2026-10-11 15:09:32 UTC — GREEN: native canonical behavior completed and source goldens were materialized; full `PYTHONPATH=src ../.venv/bin/python -m pytest -q` passed **55 tests in 6.34s**.

Canonical additions 13–17 cover the five successful combinations. Narrow
remediation diagnostics cover unset/recursive lazy dependencies with no partial
registration, incomplete installed publication with confirmed/unconfirmed reads,
and failed outer setup abort before/after closure with detached overlays and
preserved causal errors. Existing successful-abort setup coverage now also
asserts a later begin can commit normally.
- 2026-10-11 15:11:05 UTC — final local gates recorded: after targeted formatting,
  full suite **55 passed in 6.53s**. Two native generated-base renders matched
  byte for byte and the checked-in base; all 17 generated-source goldens matched.
  Compile checks passed and wheel/sdist rebuilt successfully. The lane owner
  repeats independent interpreter and installed-wheel gates for this revision.

# YIDL Undoable implementation — CODE + SURFACE-AXIS REVIEW

**Review object:** Complete `yidl_undoable` runtime package, tests, examples, generation resources, documentation and configuration at `a97e43e5010fd22a9bcd008f27072ca656b73f5b`; local implementation draft, runtime acceptance pending. Controlling design: `dev-docs/UndoableDesign.md`, accepted at `616f2f65473b1240535a6317d8cc79d5cec18414`.

**Baseline:**

| Repository | Pinned revision |
| --- | --- |
| `yidl_undoable` | `a97e43e5010fd22a9bcd008f27072ca656b73f5b` |
| `yidl-lifecycle` | `230362f642d6e9205897698670fe5f87d2c905ce` |
| `yidl` | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| `astichi` | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| `yidl-cache` | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Implementation comparison baseline: `3440ec2fcee3a8d61c1f88cdfbafafc0683edabf`. Sources were read from the working tree; read-only Git comparisons confirmed the reviewed implementation, tests and controlling documents match `HEAD`. The design matches its accepted revision, and the implementation plan matches its baseline revision. The complete tuple was verified at review start and again at review end; it did not move.

**Date:** 2026-10-12

**Axis:** Code architecture, interfaces, composition and compatibility, plus the cold Python API surface. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: NO-GO** — three P2 findings block acceptance. No P0, P1 or P3 findings. I pre-commit to GO on a revision that resolves P2-1, P2-2 and P2-3 as specified.

---

## 0. Evidence base

The cold reading order was `README.md`, `docs/API.md`, and both executable examples, before design or implementation source. The subsequent review covered:

- `README.md:1–73`, `docs/API.md:1–99`, `examples/first_use.py`, `examples/nested.py`, and `docs/Architecture.md`.
- `dev-docs/CurrentProgramCheckpoint.md`, `dev-docs/UndoableDesign.md`, and `dev-docs/UndoableImplementationPlan.md`.
- Implementation, TDD and verification claims in `dev-docs/ImplementationDraft.md`, `dev-docs/TddEvidence.md`, and `dev-docs/VerificationEvidence.md`. Those records were treated as claims to inspect, not as runtime acceptance.
- `src/yidl_undoable/undoable.py:1–76`, `undoable_harvester.py:1–132`, `facades.py:1–306`, `transaction_yidl.py:1–596`, and the supporting history, values, graph, callbacks, bindings, policies, snapshots, candidates, states and error modules.
- All nine `src/yidl_undoable/yidl/*.yidl` resources, the generation/check interface, public exports, marker re-exports and `pyproject.toml`.
- All twelve canonical scenario sources; the definition, recognition, generation, history, state, fault and adversarial diagnostic tests.
- Pinned Lifecycle harvesting and factory-dependency resources, particularly factory parameter recognition and provider metadata.

Commands and results:

1. From the canonical workspace root, `git -C <member> rev-parse HEAD` for each of the five pinned members, at both ends of the review: all matched.
2. Read-only `git diff --stat 3440ec2fcee3a8d61c1f88cdfbafafc0683edabf..HEAD`: implementation spans 78 changed files.
3. `git diff --exit-code HEAD --` over the reviewed implementation, documentation, examples, configuration, tests and evidence files: exit 0.
4. Corresponding read-only comparisons for the accepted design and baseline implementation plan: exit 0.
5. From `yidl_undoable`:

   ```sh
   PYTHONDONTWRITEBYTECODE=1 ../.venv/bin/python -m pytest -q -p no:cacheprovider \
     tests/test_canonical.py \
     tests/test_definitions.py \
     tests/test_annotation_recognition.py \
     tests/test_history.py \
     tests/test_faults.py \
     tests/test_state_diagnostics.py \
     tests/test_adversarial_diagnostics.py \
     tests/test_generation.py::test_matcher_selected_executable_surface
   ```

   Result: **43 passed in 5.57s**, Python **3.12.12**. The resource-layout test was deliberately excluded because it copies files through `tmp_path`; this review performed no file writes.

6. No-bytecode, in-memory Python probes using `PYTHONPATH=src` reproduced each finding below. They also executed both examples successfully, confirmed all five keyed manager operations default to `DEFAULT_TRANSACTION`, and counted nine package YIDL resources.
7. Regenerator `--help`: exposes checking as the ordinary operation and `--write` as the explicit mutation option. The permitted generation test independently checked that regenerated base source matches the checked-in base.

No installation, build, regeneration with writes, Git mutation, adjacent edit or additional agent was performed. The documented isolated-wheel and Python 3.13/3.14 evidence was inspected but not repeated.

## 1. Findings

### [P2-1] The mandatory constructor parameter hole prevents valid declarations with no constructor fields

**Location:** `src/yidl_undoable/yidl/undoable_core.yidl:44–54`, particularly the mandatory `init_params` parameter hole at line 50; constructor contributions are selected only for fields with `Init == True`.

**Violated invariant:** Supported field policies must compose into executable generated classes. `local_store` and `classvar` explicitly have no constructor parameter; supported `init=False` declarations must not require an unrelated constructor field to make the generator work.

**Reproduction:**

```python
from yidl_undoable import UndoRedoManager, local_store, undoable

@undoable
class ScratchOnly:
    cache: dict = local_store(default_factory=dict)
```

Decoration raises the public definition-error alias:

```text
LifecycleDefinitionError:
ScratchOnly: Undoable AST generation/execution failed:
scope.build requires native materialization but the native materializer
did not produce a composable
```

Independent probes produced the same failure for:

- An empty declaration.
- A class containing only `classvar(default="node")`.
- A class containing only `managed(default=0, init=False)`.

These schemas provide no contribution to `init_params`, leaving the mandatory parameter hole unresolved. The existing intermediate-layer fixture always retains a constructor-enabled plain field, so it misses this composition boundary.

**Impact:** Documented marker combinations cannot be decorated. An application must introduce a dummy constructor field merely to obtain executable AST, and the error misleadingly presents the failure as native materialization.

**Required correction:** Make zero generated constructor-field parameters a valid composition in the owning YIDL resource. Preserve the required keyword-only `transaction_manager` parameter. Regenerate the generated base rather than patching it by hand.

**Closure/regression test:** Add canonical generated-source coverage for local-store-only, classvar-only and all-`init=False` declarations. Each must decorate, construct with only `transaction_manager`, initialize, and execute its applicable field behavior. Include a zero-field declaration boundary and verify generated constructor parameters contain no dummy field.

### [P2-2] Working sets bypass child-view projection and leak working handles through ordinary reads

**Location:** `src/yidl_undoable/values.py:82–125`, particularly the container admission check at lines 92–93. `set` is supported by working graph traversal but omitted from `project_working`.

**Violated invariant:** Managed child references propagate their parent’s view. Ordinary parent access must return ordinary children; working parent access must return working children. An ordinary read must not unexpectedly initiate a child’s thaw.

**Reproduction:**

```python
from yidl_undoable import UndoRedoManager, managed, undoable

@undoable
class Node:
    value: tuple = managed(default=(), thaw=list, freeze=tuple)
    children: frozenset = managed(
        default=frozenset(), thaw=set, freeze=frozenset
    )

history = UndoRedoManager()
child = Node(transaction_manager=history)
parent = Node(
    children=frozenset((child,)), transaction_manager=history
)
history.initialize(parent)

history.begin()
working_set = parent.working.children
ordinary_child = next(iter(parent.children))
```

Observed:

```text
ordinary_child._u_view == "working"
type(ordinary_child.value).__name__ == "list"
```

The ordinary child read also added `(child.node_id, "value")` to the transaction’s touched fields. This happens because thawing the parent produces working child handles, and ordinary projection returns the set unchanged. The reverse direction is affected when a pending set contains ordinary/current handles.

**Impact:** A routine `frozenset`/`set` converter pair violates the advertised view semantics. Ordinary nested reads can call converters and record child versions unexpectedly. Working nested reads can receive a child view that does not supply the expected thaw behavior.

**Required correction:** Project exact built-in working sets recursively. Preserve set semantics, node identity and the owned working-set object where in-place projection is requested; ordinary projection must not rewrite the owned set’s child views.

**Closure/regression test:** Add a canonical scenario using `thaw=set` and `freeze=frozenset`. Check both directions: an ordinary read after thaw returns ordinary children without touching their fields, and a working read of a pending set containing ordinary/current handles returns working children. Check nested sets and committed/current reads, then retain and mutate the escaped set after completion to confirm committed data remains detached.

### [P2-3] Named constructor providers receive the lazy-storage sentinel instead of the provider value

**Location:** `src/yidl_undoable/facades.py:48–85` and `93–108`. A static field is resolved to `MISSING` at lines 62–63; named construction providers use `_u_resolve_constructor` directly at lines 102–103 and receive that sentinel.

**Violated invariant:** Named factory parameters resolve declared field providers in dependency order. Lazy fields expose their first-read value, and internal unset sentinels must not become application factory arguments or stored application values. The documented provider surface does not exclude lazy fields.

**Reproduction:**

```python
from yidl_undoable import UndoRedoManager, const, lazy, undoable

@undoable
class WithNamed:
    source: int = lazy(default_factory=lambda: 7)
    target: object = const(default_factory=lambda source: source)

@undoable
class WithSelf:
    source: int = lazy(default_factory=lambda: 7)
    target: object = const(
        default_factory=lambda self: self.source,
        allow_self_factory=True,
    )

history = UndoRedoManager()
named = WithNamed(transaction_manager=history)
own = WithSelf(transaction_manager=history)
history.initialize(named, own)
```

Observed:

```text
named.target == MISSING
own.target == 7
named.source == 7
```

`named.target` remains the internal sentinel after successful initialization. The equivalent named dependency feeding a managed field instead causes initialization to fail with:

```text
FrozenValueError:
LazyDependency.target: unsupported stable value _FallbackSentinel;
declare freeze
```

That diagnostic incorrectly directs the user toward freezing a value the framework itself supplied.

**Impact:** A documented provider combination silently initializes nonversioned application data with an internal sentinel, or fails later with an unrelated frozen-value error. Named and opt-in self provider forms disagree.

**Required correction:** Resolve a named lazy provider through its appropriate materialization path during construction, retaining callback fencing, single evaluation and recursive-provider diagnostics. An unset lazy field with no usable value must fail contextually at the dependency rather than passing `MISSING` to application code.

**Closure/regression test:** Add canonical coverage for a named lazy dependency feeding both a const and a managed field, with declaration-order variations and setup/provisional construction. Assert the real provider value and one factory evaluation shared across all views. Add narrow diagnostics for unset and recursive lazy dependencies, including no partial node registration.

## 2. Invariant analysis

The existing implementation held against the following attacks:

- **Transaction-only managed writes:** Idle and construction writes reject; current managed writes remain read-only.
- **Joined scopes and stale tokens:** Nested begins join one token, inner commit publishes nothing, rollback closes the joined edit, and stale exceptional scopes preserve the body exception without aborting a replacement transaction.
- **Root graph integrity:** Shared children preserve identity; managed cycles and foreign-manager edges reject; final empty root sets are supported. Omitted setup nodes, aborted creations and abandoned future-only nodes cannot regain a baseline.
- **Sparse history and branch trimming:** Negative predecessor positions reject. Branch commits trim untouched future field histories as well as presence histories. Rollback and failed final preparation preserve redo.
- **Absence and snapshots:** Last-visible descendants remain pinned to the parent’s fallback frame. Snapshots preserve nested aliases and abandoned-branch values while excluding nonmanaged fields and application methods.
- **Stable storage and publication:** Application-backed mapping proxies are copied into private immutable storage. Later-node freeze/validation failures publish no earlier prepared value. Successful publication replaces one selection reference.
- **Original callback counterexamples:** Equality/truth callbacks attempting rollback or replacement, transient factories attempting retained scope completion, and idle lazy factories attempting begin/navigation are fenced. Failed materialization leaves the target unset and permits a pure retry.
- **Fault evidence:** Synthetic cleanup and ownership failures enter faulted state. Confirmed publication remains readable; unconfirmed publication blocks managed reads and snapshots.
- **Field policies:** Covered const, plain, binding, local-store, lazy and transient behavior follows the nonversioned/transient distinction. Removed nodes’ transient overlays are cleared.
- **Actual generation:** The nine-layer chain compiles executable AST. Matchers select constructor, kind, binding shape, lazy mutability/factory, transient factory and managed-view behavior. Canonical goldens compare actual generated source after executing behavior.

These successful attacks support the architecture, but they do not close the uncovered combinations in the findings. The intermediate layers’ persistent constructor field, list-focused working projection, and provider fixtures without constructor-time lazy dependencies explain how the suite remains green.

## 3. Risks and next action

The findings have bounded generator/runtime corrections; they do not establish an architectural failure or require redesign.

The next action is one test-led remediation revision covering P2-1 through P2-3, followed by originating counterexample closure and the existing acceptance gates. Keep successful coverage in the canonical harness; reserve narrow tests for unresolved/recursive provider diagnostics.

Residual verification limits: this review independently executed Python 3.12.12 source behavior and deterministic generation checks. It inspected, but did not independently repeat, the isolated-wheel and Python 3.13/3.14 records. Public registry release and arbitrary older same-version dependency compatibility remain outside the accepted scope.

## 4. Surface

The cold Python walkthrough was understandable:

- The package-root imports, decorator and required `transaction_manager=` keyword are visible immediately.
- Construction followed by explicit initialization separates setup from history.
- Manager-owned begin/commit/rollback/validate operations form a discoverable lifecycle.
- Exceptional scope exit explains rollback; undo/redo boundaries and branch behavior are documented.
- Default/current/working handles and snapshots have distinct names and stated purposes.
- Strict absence is the stated default; last-visible fallback and pinned descendants are explained.
- Custom transaction keys, lazy write-once behavior, transient cleanup, shared nonversioned data and fault recovery limits are described.

Both executable examples passed. Signature introspection confirmed the keyed operations default to `DEFAULT_TRANSACTION`. The regeneration CLI clearly distinguishes checking from writing.

The installation walkthrough requires assuming the stated relative sibling-source development layout; the README does not provide a standalone dependency-cloning recipe. This is a documentation limitation of the local draft, not evidence of a broken advertised registry installation.

The runtime surface failures are P2-1 through P2-3: supported declaration combinations fail, ordinary nested set reads behave as working reads, and a documented named provider delivers an internal sentinel. Each contradicts what a user can reasonably infer from the field and view guide.
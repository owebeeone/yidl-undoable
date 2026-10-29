# Specialized accessor experiment

Status: implemented and benchmarked. User-authorized experiment, 29 October 2026.

## Result

**Field-specific bodies materially improve simple access, but this experiment
does not show a substantial improvement to Undoable's transaction workloads.**
Plain/constant/local/binding reads improved about 1.9x; a materialized lazy read
improved 2.25x. Managed reads improved only about 1–2%, and complete commits were
effectively unchanged. The specialized bodies are significantly larger and take
longer to generate. Keep the variant opt-in; there is no evidence here for a
blanket replacement of the baseline implementation.

## Scope

Create an opt-in Undoable variant that generates field-specific accessor bodies,
and compare it against the existing decorator under identical behavior. Changes
are limited to this repository: experimental YIDL resources, generation/adapter
code, validation, benchmarks and this report. The existing `undoable` decorator
remains the baseline. No release, publication or workspace membership change.
YIDL, Astichi, Lifecycle and Dataclass are reference-only dependencies.

Preserve three facade classes, node state, transaction overlays, sparse history,
callback fencing, snapshots, comparisons and public field semantics. Specialize
facade access bodies; keep the shared history engine and constructor/provider
machinery. This measures accessor indirection, not an alternative storage engine.
No claim of eliminating all runtime policy/field lookups is made: shared history
operations retain their existing contracts.

## Delivery and verification

- Experimental decorator available separately from the baseline import.
- Authored YIDL extension with distinct resources and weighted matcher rules;
  no edits to SDKs, generated-method string interpolation or AST surgery.
- Existing canonical behavior stories executed with both decorators; baseline
  generated-source goldens remain unchanged.
- Focused source checks establish specialized bodies rather than renamed
  calls to generic facade accessor helpers.
- Paired multi-process timings for reads, writes and complete transactions,
  with the same classes, field policies, history depth and workload.
- Report generation cost separately, and record interpreter/dependency tuple,
  repetitions and variability. Performance is measured, not assumed.

## Initial feasibility observations

The shared workspace environment ran 250 tests before stopping at three failures:
its installed Dataclass metadata is `0.1.0.dev0`, whereas regeneration requires
the pinned `0.1.1` comparison authority. These were pre-change baseline failures.
An isolated published-dependency attempt with Lifecycle `0.1.0` and YIDL `0.1.2`
failed dependency resolution because that Lifecycle wheel pins YIDL `0.1.0`.
Neither observation authorizes dependency source edits. Use a compatible isolated
test environment or the supported local Lifecycle package route first.

The local Lifecycle package route succeeded. Final validation and timings used
CPython 3.12.12 on Darwin arm64, Astichi 1.1.3, YIDL 0.1.2, Lifecycle 0.1.1 and
the installed Dataclass 0.1.1 comparison authority. The isolation tool built the
local Lifecycle/YIDL package route; this is not described as an entirely
published-wheel qualification. No dependency source was edited.

## Implementation

The opt-in decorator is:

```python
from yidl_undoable.specialized import undoable
```

It accepts the same `eq` and `order` options as the existing decorator and uses
the same marker declarations. The default `from yidl_undoable import undoable`
continues to select the baseline.

`src/yidl_undoable/yidl/experimental/specialized.yidl` extends `UndoableBase`
using distinct authored resources and higher-weight matcher rules. It reuses
the class, constructor and comparison productions. The specialized assembly
gets its own module root. Error types, sentinels and fence/binding helpers are
held in an immutable capture carrier under the existing collision-free private
class aliases. Generated references select fixed attributes on that carrier;
there is no field-name dispatch in it.
Its generated runtime is compiled once per process on first use, then cached.
This experimental path consequently needs the existing `regenerate` extra's
pinned Dataclass authority. The ordinary decorator has no added Dataclass
runtime dependency.

The private `_decorate` adapter accepts a generation module and capture-carrier
type, passing the module to `build_composable` and instantiating the carrier
under the existing private aliases. Its defaults remain the existing checked-in
generated base and comparison-only carrier. Existing authored baseline
resources, generated base, runtime facade helpers and history manager remain
unchanged.

Generated getter/setter bodies now contain direct node-value access, managed
view selection and transaction checks, lazy initialization/write policy,
transient selection and binding validation. The following remain shared:

- Constructor resolution and provider invocation through `_u_factory`.
- Transaction manager, callback ownership fences and stable-value projection.
- Historical lookup, working overlays, commit, rollback and navigation.
- Field-policy facts still consumed by shared history operations.

The change removes the generic **facade accessor layer**, not every generic
operation below it. Some helper imports move from each setter invocation to
the experimental adapter's initialization and capture carrier. That is part of
the measured variant; the timings do not isolate Python call overhead from
helper-reference binding.

During validation, running baseline and specialized canonical stories together
exposed a temporary-variable scope mismatch in an inserted transient fragment.
The initially passing isolated checks were insufficient. Explicit outer bindings,
owned local names and initialized fragment result carriers fixed the generated
body. The final mixed suite exercises the original callback-fencing story, and a
bytecode check rejects accidentally global temporary-variable loads. An
additional probe found that a public class named `require_mutation` could shadow
an imported helper. The capture carrier fixes this; eight class-name regression
cases check the new helpers, sentinel and private-alias collision. No compiler
or dependency edit was implemented outside the consumer.

## Validation evidence

The final CPython 3.12 checks pass with both explicit lowering selections:

| Check | Python lowering | Native Rust lowering |
| --- | ---: | ---: |
| Full suite: baseline goldens plus specialized canonical behavior/source checks | 412 passed | 412 passed |
| Existing semantic suite redirected to the specialized decorator | 382 passed | 382 passed |

These counts overlap; they are not 794 independent scenarios per backend.
The redirected runner excludes baseline source-byte golden comparisons and the
baseline builder regeneration module. The new canonical test executes all 24
applicable existing behavior stories against the specialized decorator. The
`11_layers` story intentionally compiles individual baseline concepts and stays
in the ordinary canonical suite. No baseline golden was rewritten.

Source checks cover field kinds and managed views, reject calls from properties
to the old generic facade accessor helpers, and check temporary-variable binding.
Existing transaction, candidate, thaw, callback, comparison, inheritance and
snapshot behavior tests are reused rather than reimplemented as a second suite.
Focused name-collision tests also verify capture identity and exercise the
mutation fence, lazy sentinel, binding validation and error paths.

This is source/runtime validation on Python 3.12, not release qualification for
every supported interpreter, operating system or installed distribution.

## Benchmark method

Runner: `scripts/benchmark_specialized.py`.
Raw results: [Python 3.12 measurements](experiment/specialized-accessors-python312.json).
Source identity: [SHA256 manifest](experiment/specialized-accessors-source-sha256.json),
against baseline commit `307c0ff6924b5c405f2d287b14448d0006cfe35a` plus this
experiment's uncommitted source changes.

- Five fresh worker processes; five samples per implementation and case in each.
- Both implementations run in each worker; a seeded shuffle alternates their
  sample order. Both use the same seven-field declaration and history engine.
- Hot accessor cases use 40,000 iterations per sample. Generation, initialization,
  lazy materialization and history preparation are outside those timings.
- Each sample starts from fresh equivalent state; a separate instance is warmed.
- History-dependent cases start with one or 128 committed frames as named.
- Complete-commit samples perform 64 commits, growing history identically from
  the named starting depth. Rollback samples also perform 64 transactions.
- Changed managed writes alternate two values; their denominator counts both
  assignments. Undo/redo control timings report one **pair** per operation.
- GC is disabled during measurements for both implementations. These are
  controlled microbenchmarks, not application latency or memory-pressure tests.
- Each reported speedup is the median of the five paired process-median ratios
  `baseline / specialized`. The range is the minimum/maximum of those ratios,
  not a confidence interval. Independently aggregated latency columns need not
  divide to exactly the paired speedup.

### Steady-state observations

Times below are nanoseconds per operation except where marked microseconds.

| Operation | Baseline | Specialized | Paired speedup | Process-ratio range |
| --- | ---: | ---: | ---: | ---: |
| Plain read | 62.9 ns | 32.1 ns | 1.946x | 1.821–1.985x |
| Const read | 61.7 ns | 33.0 ns | 1.921x | 1.818–1.963x |
| Materialized lazy read | 103.3 ns | 45.5 ns | 2.251x | 2.211–2.327x |
| Local-store read | 64.2 ns | 33.4 ns | 1.870x | 1.862–1.975x |
| Binding read | 61.6 ns | 32.4 ns | 1.885x | 1.792–1.935x |
| Transient baseline read | 115.9 ns | 57.0 ns | 2.048x | 1.968–2.057x |
| Transient read in edit | 133.0 ns | 98.0 ns | 1.357x | 1.325–1.384x |
| Plain write | 59.2 ns | 41.1 ns | 1.474x | 1.431–1.499x |
| Mutable lazy write | 58.5 ns | 40.4 ns | 1.470x | 1.448–1.493x |
| Managed read, one frame | 784.4 ns | 774.9 ns | 1.009x | 1.005–1.018x |
| Managed read, 128 frames | 799.6 ns | 789.5 ns | 1.013x | 1.010–1.015x |
| Current read, 128 frames | 594.6 ns | 586.6 ns | 1.017x | 1.006–1.021x |
| Clean working read, 128 frames | 6.819 µs | 6.746 µs | 1.006x | 1.004–1.012x |
| Dirty working read, 128 frames | 4.377 µs | 4.335 µs | 1.009x | 1.005–1.015x |
| Unchanged managed write | 11.546 µs | 11.250 µs | 1.025x | 1.020–1.030x |
| Changed managed write | 9.031 µs | 8.756 µs | 1.029x | 1.024–1.034x |
| Complete commit, initially one frame | 41.264 µs | 40.863 µs | 1.007x | 1.006–1.021x |
| Complete commit, initially 128 frames | 45.290 µs | 44.976 µs | 1.006x | 1.002–1.009x |
| Complete rollback, 128 frames | 24.458 µs | 24.102 µs | 1.013x | 1.006–1.019x |
| Undo/redo pair control, 128 frames | 818.2 ns | 816.4 ns | 0.999x | 0.985–1.012x |

Small changes should not be presented as statistically established application
improvements. The unchanged shared-engine control gives useful context for the
scale of noise; the large simple-accessor gains are much clearer than the
transaction differences. The benchmark does not cover large object graphs,
expensive converters, deep histories beyond these cases, or a representative UI.

### Generation and generated-code tradeoff

For the same seven-field model:

| Observation | Baseline | Specialized |
| --- | ---: | ---: |
| Generated model source | 3,349 bytes | 8,621 bytes |
| Sum of locally defined accessor `co_code` lengths across views | 684 bytes | 4,970 bytes |
| Median warm class decoration | 24.18 ms | 217.13 ms |

The source is about 2.57x larger; accessor bytecode length about 7.27x larger.
Warm class decoration is about 8.98x slower in this implementation.
These timings include YIDL assembly and capture binding, not just Python class
creation; they do not establish an unavoidable cost for every specialization
strategy.
Bytecode length is **not total heap usage**: it excludes constants, code-object
overhead, shared helpers and inherited definitions. Warm class-generation times
exclude the declaration construction, and follow one cache-warming model per
implementation.

The experimental extension builder compilation took a median **757 ms once per
worker process**, before warm class timings. The baseline ships its builder
already generated. This first-use difference partly reflects the experimental
packaging route, not an unavoidable cost of specialized accessor code. It must
not be hidden, but it also must not be attributed entirely to specialization.
No ahead-of-time experimental builder or startup cache was added in this scope.

## Interpretation and follow-up findings

**Worth keeping as an experiment:** the user hypothesis is confirmed for simple
accessor overhead. Removing two or more helper calls can save a substantial
fraction of a tens-of-nanoseconds operation.

**Not a demonstrated general Undoable optimization:** managed history accesses,
transaction ownership checks and complete commits do much more work than that
facade forwarding. Their measured gains here are small. The larger source and
roughly ninefold warm generation cost mean adopting this everywhere needs a
workload-specific reason. This experiment has not optimized the assembly cost.

A separate diagnostic profile of 20,000 specialized clean-working reads found
40,000 `_present` calls and 40,000 graph `visit` calls, alongside callback fencing,
decoding and historical reads. Profiling overhead makes those elapsed times
unsuitable as benchmark latencies. The counts and call paths point toward the
shared engine as the next place to investigate **if** managed access is the
application bottleneck. This is an optimization opportunity, not a confirmed
defect or a blocker for this experiment. Working membership is intentionally
recomputed because mutable working containers can escape; changing that requires
a separate semantic/invalidation design and user authorization. No history-engine
optimization was implemented here.

A native-lowering feasibility check rejected `astichi_ref` markers inside the
initial lazy-setter fallback and binding-validation lambda, reporting a missing
native package marker row. The final authored resources use explicit setter and
validation contributions, with the validator reference selected before its
lambda. Both lowering routes now pass without dependency edits. This is a
recorded template-placement limitation, not evidence that native lowering cannot
support the requirement. A separately authorized SDK investigation could reduce
that authoring constraint; it does not block this experiment.

## Reproduction

From this repository root, the isolated environment used here can be selected
without changing the shared workspace environment:

```sh
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
export ASTICHI_LOWER_ENGINE=python

uv run --no-project --python ../.venv/bin/python \
  --with ../yidl-lifecycle --with yidl-dataclass==0.1.1 --with pytest \
  python -m pytest -q -p no:cacheprovider

uv run --no-project --python ../.venv/bin/python \
  --with ../yidl-lifecycle --with yidl-dataclass==0.1.1 --with pytest \
  python scripts/check_specialized.py

uv run --no-project --python ../.venv/bin/python \
  --with ../yidl-lifecycle --with yidl-dataclass==0.1.1 --with pytest \
  python scripts/benchmark_specialized.py \
  --processes 5 --samples 5 --loops 40000 \
  --output dev-docs/experiment/specialized-accessors-python312.json
```

Use `ASTICHI_LOWER_ENGINE=native-rust` to repeat validation on that lowering route.
The recorded benchmark used Python lowering; no cross-backend timing claim is made.
Interpreter/package versions should be checked against the raw result before
comparing runs. Neither this report nor its commands authorize a release or
changes to the referenced dependency sources.

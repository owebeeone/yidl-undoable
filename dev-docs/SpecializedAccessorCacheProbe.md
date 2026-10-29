# Compiled-builder cache probe

Date: 29 October 2026. Status: bounded mechanism probe completed, not a production
cache integration or release. The user requested this after reviewing the
specialized accessor experiment's class-generation cost.

## Scope

Use the existing published `yidl-cache` API around compilation of a model-specific
builder, then execute its code in a fresh namespace and bind the current schema,
declaration and capture carrier. New probe script, measurements and this report
are the only authored files. The existing uncommitted specialization and its
benchmarks are preserved. No SDK, cache package, shipped decorator, history
engine, dependency declaration or publishing workflow was changed by this probe.

## Result

Persistent compiled-builder reuse removes the measured warm generation penalty
for this model. It does not eliminate empty-cache generation or improve managed
history access by itself. Both baseline and specialized builders benefit.

Median times from five process sets, CPython 3.12.12 on macOS arm64, Python
lowering:

| Path | Baseline | Specialized |
| --- | ---: | ---: |
| Cache disabled, warmed model generation | 24.059 ms | 218.179 ms |
| First lookup into an empty cache | 48.786 ms | 953.972 ms |
| In-process hits after that population | 0.263 ms | 0.256 ms |
| First persisted hit in a fresh process | 1.878 ms | 1.085 ms |
| Subsequent hits in that fresh process | 0.250 ms | 0.249 ms |

The small baseline/specialized differences on hits are not evidence that one
cache path is faster. First-hit timing can include lazy import/initialization
effects. The useful observation is that both reuse paths avoid generation and
are far below their uncached generation costs.

The first-hit timers start after dependency inventory capture and consumer
imports. They are **not entire interpreter/application startup times**. The
cached process also executes six generated models per implementation and their
correctness checks; its process wall time must not be described as one class's
startup latency. Raw process and inventory timings are retained in the data.

## Method and correctness evidence

The probe uses the same seven field families as the accessor benchmark: ordinary,
constant, managed, lazy, transient, binding and local storage. Each process set
runs a disabled-cache worker, an empty-cache population worker, and a fresh worker
reusing the latter's persistent artifacts. Five fresh class builds follow the
first build for each variant. Variant order is seeded/shuffled.

The same standalone binding adapter is timed with caching disabled and enabled.
The timer includes declaration creation, harvesting, shape fingerprinting, lookup,
generation on a miss, code execution and fresh class binding. Instance creation
and transaction/undo checks occur outside the generation timer.

Every generated class is new. Defaults and closure-based lazy factories change
between builds, including between population and fresh-process reuse. Assertions
check their new values, distinct local dictionaries, committed versus pending
values, transient cleanup, commit, undo, redo and rollback. A changed field layout
requires a new cache miss. Fresh-process producer callbacks explicitly raise if
called: all ten implementation/process combinations reused code with zero
producer calls and `generated=False` diagnostics.

Only compiled code objects are cached. Class objects, namespaces, schemas,
callbacks and live defaults are not persisted. The request fingerprints audited
structural facts and a variant identity, excluding runtime values. Dependencies
capture source timestamps/sizes before generator use; every worker must report
the same dependency digest. Canonical private temporary cache locations are used.
The first smoke attempt used a noncanonical temporary path and could not prove
warm reuse; resolving that path allowed the existing trust policy to work without
changing cache security or implementation.

## Limits and next qualification

The probe intentionally supports a bounded builtin-annotation model without
validators, inheritance or enabled logical comparisons. It is not a general
fingerprint adapter for arbitrary user declarations. It does not reconstruct the
diagnostic `__undoable_source__` string on hits; that work is also excluded from
the disabled-cache adapter. These timings therefore compare like binding paths,
not every diagnostic behavior of the existing decorators.

This does **not** replace the full Undoable regression suite. The specialized
decorator's separate 412/382-test results remain scoped to that earlier
implementation. The cache route has the assertions above, not those full-suite
results. Before adopting it, qualify all supported field/provider/inheritance/
comparison shapes, diagnostics and invalidation, and rerun existing semantic and
canonical stories through cold and populated adapters. Preserve fresh bindings
and cache trust/bypass behavior. No cache implementation needs to be redesigned
to establish this mechanism.

Only Python lowering on this interpreter/platform was timed. Existing CPU load,
OS file caches, GC behavior and microbenchmark conditions limit extrapolation to
application startup. No new steady-state accessor measurements were made: the
earlier runtime gains and their limitations remain separate.

## Reproduce and evidence

Run from this repository root with the local opt-in specialization present and
an isolated CPython 3.12 environment containing Astichi 1.1.3, YIDL 0.1.2,
yidl-cache 0.1.0, Lifecycle 0.1.1 and Dataclass 0.1.1:

```sh
ASTICHI_LOWER_ENGINE=python YIDL_LIFECYCLE_CACHE=off \
  python scripts/probe_specialized_cache.py --processes 5 \
  --output dev-docs/experiment/specialized-cache-python312.json
```

[Raw measurements](experiment/specialized-cache-python312.json) record every
sample, outcome, producer count, dependency digest, interpreter/package versions,
process timing and the script's SHA-256. The script loads local Undoable source
but this run used published dependency packages, not sibling SDK source edits.
The original [specialization report](SpecializedAccessorExperiment.md) retains
its own scope and source-identity evidence. No commit or publication is implied
by these local probe files.

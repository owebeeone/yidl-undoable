# Undoable comparison integration E/F evidence

Status: combined E/F consumer checkpoint, awaiting owner installed verification.
Only Undoable comparison integration and Dataclass affected-test evidence changed.
Original Astichi 1.1.3, YIDL 0.1.0 and Lifecycle 0.1.0 remain reference-only wheels.
No SDK/Lifecycle changes or rebuilds occurred. The pre-integration owner baseline
was 215 passing tests on each of the six minor/backend combinations; it was not
unnecessarily repeated here.

## Behavior and generation boundary

Strict decorator flags default to disabled equality/ordering. Boolean logical
comparison is field-local; managed write comparison has separate value/identity
policy, with legacy string compatibility and explicit-conflict diagnostics.
Default/current/working classes consume the pinned Dataclass ComparisonCore's
actual equality/ordering productions. Adapter matching indexes shared resources
per view. Operand bindings remain ordered and field-specific. Undoable's explicit
unhashability adapter preserves the public hash slot. SnapshotNode is unchanged.

The authored historical-write prelude precedes self/class/operand reads. Its
constant-True statement carrier is eliminated by compilation; source and bytecode
checks retain calls, constants and jumps, normalizing only CPython fused local
opcodes. Existing SDK outer-binding markers link generated class registry/result
references. These are consumer source-pattern choices, not SDK capability claims.
There is no shared-resource copy, generic runtime comparison dispatch, method
source emitter, AST repair or recursive payload projection.

The managed value-write branch still performs native `bool(old == value)` on the
original operands within its existing ownership fence. A fresh private ContextVar
marker contains only its active boolean. Every exit closes it before reset;
closed copied contexts cannot reactivate it. Identity writes create no scope.
Enabled facade equality delegates to the captured historical RuntimeFacade method
only during that active scope; normal logical equality resumes afterward.

Regeneration consumes installed Dataclass 0.1.0.dev0 D wheel SHA256
`845b55e814a7b56be4cda0964393962fbcf977898eae068bb1c489ebd1ff0942`,
and authoritative shared resource SHA256
`2f7e6df989b0714d8764de84d8a6f6b03f39c3ad7f57dba5e55f5131b8354eef`.
Generated provenance embeds logical names/digests. Regeneration rejects changed
version/bytes. Normal decoration is tested in a fresh process blocking all
Dataclass imports. Environment records preserve selected backend, actual installed
origins, exact dependency versions and original wheel hashes.

## Actual TDD and verification

`increments.jsonl` is append-only: exact commands, elapsed times, recorder runtime,
backend, return codes, sanitized log/JUnit hashes and original raw hashes.
Earlier rows whose recorder and child used different minors report the recorder's
runtime; the command identifies the actual child environment. Raw bytes are
content-addressed externally at `external:yidl-undoable-stage-ef-raw`.
`corrections.jsonl` preserves interpretation/setup corrections without rewriting
historical rows or their hashes.

E01 recorded actual missing decorator/marker behavior and inherited enabled-to-
disabled reset failures before implementation, then the same focused/canonical
behavior passed. The declaration deletion canonical was written after the feature
and passed immediately: this is a **TDD sequencing deviation**, not a manufactured
RED. It covers removal and the missing-provider mutant as later verification.

F01's equal-valued distinct child suppressed a required replacement; an opaque
callback saw structural rather than historical facade results inside the fence.
These were actual pre-fix behavior failures. The unchanged opaque callback target
passed after scope/prelude integration. Canonical F later corrected its retention
precondition to keep both child roots, so that corrected fixture is verification,
not claimed byte-identical RED-to-GREEN proof. Prewritten focused scope lifecycle
checks followed; missing-private-module import errors are setup/API seam failures,
not the behavioral RED anchor. Existing native-container success fixtures and
expanded source/async/pinned-state coverage are honestly post-GREEN verification.

Multi-view conjunction generation failed on Python 3.13/14; indexed consumer
resource matching and explicit outer-bound result names fixed the unchanged rich
canonical assertions. Invalid resource/matcher authoring attempts and abandoned
final keep-name preferences remain preserved. EF03's attempted hash-slot RED
already passed (Python's generated equality already made each view unhashable);
it is verification. EF07 separately captured a genuine emitted public-name RED
and identical-target GREEN after the explicit Undoable hash-slot adapter.

The current focused F target comprises 59 tests (21 scope/fence tests, 32 native
dispatch tests and six source/bytecode boundary tests). The focused F matrix includes original opaque operands in both directions,
NotImplemented/reflection/nonbool returns, tuple length-prefix versus list order,
nonreflexive identity shortcuts, cached dictionary hashes/collisions/errors,
proxy/custom mapping boundaries, nested dict/set shapes, cycles, equal-distinct
children, all legacy/new write policies and logical inclusion combinations,
view pins, ownership/mutation fences, fault and BaseException cleanup, nested and
cross-manager contexts, copied contexts, async and thread expiry, an in-flight
prelude selection barrier, weak references and unchanged ordering/hash policies.
No performance result is claimed.

## Final gates and remaining scope

The stopped-tree full gate is `ef09-final-{backend}-{minor}-verification` for
native-rust/Python and 312/313/314: **340 passed, zero skips/failures/errors in
each run**. Older full attempts remain historical. Each
final suite includes source goldens, build-resource regeneration and A-era legacy
Undoable behavior. Dataclass's unchanged D product/shared authority has six
focused source/regeneration/neutral checks recorded in its own Stage E/F folder;
its complete D matrix remains the independently verified baseline.

`check_evidence.py` checks every sanitized/raw hash and JUnit, final six suites,
text path/hostname hygiene, and freezes owned file hashes. The manifest inventories
owned source/tests/public docs plus E/F evidence, without claiming unchanged files
were newly edited. Owner checkpoint/ledger/usage and paused UndoableLeaf documents
are excluded. Final installed wheel verification belongs to the owner.

G still owns Dataclass's field-removal canonical, public/LLM/declarative and final
installation corpus. H owns fixed-definition performance measurements and final
Code/State review. Historical B and E TDD deviations and recorded scope/process
lapses remain part of the experiment assessment.

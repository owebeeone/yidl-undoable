"""Bounded compiled-builder cache probe; not a production decorator adapter.

Only the seven-field model below and builtin annotations are qualified. Uses
current uncommitted specialization without modifying it. Cached code executes in
a fresh namespace; declaration, schema, captures and classes are never persisted.
The diagnostic __undoable_source__ string is deliberately not reconstructed on
hits. Timing comparisons use this same binding path with caching off/on.
"""

import argparse
import dataclasses
import hashlib
import importlib.metadata
import importlib.util
import json
import os
from pathlib import Path
import platform
import random
import statistics
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
RUNTIME_KEYS = {
    "default_value", "default_factory", "working_default_factory", "freeze", "thaw"
}


def dependencies():
    from yidl_cache import DependencyInventory

    files = {"probe": Path(__file__)}
    for name in ("yidl_undoable", "yidl", "astichi", "yidl_lifecycle", "yidl_dataclass"):
        spec = importlib.util.find_spec(name)
        roots = tuple(spec.submodule_search_locations)
        assert len(roots) == 1
        root = Path(roots[0])
        for path in root.rglob("*"):
            if path.suffix in {".py", ".yidl", ".so", ".pyd", ".dylib"}:
                files[f"{name}/{path.relative_to(root).as_posix()}"] = path
    return DependencyInventory.capture(files)


def declaration(seed, *, extra=False):
    from yidl_undoable import binding, const, field, lazy, local_store, managed, transient

    annotations = {
        "plain": int, "constant": int, "value": int, "delayed": int,
        "scratch": list, "resource": object, "cache": dict,
    }
    body = {
        "__annotations__": annotations,
        "plain": field(default=seed), "constant": const(default=seed + 1),
        "value": managed(default=seed + 2),
        "delayed": lazy(default_factory=lambda: seed + 10, mutable=True),
        "scratch": transient(default_factory=list, working_default_factory=list),
        "resource": binding(default=None), "cache": local_store(default_factory=dict),
    }
    if extra:
        annotations["extra"] = int
        body["extra"] = field(default=seed + 100)
    return type("CacheBench", (), body)


def shape_digest(schema, variant):
    assert not schema.validators
    fields = []
    for field in schema.fields:
        annotation = field["annotation"]
        assert annotation in (int, list, object, dict)
        fact = {key: value for key, value in field.items() if key not in RUNTIME_KEYS}
        fact["annotation"] = annotation.__name__
        fields.append(fact)
    shape = {
        "variant": variant, "name": schema.name, "fields": fields,
        "eq": schema.eq, "order": schema.order,
        "restore_identity": schema.restore_identity, "restore_order": schema.restore_order,
    }
    return hashlib.sha256(json.dumps(shape, sort_keys=True).encode()).hexdigest()


def bind(code, cls, schema, variant):
    from yidl_undoable.comparison_captures import ComparisonCaptures, capture_ids
    from yidl_undoable.facades import RuntimeFacade
    from yidl_undoable.write_comparison_context import _historical_write_scope

    carrier_type = ComparisonCaptures
    if variant == "specialized":
        from yidl_undoable.specialized import AccessorCaptures
        carrier_type = AccessorCaptures
    carrier = carrier_type(
        _historical_write_scope, RuntimeFacade.__eq__, RuntimeFacade.__hash__,
        object.__lt__, object.__le__, object.__gt__, object.__ge__,
    )
    namespace = {"__name__": cls.__module__, **dict.fromkeys(capture_ids(schema.name), carrier)}
    exec(code, namespace)
    base = type(f"{cls.__name__}_UserBase", (RuntimeFacade, cls), {"__slots__": ()})
    model = namespace["build_undoable_class"](base, schema=schema)
    model.__module__, model.__qualname__ = cls.__module__, cls.__qualname__
    return model


def check(model, seed, *, extra=False):
    from yidl_undoable import UndoRedoManager

    manager = UndoRedoManager()
    node = model(transaction_manager=manager)
    assert (node.plain, node.constant, node.value, node.delayed) == (
        seed, seed + 1, seed + 2, seed + 10,
    )
    if extra:
        assert node.extra == seed + 100
    manager.initialize(node)
    with manager.begin():
        node.value = seed + 20
        node.working.scratch.append("temporary")
        assert node.current.value == seed + 2
    assert node.value == seed + 20
    assert node.scratch == []
    assert manager.undo() and node.value == seed + 2
    assert manager.redo() and node.value == seed + 20
    try:
        with manager.begin():
            node.value = seed + 30
            raise ValueError("cancel")
    except ValueError:
        pass
    assert node.value == seed + 20
    return node


def worker(args):
    from yidl_cache import CacheRequest, CompilationContext, GeneratedCodeCache

    start = time.perf_counter_ns()
    inventory = dependencies()  # Before importing the producer/SDK modules.
    inventory_ns = time.perf_counter_ns() - start
    from yidl_undoable.undoable_harvester import harvest_undoable_definition
    from yidl_undoable.undoable import build_composable
    from yidl_undoable import _generated_undoable_base

    cache = GeneratedCodeCache(Path(args.cache), enabled=args.mode != "off")
    rows = {}
    labels = ["baseline", "specialized"]
    random.Random(args.seed).shuffle(labels)
    for variant in labels:
        producer_calls = 0
        outcomes = []
        diagnostics = []

        def decorate(seed, *, extra=False, forbid=False):
            nonlocal producer_calls
            cls = declaration(seed, extra=extra)
            schema = harvest_undoable_definition(cls, eq=False, order=False)
            compilation = CompilationContext(filename=f"<cache-probe.{variant}>")
            request = CacheRequest(
                namespace="undoable.probe." + variant, generator_revision="1",
                input_digest=shape_digest(schema, variant), compilation=compilation,
                dependencies=inventory,
            )

            def produce():
                nonlocal producer_calls
                producer_calls += 1
                if forbid:
                    raise AssertionError("warm cache invoked producer")
                module = _generated_undoable_base
                if variant == "specialized":
                    from yidl_undoable.specialized import generation_module
                    module = generation_module()
                ast_module = build_composable(schema, generation_module=module).to_executable_ast()
                return compile(
                    ast_module, compilation.filename, "exec", flags=compilation.flags,
                    dont_inherit=compilation.dont_inherit, optimize=compilation.optimize,
                )

            result = cache.get(request, produce)
            outcomes.append(type(result).__name__)
            diagnostics.append(dataclasses.asdict(cache.diagnostics[-1]))
            return bind(result.code, cls, schema, variant)

        first_start = time.perf_counter_ns()
        first = decorate(args.seed, forbid=args.mode == "disk")
        first_ns = time.perf_counter_ns() - first_start
        first_node = check(first, args.seed)
        timings = []
        for offset in range(1, 6):
            value = args.seed + offset
            before = time.perf_counter_ns()
            model = decorate(value, forbid=args.mode != "off")
            timings.append(time.perf_counter_ns() - before)
            node = check(model, value)
            assert model is not first
            assert node.cache is not first_node.cache
        if args.mode == "seed":
            # Different code shape must miss; live-value changes above must hit.
            changed = decorate(args.seed, extra=True)
            check(changed, args.seed, extra=True)
            assert outcomes[-1] == "CacheMiss"
        rows[variant] = {
            "first_ns": first_ns, "warm_ns": timings,
            "producer_calls": producer_calls, "outcomes": outcomes,
            "generated": [entry["generated"] for entry in diagnostics],
        }
        if args.mode == "disk":
            assert producer_calls == 0 and all(not entry["generated"] for entry in diagnostics)
    return {
        "mode": args.mode, "seed": args.seed, "inventory_ns": inventory_ns,
        "dependency_digest": inventory.digest, "variants": rows,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--worker", action="store_true")
    parser.add_argument("--mode", choices=("off", "seed", "disk"), default="off")
    parser.add_argument("--cache")
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--processes", type=int, default=5)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if os.environ.get("ASTICHI_LOWER_ENGINE") != "python":
        raise SystemExit("This probe qualifies only ASTICHI_LOWER_ENGINE=python")
    if args.worker:
        print(json.dumps(worker(args)))
        return
    results = []
    with tempfile.TemporaryDirectory(prefix="undoable-cache-probe-") as temporary:
        for index in range(args.processes):
            cache = str(Path(temporary).resolve() / str(index))
            for mode in ("off", "seed", "disk"):
                command = [sys.executable, str(Path(__file__).resolve()), "--worker",
                           "--mode", mode, "--cache", cache, "--seed",
                           str(1000 * index + (100 if mode == "disk" else 1))]
                before = time.perf_counter_ns()
                completed = subprocess.run(command, capture_output=True, text=True)
                if completed.returncode:
                    sys.stderr.write(completed.stderr)
                    completed.check_returncode()
                row = json.loads(completed.stdout)
                row["wall_ns"] = time.perf_counter_ns() - before
                results.append(row)
        assert len({row["dependency_digest"] for row in results}) == 1
    summary = {}
    for variant in ("baseline", "specialized"):
        summary[variant] = {}
        for mode in ("off", "seed", "disk"):
            rows = [row for row in results if row["mode"] == mode]
            summary[variant][mode] = {
                "first_ms": statistics.median(row["variants"][variant]["first_ns"] for row in rows) / 1e6,
                "warm_ms": statistics.median(statistics.median(row["variants"][variant]["warm_ns"]) for row in rows) / 1e6,
            }
    result = {
        "python": sys.version.split()[0], "platform": sys.platform,
        "machine": platform.machine(), "engine": os.environ["ASTICHI_LOWER_ENGINE"],
        "process_pairs": args.processes, "model_fields": 7,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "versions": {name: importlib.metadata.version(name) for name in (
            "yidl", "astichi", "yidl-cache", "yidl-lifecycle", "yidl-dataclass")},
        "summary": summary, "workers": results,
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

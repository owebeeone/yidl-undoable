"""Subprocess fixture for real decorator cache boundaries, not another history suite."""
import importlib
import inspect
import json
import os

from yidl_undoable import (
    UndoRedoManager, const, field, initvar, lazy, local_store, managed, undoable,
    validate_commit, DEFAULT_TRANSACTION,
)
from yidl_undoable.code_cache import cache_statistics, cache_diagnostics, clear_code_cache

adapter = importlib.import_module("yidl_undoable.undoable")
original = adapter.build_composable

def forbidden(*args, **kwargs):
    raise AssertionError("cache hit attempted model assembly")

if os.environ.get("EXPECT_DISK_HIT"):
    adapter.build_composable = forbidden


def build(offset):
    annotation = type("FreshAnnotation", (), {})
    callback = lambda seed: seed + offset
    payload = object()

    @undoable(eq=True, order=True)
    class Model:
        seed: int = initvar(default=offset)
        value: annotation = managed(default_factory=callback)
        items: tuple = managed(default=(), thaw=list, freeze=lambda value: tuple(value))
        plain: object = field(default=payload, compare=False)
        name: str = const(default=str(offset))
        memo: int = lazy(default_factory=lambda seed: seed * offset)
        scratch: dict = local_store(default_factory=lambda: {"offset": offset})

        @validate_commit(DEFAULT_TRANSACTION)
        def check(self):
            return self.value >= offset

    assert inspect.signature(Model).parameters["value"].annotation is annotation
    h = UndoRedoManager()
    model = Model(transaction_manager=h)
    h.initialize(model)
    assert model.value == 2 * offset and model.plain is payload
    assert model.memo == offset * offset and model.scratch == {"offset": offset}
    assert model.name == str(offset)
    return Model, model, h

seed = int(os.environ.get("BINDING_SEED", "2"))
first, a, h = build(seed)
before = cache_statistics()
if before is not None and before.bypasses == 0:
    adapter.build_composable = forbidden
second, b, _ = build(seed + 1)
assert first is not second and a.scratch is not b.scratch
assert first.__undoable_source__ == second.__undoable_source__
with h.begin():
    a.working.items.append(9)
assert h.undo() and a.items == ()
assert h.redo() and a.items == (9,)
adapter.build_composable = original

# Structural field additions must miss, even at the same class/compile name.
from yidl_undoable.undoable_harvester import harvest_undoable_definition
from yidl_undoable.code_cache_inputs import generation_digest
schema = harvest_undoable_definition(type("Shape", (), {"__annotations__": {"x": int}, "x": managed(default=1)}))
other = harvest_undoable_definition(type("Shape", (), {"__annotations__": {"x": int, "y": int}, "x": managed(default=1), "y": managed(default=2)}))
assert generation_digest(schema) != generation_digest(other)
stats = cache_statistics()
print(json.dumps({
    "statistics": None if stats is None else vars(stats),
    "generated": [d.generated for d in cache_diagnostics()],
    "cleared": clear_code_cache() if os.environ.get("CLEAR_CACHE") else None,
}))

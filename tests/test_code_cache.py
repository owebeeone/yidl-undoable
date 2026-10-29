"""Focused persistence, fresh-binding and fail-open integration checks."""
import json
import os
from pathlib import Path
import subprocess
import sys

FIXTURE = Path(__file__).with_name("cache_scenario.py")


def run_cache(root, **settings):
    import yidl_undoable
    env = dict(os.environ, YIDL_UNDOABLE_CACHE="on", YIDL_UNDOABLE_CACHE_DIR=str(root.resolve()), PYTHONDONTWRITEBYTECODE="1")
    env["PYTHONPATH"] = str(Path(yidl_undoable.__file__).resolve().parent.parent)
    env.update(settings)
    result = subprocess.run([sys.executable, str(FIXTURE)], env=env, capture_output=True, text=True, timeout=120)
    assert result.returncode == 0, result.stdout + result.stderr
    return json.loads(result.stdout)


def test_cold_memory_and_fresh_process_hits_rebind_runtime_objects(tmp_path):
    cold = run_cache(tmp_path)
    assert cold["statistics"] == {"hits": 1, "misses": 1, "bypasses": 0}
    assert cold["generated"] == [True, False]
    fresh = run_cache(tmp_path, EXPECT_DISK_HIT="1", BINDING_SEED="11", CLEAR_CACHE="1")
    assert fresh["statistics"] == {"hits": 2, "misses": 0, "bypasses": 0}
    assert fresh["generated"] == [False, False]
    assert fresh["cleared"] > 0


def test_disabled_and_unavailable_storage_preserve_generation(tmp_path):
    disabled = run_cache(tmp_path / "off", YIDL_UNDOABLE_CACHE="off")
    assert disabled["statistics"] is None
    assert not (tmp_path / "off").exists()
    blocked = tmp_path / "blocked"
    blocked.write_text("not a directory")
    bypass = run_cache(blocked)
    assert bypass["statistics"] == {"hits": 0, "misses": 0, "bypasses": 2}
    assert bypass["generated"] == [True, True]

"""Run the existing behavior suite against the opt-in experimental decorator.

The ordinary canonical harness compares baseline source bytes, so its behavior
stories run instead through test_specialized.py. Baseline builder regeneration
checks run in the normal full suite. No golden outputs are rewritten here.
"""

import importlib
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))


def main():
    import pytest
    import yidl_undoable
    from yidl_undoable.specialized import undoable

    yidl_undoable.undoable = undoable
    importlib.import_module("yidl_undoable.undoable").undoable = undoable
    return pytest.main(
        [
            str(ROOT / "tests"),
            "-q",
            "-p",
            "no:cacheprovider",
            "--tb=short",
            "--ignore=" + str(ROOT / "tests" / "test_canonical.py"),
            "--ignore=" + str(ROOT / "tests" / "test_generation.py"),
            *sys.argv[1:],
        ]
    )


if __name__ == "__main__":
    raise SystemExit(main())

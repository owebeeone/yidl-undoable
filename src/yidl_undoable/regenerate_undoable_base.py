from __future__ import annotations

import argparse
import difflib
from pathlib import Path
import sys

from yidl.concept_parser import compile_yidl_files
from yidl.generation.data_def_sys import emit_concept_runtime_source

_PACKAGE_ROOT = Path(__file__).resolve().parent
_PROJECT_ROOT = _PACKAGE_ROOT.parent.parent
_YIDL_SOURCE_DIR = _PACKAGE_ROOT / "yidl"
_GENERATED_BASE_PATH = _PACKAGE_ROOT / "_generated_undoable_base.py"
_ENTRY_PATH = _YIDL_SOURCE_DIR / "undoable_base.yidl"
_CONCEPT_NAME = "UndoableBase"
_LOGICAL_RESOURCE_ROOT = Path("src/yidl_undoable/yidl")


def render_undoable_base_source(
    *,
    source_dir: Path = _YIDL_SOURCE_DIR,
    entry_path: Path = _ENTRY_PATH,
    project_root: Path = _PROJECT_ROOT,
) -> str:
    """Render layers with stable logical names across source and wheel layouts.

    ``project_root`` is retained for callers that supply a source checkout;
    physical locations must not affect the generated source's resource IDs.
    """

    del project_root

    paths = tuple(sorted(source_dir.glob("*.yidl")))
    compiled = compile_yidl_files(
        {
            (_LOGICAL_RESOURCE_ROOT / path.name).as_posix(): path.read_text(
                encoding="utf-8"
            )
            for path in paths
        },
        (_LOGICAL_RESOURCE_ROOT / entry_path.name).as_posix(),
    )
    concept = compiled.concepts[_CONCEPT_NAME]
    return emit_concept_runtime_source(
        concept.plan.build_data_definition(),
        resources=concept.resources,
        assembly_plan=concept,
    )


def check_undoable_base(
    *,
    generated_path: Path = _GENERATED_BASE_PATH,
) -> tuple[bool, str]:
    """Return whether the committed generated base matches regenerated source."""

    expected = generated_path.read_text(encoding="utf-8")
    actual = render_undoable_base_source()
    if actual == expected:
        return True, ""
    diff = "\n".join(
        difflib.unified_diff(
            expected.splitlines(),
            actual.splitlines(),
            fromfile=generated_path.as_posix(),
            tofile="regenerated undoable base",
            lineterm="",
        ),
    )
    return False, diff


def write_undoable_base(
    *,
    generated_path: Path = _GENERATED_BASE_PATH,
) -> None:
    """Rewrite the committed generated base from the checked-in YIDL layers."""

    generated_path.write_text(render_undoable_base_source(), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Regenerate or check src/yidl_undoable/_generated_undoable_base.py "
            "from src/yidl_undoable/yidl/*.yidl."
        ),
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="rewrite the generated undoable base instead of checking it",
    )
    args = parser.parse_args(argv)

    if args.write:
        write_undoable_base()
        print(f"wrote {_GENERATED_BASE_PATH.relative_to(_PACKAGE_ROOT.parent.parent)}")
        return 0

    ok, diff = check_undoable_base()
    if ok:
        print("generated undoable base matches")
        return 0
    print(diff, file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

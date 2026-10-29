"""Execute canonical stories and capture their actual generated executable source."""

from pathlib import Path
import runpy
import sys

STORIES = Path(__file__).parent / "data" / "gold_src"
GOLDEN = Path(__file__).parent / "data" / "golden"


def run_story(story):
    namespace = runpy.run_path(str(story), run_name="__canonical__")
    models = [
        (name, value.__dict__["__undoable_source__"])
        for name, value in namespace.items()
        if isinstance(value, type) and "__undoable_source__" in value.__dict__
    ]
    models.extend(namespace.get("LAYER_SOURCES", ()))
    return "\n".join(
        f"# Generated model: {name}\n{source}" for name, source in sorted(models)
    )


def golden_path(story):
    # Native hygiene spells a few private capture aliases differently. Preserve
    # exact inspectable source for each backend instead of normalizing it away.
    from astichi.lower_engine import select_effective_lower_engine
    native = select_effective_lower_engine().selected_engine.startswith("native")
    suffix = ".native" if native and story.stem.startswith(("16_", "20_", "21_")) else ""
    if story.stem.startswith(("21_", "22_", "23_", "24_")):
        minor = f"py{sys.version_info.major}{sys.version_info.minor}"
        return GOLDEN / f"{story.stem}.{minor}{suffix}.generated.py"
    return GOLDEN / (story.stem + suffix + ".generated.py")

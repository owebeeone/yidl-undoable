"""Execute canonical stories and capture their actual generated executable source."""

from pathlib import Path
import runpy

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

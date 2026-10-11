"""Regenerate only after each canonical behavior story passes."""

import argparse
from canonical_support import STORIES, GOLDEN, run_story


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    for story in sorted(STORIES.glob("*.py")):
        actual = run_story(story)
        target = GOLDEN / (story.stem + ".generated.py")
        if args.write:
            target.write_text(actual)
        elif target.read_text() != actual:
            raise SystemExit(f"golden mismatch: {target.name}")
    print(
        "canonical generated-source goldens match"
        if not args.write
        else "wrote canonical generated-source goldens"
    )


if __name__ == "__main__":
    main()

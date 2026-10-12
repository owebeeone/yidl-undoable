"""Regenerate only after each canonical behavior story passes."""

import argparse
from canonical_support import STORIES, GOLDEN, run_story, golden_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("stories", nargs="*")
    args = parser.parse_args()
    for story in sorted(STORIES.glob("*.py")):
        if args.stories and story.name not in args.stories:
            continue
        actual = run_story(story)
        target = golden_path(story)
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

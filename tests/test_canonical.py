"""Canonical generated-class scenarios and deterministic executable-source goldens."""

import pytest
from canonical_support import STORIES, GOLDEN, run_story


@pytest.mark.parametrize("story", sorted(STORIES.glob("*.py")), ids=lambda p: p.stem)
def test_generated_story(story):
    actual = run_story(story)
    expected = (GOLDEN / (story.stem + ".generated.py")).read_text()
    assert actual == expected

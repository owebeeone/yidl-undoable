# Contributing

Run the existing semantic tests and canonical generated-source stories before
changing behavior. Source goldens are also inspection examples; keep contrasting
field policies visible. See [generation and history](docs/Architecture.md) and the
[experiment records](dev-docs/README.md) for implementation evidence.

Install development and regeneration dependencies in an isolated environment:

```sh
python -m pip install '.[dev,regenerate]'
python -m pytest -q
python -m yidl_undoable.regenerate_undoable_base
python tests/regenerate_golden.py
```

The regeneration extra pins the Dataclass comparison authority. Normal model
use does not import Dataclass. SDKs are dependencies, not implicit edit targets;
record outside-scope findings separately. Use `--write` only when intentionally
updating generated artifacts. Comparison source goldens are Python-version-specific; three stories also retain
explicit native-backend goldens for different private capture alias spelling.

For documentation:

```sh
python -m pip install -r docs-requirements.txt
python dev-docs/documentation/verify_examples.py
python -m mkdocs build --strict
python dev-docs/documentation/check_site.py build/docs-site
```

The workflow installs the packaged checkout and registry dependencies; local
editable sibling overrides in `tool.uv.sources` are not that qualification route.
Verify substantive public documentation with an independent review before pushing.
Development records and `docs/validation` do not belong in the public site.
Package releases use [Gearu](RELEASE.md), separately from documentation deployment.

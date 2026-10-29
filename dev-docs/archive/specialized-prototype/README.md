# Pre-integration specialized accessor prototype

The original specialization measurements predate promotion to the normal decorator
and compiled-builder caching. They are not measurements of the later integration.
These verbatim source snapshots retain the two prototype files subsequently edited;
`.txt` prevents them from being mistaken for current executable helpers.

- `specialized.py.txt`: original opt-in dynamic adapter.
- `benchmark_specialized.py.txt`: original benchmark driver.
- `tracked.patch`: original tracked edits against baseline
  `307c0ff6924b5c405f2d287b14448d0006cfe35a`.

The original [source digest inventory](../../experiment/specialized-accessors-source-sha256.json)
identifies the remaining unchanged authored resource, test, driver and runtime
files, plus the baseline generated builder. Reconstruct the prototype only in an
isolated checkout of that baseline, apply the patch, restore these adapters and
copy the unchanged prototype additions identified by the inventory. The
[raw measurements](../../experiment/specialized-accessors-python312.json) and
[report](../../SpecializedAccessorExperiment.md) retain the actual old environment
and commands. The integration does not retroactively change their scope.

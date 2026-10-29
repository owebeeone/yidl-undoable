# Cache generated builders

Builder caching and these controls are added in `yidl-undoable==0.1.2`.
They are not available in version 0.1.1. This is generated-code caching, not
storage of undo history.

Undoable normally persists compiled model-builder code using YIDL Cache. A hit
skips YIDL/Astichi assembly and compilation for that model shape, then creates a
fresh class and binds its current schema, defaults and callbacks. It does not
cache live instances, history, callback results, or generated class identity.

## Controls

Set these before the first import of `yidl_undoable`:

| Environment variable | Behavior |
| --- | --- |
| `YIDL_UNDOABLE_CACHE=off` | Disable compiled-builder reuse |
| `YIDL_UNDOABLE_CACHE=on` or unset | Enable optional reuse |
| `YIDL_UNDOABLE_CACHE_DIR=directory` | Use that root instead of default locations; `off` wins |

The default tries a source-adjacent `__pycache__/yidl_cache` location, then a
per-user `.yidl/cache` location. The explicit root is namespace-separated.
These are executable code artifacts: use a directory you control, not shared
untrusted storage. Unsupported identity or unavailable/untrusted storage safely
falls back to generation. Settings are fixed at import; restart after changing
them or generator dependencies. Caching does not add manager thread/task isolation.

## Inspect and clear

```python
from yidl_undoable.code_cache import (
    cache_configuration, cache_statistics, cache_diagnostics, clear_code_cache,
)

configuration = cache_configuration()
statistics = cache_statistics()  # None when disabled.
diagnostics = cache_diagnostics()  # Recent completed requests, no automatic logging.
```

`clear_code_cache()` explicitly clears cache locations tracked by this process;
it is not a scan of every user's cache directory. Generated source remains
available as `Model.__undoable_source__` on both misses and hits.

Field-specific accessors reduce dispatch on ordinary fields, constants and ready
lazy values; managed reads still perform history selection. Caching addresses
class generation, not commit cost or the history algorithm. The
[accessor experiment](../dev-docs/SpecializedAccessorExperiment.md) and
[bounded cache probe](../dev-docs/SpecializedAccessorCacheProbe.md) record their own
workloads; their timings are not a general performance guarantee.

"""Optional compiled-builder persistence; fresh class execution stays consumer-owned."""

from dataclasses import dataclass
from importlib.machinery import EXTENSION_SUFFIXES
from importlib.util import find_spec
import os
from pathlib import Path
import sys
from types import ModuleType

from yidl_cache import (
    CacheDependencyError, CacheIdentityError, CacheLocationPolicy, CacheRequest,
    DependencyInventory, GeneratedCodeCache, SourceOrigin,
)

from .code_cache_inputs import generation_digest

_NAMESPACE = "yidl_undoable.builder"
_REVISION = "specialized-v1"
_SOURCE_TAG = "yidl_undoable.source-v1"


@dataclass(frozen=True)
class CacheConfiguration:
    enabled: bool
    override_root: Path | None = None
    user_root: Path | None = None
    problem: str | None = None


def _configuration():
    setting = os.environ.get("YIDL_UNDOABLE_CACHE", "").strip().lower()
    if setting == "off":
        return CacheConfiguration(False)
    if setting not in {"", "on"}:
        return CacheConfiguration(False, problem="YIDL_UNDOABLE_CACHE must be on or off")
    try:
        home = Path.home()
    except (OSError, RuntimeError, ValueError):
        home = None
    try:
        directory = os.environ.get("YIDL_UNDOABLE_CACHE_DIR", "")
        if directory.startswith("~"):
            if home is None or (directory != "~" and not directory.startswith("~/")):
                return CacheConfiguration(False, problem="unsupported cache-root home expansion")
            directory = str(home / directory[2:]) if directory != "~" else str(home)
        if "\x00" in directory:
            return CacheConfiguration(False, problem="invalid cache root")
        override = Path(os.path.abspath(directory)) if directory else None
        return CacheConfiguration(True, override, None if home is None else home / ".yidl/cache")
    except (OSError, RuntimeError, ValueError):
        return CacheConfiguration(False, problem="cache root is unavailable")


def _dependencies():
    sources = {}
    for name in ("yidl_undoable", "yidl", "astichi", "yidl_lifecycle"):
        spec = find_spec(name)
        if spec is None or not spec.submodule_search_locations:
            raise CacheDependencyError("producer package source is unavailable")
        roots = tuple(spec.submodule_search_locations)
        if len(roots) != 1:
            raise CacheDependencyError("producer source is ambiguous")
        root = Path(roots[0])
        found = False
        for path in root.rglob("*"):
            if path.suffix in {".py", ".yidl"} or path.name.endswith(tuple(EXTENSION_SUFFIXES)):
                sources[f"{name}/{path.relative_to(root).as_posix()}"] = path
                found = True
        if not found:
            raise CacheDependencyError("producer package has no source inventory")
        if name == "astichi":
            for parent in root.parents:
                native = parent / "native_engine"
                if (native / "Cargo.toml").is_file():
                    for path in native.glob("_astichi_native_engine*"):
                        if path.name.endswith(tuple(EXTENSION_SUFFIXES)):
                            sources[f"astichi/native/{path.name}"] = path
                    break
    native = find_spec("_astichi_native_engine")
    if native is not None:
        if not native.origin:
            raise CacheDependencyError("native engine provenance unavailable")
        sources["astichi/installed-native"] = Path(native.origin)
    return DependencyInventory.capture(sources)


_configuration_value = _configuration()
_inventory = None
if _configuration_value.enabled:
    try:
        _inventory = _dependencies()
    except (CacheDependencyError, OSError, ImportError, ValueError):
        pass
_policy = CacheLocationPolicy(_configuration_value.override_root, _configuration_value.user_root)
_cache = GeneratedCodeCache(enabled=True) if _configuration_value.enabled else None


def with_source(code, source):
    """Attach diagnostic text as inert constants; executable instructions stay intact."""
    return code.replace(co_consts=(*code.co_consts, (_SOURCE_TAG, source)))


def source_from_code(code):
    metadata = code.co_consts[-1] if code.co_consts else None
    if (
        type(metadata) is not tuple or len(metadata) != 2
        or metadata[0] != _SOURCE_TAG or type(metadata[1]) is not str
    ):
        raise CacheIdentityError("Undoable builder source metadata is unavailable")
    return metadata[1]


def compiled_builder(schema, declaration, compilation, produce):
    if _cache is None:
        return produce()
    try:
        digest = generation_digest(schema)
        module = sys.modules.get(declaration.__module__)
        filename = vars(module).get("__file__") if type(module) is ModuleType else None
        source = Path(filename).absolute() if type(filename) is str and not filename.startswith("<") else None
        locations = _policy.locations_for(
            _NAMESPACE, SourceOrigin(source, declaration.__module__)
        )
    except (CacheIdentityError, OSError, UnicodeError, ValueError):
        return _cache.bypass(
            _NAMESPACE, produce, CacheIdentityError("unsupported Undoable cache identity/location")
        ).code
    request = CacheRequest(_NAMESPACE, _REVISION, digest, compilation, _inventory)
    result = _cache.get(request, produce, locations=locations)
    try:
        source_from_code(result.code)
    except CacheIdentityError as error:
        return _cache.bypass(_NAMESPACE, produce, error).code
    return result.code


def cache_configuration():
    return _configuration_value


def cache_statistics():
    return None if _cache is None else _cache.statistics


def cache_diagnostics():
    return () if _cache is None else _cache.diagnostics


def clear_code_cache():
    return 0 if _cache is None else _cache.clear()

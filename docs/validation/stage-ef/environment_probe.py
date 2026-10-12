"""Record original-wheel versions/origins without importing workspace SDKs."""

from __future__ import annotations
import hashlib
import importlib.metadata as metadata
import json
import os
from pathlib import Path
import sys
import astichi
import yidl
import yidl_lifecycle
import yidl_dataclass
from importlib.resources import files
from astichi.lower_engine import select_effective_lower_engine


def main() -> None:
    output = Path(sys.argv[1])
    wheelhouse = Path(os.environ["SDK_WHEELHOUSE"])
    prefix = Path(sys.prefix).resolve()
    modules = {}
    for module, expected in (
        (astichi, "1.1.3"),
        (yidl, "0.1.0"),
        (yidl_lifecycle, "0.1.0"),
        (yidl_dataclass, "0.1.0.dev0"),
    ):
        origin = Path(module.__file__).resolve()
        assert origin.is_relative_to(prefix), module.__name__
        assert metadata.version(module.__name__) == expected
        modules[module.__name__] = {
            "version": expected,
            "origin_relative_to_prefix": origin.relative_to(prefix).as_posix(),
        }
    wheels = {}
    for name in (
        "astichi-1.1.3-cp312-abi3-macosx_11_0_arm64.whl",
        "yidl-0.1.0-py3-none-any.whl",
        "yidl_lifecycle-0.1.0-py3-none-any.whl",
    ):
        wheels[name] = hashlib.sha256((wheelhouse / name).read_bytes()).hexdigest()
    authority = Path(os.environ["DATACLASS_AUTHORITY_WHEEL"])
    authority_hash = hashlib.sha256(authority.read_bytes()).hexdigest()
    assert (
        authority_hash
        == "845b55e814a7b56be4cda0964393962fbcf977898eae068bb1c489ebd1ff0942"
    )
    shared_hash = hashlib.sha256(
        files("yidl_dataclass").joinpath("yidl/shared/comparison.yidl").read_bytes()
    ).hexdigest()
    assert (
        shared_hash
        == "2f7e6df989b0714d8764de84d8a6f6b03f39c3ad7f57dba5e55f5131b8354eef"
    )
    payload = {
        "dataclass_authority_wheel": {"name": authority.name, "sha256": authority_hash},
        "shared_comparison_sha256": shared_hash,
        "python": sys.version,
        "implementation": sys.implementation.name,
        "sdk_modules": modules,
        "original_wheel_sha256": wheels,
        "selected_backend": select_effective_lower_engine().selected_engine,
        "dependencies": {
            item.metadata["Name"]: item.version for item in metadata.distributions()
        },
    }
    output.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")


if __name__ == "__main__":
    main()

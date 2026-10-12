"""Undoable-owned G distribution/source evidence and unchanged runtime tuple."""

from __future__ import annotations
import hashlib
import json
from pathlib import Path
import socket
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[3]
EVIDENCE = ROOT / "docs/validation/stage-g"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    rows = [
        json.loads(line)
        for line in (EVIDENCE / "increments.jsonl").read_text().splitlines()
    ]
    references = [item for row in rows for item in row["artifacts"]]
    raw = Path(tempfile.gettempdir()) / "yidl-undoable-stage-g-raw"
    for item in references:
        assert digest(ROOT / item["path"]) == item["sha256"]
        assert digest(raw / (item["raw_sha256"] + ".raw")) == item["raw_sha256"]
    assert all(row["exit_code"] == 0 for row in rows if row["phase"] != "red")
    xmls = sorted(EVIDENCE.glob("*.junit.xml"))
    for path in xmls:
        ET.parse(path)
    prior = json.loads(
        (ROOT / "docs/validation/stage-ef/owned-manifest.json").read_text()
    )
    previous = {row["path"]: row["sha256"] for row in prior["files"]}
    paths = [
        ROOT / name
        for name in (
            "README.md",
            "pyproject.toml",
            ".gitignore",
            "docs/API.md",
            "docs/Architecture.md",
        )
    ]
    for directory in (ROOT / "src", ROOT / "tests", ROOT / "examples", EVIDENCE):
        paths.extend(
            path
            for path in directory.rglob("*")
            if path.is_file()
            and "__pycache__" not in path.parts
            and path.name not in ("owned-manifest.json", "evidence-qa.json")
        )
    assert all(
        previous[path.relative_to(ROOT).as_posix()] == digest(path)
        for path in paths
        if path.relative_to(ROOT).as_posix().startswith("src/")
    )
    for path in paths:
        assert not any(
            part in path.read_text()
            for part in (
                str(ROOT),
                str(Path.home()),
                tempfile.gettempdir(),
                socket.gethostname(),
            )
        ), path.relative_to(ROOT)
    qa = {
        "increments": len(rows),
        "artifact_references": len(references),
        "distinct_raw_hashes": len({row["raw_sha256"] for row in references}),
        "junit_files": len(xmls),
        "runtime_source_unchanged_from_ef": True,
        "absolute_path_or_hostname_matches": 0,
        "sdk_or_lifecycle_changes_or_builds": False,
        "paired_installed_evidence": "external:yidl-dataclass-stage-g-owned-evidence",
    }
    q = EVIDENCE / "evidence-qa.json"
    q.write_text(json.dumps(qa, sort_keys=True, indent=2) + "\n")
    paths.append(q)
    manifest = {
        "stage": "G consumer packaging",
        "baseline_owner_commit": "bedec080d1d3531d7a250b9e4f729040c57645c7",
        "raw_archive": "external:yidl-undoable-stage-g-raw",
        "files": [],
    }
    for path in sorted(paths):
        name = path.relative_to(ROOT).as_posix()
        sha = digest(path)
        manifest["files"].append(
            {
                "path": name,
                "bytes": path.stat().st_size,
                "sha256": sha,
                "stage_ef_relation": (
                    "new"
                    if name not in previous
                    else "unchanged" if previous[name] == sha else "changed"
                ),
            }
        )
    output = EVIDENCE / "owned-manifest.json"
    output.write_text(json.dumps(manifest, sort_keys=True, indent=2) + "\n")
    print(
        json.dumps(
            {
                "owned_files": len(paths),
                "manifest_sha256": digest(output),
                "qa_sha256": digest(q),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()

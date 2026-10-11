"""Record sanitized token counters from one actor's local Codex session log."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path


def collect(session: Path) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    usage: list[dict[str, object]] = []
    contexts: list[dict[str, object]] = []
    for line in session.read_text(encoding="utf-8").splitlines():
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        payload = row.get("payload", {})
        if row.get("type") == "turn_context":
            contexts.append({"time": row["timestamp"], "model": payload.get("model"), "effort": payload.get("effort")})
        if row.get("type") == "event_msg" and payload.get("type") == "token_count":
            info = payload.get("info") or {}
            if info.get("total_token_usage"):
                last = info.get("last_token_usage") or {}
                usage.append({"time": row["timestamp"], "counts": info["total_token_usage"],
                              "request_input_tokens": last.get("input_tokens")})
    return usage, contexts


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--session", type=Path, required=True)
    parser.add_argument("--actor", default="lane-owner")
    parser.add_argument("--phase", required=True)
    parser.add_argument("--start", required=True)
    parser.add_argument("--at", help="Retrospective cutoff; defaults to latest usage")
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("usage.jsonl"))
    args = parser.parse_args()
    usage, contexts = collect(args.session)
    baseline = [item for item in usage if item["time"] < args.start]
    selected = [item for item in usage if args.at is None or item["time"] <= args.at]
    if not selected:
        raise SystemExit("No token observation available for this checkpoint")
    sample = selected[-1]
    request_sizes = [item["request_input_tokens"] for item in selected
                     if item["time"] >= args.start and item["request_input_tokens"] is not None]
    counts = sample["counts"]
    base = baseline[-1]["counts"] if baseline else {key: 0 for key in counts}
    delta = {key: counts[key] - base.get(key, 0) for key in counts}
    if any(value < 0 for value in delta.values()):
        raise SystemExit("Counters reset; a new, explicitly recorded baseline is needed")
    context = [item for item in contexts if item["time"] <= sample["time"]]
    metadata = context[-1] if context else {}
    cost = None
    if metadata.get("model") == "gpt-6.1-sol":
        input_count = delta.get("input_tokens", 0)
        cached = delta.get("cached_input_tokens", 0)
        writes = delta.get("cache_write_input_tokens", 0)
        if cached + writes > input_count:
            raise SystemExit("Cached counts exceed input; pricing basis requires inspection")
        cost = ((input_count - cached - writes) * 2 + cached * 0.1 + writes * 2.5 + delta.get("output_tokens", 0) * 10) / 1_000_000
    record = {
        "actor": args.actor, "phase": args.phase, "experiment_start_utc": args.start,
        "recorded_utc": datetime.now(timezone.utc).isoformat(),
        "usage_observed_utc": sample["time"], "retrospective": args.at is not None,
        "model": metadata.get("model"), "reasoning_effort": metadata.get("effort"),
        "baseline": base, "cumulative": counts, "experiment_delta": delta,
        "maximum_observed_request_input_tokens": max(request_sizes) if request_sizes else None,
        "standard_api_equivalent_usd": cost, "actual_billed_usd": None,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("a", encoding="utf-8") as output:
        output.write(json.dumps(record, sort_keys=True) + "\n")
    print(json.dumps({"actor": args.actor, "phase": args.phase, "delta": delta, "standard_api_equivalent_usd": cost}))


if __name__ == "__main__":
    main()

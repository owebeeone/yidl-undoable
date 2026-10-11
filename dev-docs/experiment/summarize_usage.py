"""Summarize the latest disjoint actor observations for one experiment baseline."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lane-start", required=True)
    parser.add_argument("--input", type=Path, default=Path(__file__).with_name("usage.jsonl"))
    args = parser.parse_args()
    latest = {}
    for line in args.input.read_text(encoding="utf-8").splitlines():
        record = json.loads(line)
        if record["actor"] == "lane-owner":
            if record["experiment_start_utc"] != args.lane_start:
                continue
        latest[record["actor"]] = record
    if "lane-owner" not in latest:
        raise SystemExit("No lane-owner observation for the requested baseline")
    counts = {}
    estimates = []
    actors = []
    for actor, record in sorted(latest.items()):
        for key, value in record["experiment_delta"].items():
            counts[key] = counts.get(key, 0) + value
        estimate = record["standard_api_equivalent_usd"]
        estimates.append(estimate)
        actors.append({"actor": actor, "phase": record["phase"],
                       "observed_utc": record["usage_observed_utc"],
                       "standard_api_equivalent_usd": estimate})
    print(json.dumps({"lane_start_utc": args.lane_start, "actors": actors,
                      "disjoint_observed_tokens": counts,
                      "standard_api_equivalent_usd": None if None in estimates else sum(estimates),
                      "actual_billed_usd": None}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

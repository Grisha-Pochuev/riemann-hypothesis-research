#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from mpmath import mp

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from riemann_lab import normalized_gap, verify_indexed_zeros, zero_counting_main_term


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize finite statistics of indexed zeta zeros")
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--count", type=int, default=50)
    parser.add_argument("--dps", type=int, default=50)
    args = parser.parse_args()

    if args.start < 1 or args.count < 2:
        parser.error("start must be positive and count must be at least two")

    records = verify_indexed_zeros(range(args.start, args.start + args.count), dps=args.dps)
    ordinates = [record.imaginary for record in records]
    gaps = [normalized_gap(a, b) for a, b in zip(ordinates, ordinates[1:])]
    top = ordinates[-1]

    payload = {
        "experiment": "zero-gap-summary",
        "start_index": args.start,
        "count": args.count,
        "dps": args.dps,
        "first_ordinate": mp.nstr(ordinates[0], 25),
        "last_ordinate": mp.nstr(top, 25),
        "mean_normalized_gap": mp.nstr(mp.fsum(gaps) / len(gaps), 20),
        "minimum_normalized_gap": mp.nstr(min(gaps), 20),
        "maximum_normalized_gap": mp.nstr(max(gaps), 20),
        "counting_main_term_at_last_zero": mp.nstr(zero_counting_main_term(top), 20),
    }
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()

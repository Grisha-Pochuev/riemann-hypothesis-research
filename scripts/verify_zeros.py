#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from riemann_lab import verify_indexed_zeros


def main() -> None:
    parser = argparse.ArgumentParser(description="Verify indexed zeta zeros at high precision")
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--count", type=int, default=10)
    parser.add_argument("--dps", type=int, default=50)
    args = parser.parse_args()

    if args.start < 1 or args.count < 1:
        parser.error("start and count must be positive")

    indices = range(args.start, args.start + args.count)
    for record in verify_indexed_zeros(indices, dps=args.dps):
        payload = {"experiment": "indexed-zero-verification", "dps": args.dps, **record.as_dict()}
        print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()

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

from riemann_lab import hardy_z


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan Hardy Z(t) and report sign-change brackets")
    parser.add_argument("--start", type=float, default=10.0)
    parser.add_argument("--stop", type=float, default=50.0)
    parser.add_argument("--step", type=float, default=0.05)
    parser.add_argument("--dps", type=int, default=40)
    args = parser.parse_args()

    if args.stop <= args.start or args.step <= 0:
        parser.error("require stop > start and step > 0")

    with mp.workdps(args.dps):
        left = mp.mpf(args.start)
        left_value = hardy_z(left)
        while left < args.stop:
            right = min(left + args.step, mp.mpf(args.stop))
            right_value = hardy_z(right)
            if left_value == 0 or right_value == 0 or mp.sign(left_value) != mp.sign(right_value):
                print(
                    json.dumps(
                        {
                            "experiment": "hardy-z-sign-change",
                            "left": mp.nstr(left, 20),
                            "right": mp.nstr(right, 20),
                            "z_left": mp.nstr(left_value, 20),
                            "z_right": mp.nstr(right_value, 20),
                            "dps": args.dps,
                        },
                        sort_keys=True,
                    )
                )
            left, left_value = right, right_value


if __name__ == "__main__":
    main()

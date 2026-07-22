# Riemann Hypothesis Research

A reproducible computational workspace for experiments related to the **Riemann Hypothesis**, the Riemann zeta function, and the statistics of its nontrivial zeros.

> **Status:** exploratory numerical research. This repository does not claim a proof or disproof of the Riemann Hypothesis.

## Mathematical focus

The Riemann Hypothesis states that every nontrivial zero of the analytically continued zeta function

\[
\zeta(s)=\sum_{n=1}^{\infty} n^{-s}
\]

has real part `1/2`. Computation can test finite ranges, validate implementations, compare zero-counting estimates, and search for numerical patterns. It cannot by itself establish a statement about all zeros.

This project currently studies:

- high-precision evaluation of `zeta(s)`;
- verification of zeros on the critical line;
- Hardy's real-valued `Z(t)` function;
- normalized gaps between consecutive zeros;
- comparison with the main term of the Riemann--von Mangoldt zero-counting formula;
- reproducible records for finite numerical experiments.

## Repository layout

```text
src/riemann_lab/       Reusable numerical routines
scripts/               Command-line experiment drivers
tests/                 Numerical and structural tests
docs/                  Research plan, methods, and interpretation limits
experiments/            Dated, reproducible experiment records
.github/workflows/      Automated test workflow
```

## Quick start

```bash
python -m pip install -e .[dev]
pytest
python scripts/verify_zeros.py --count 20 --dps 60
python scripts/scan_hardy_z.py --start 10 --stop 50 --step 0.05
python scripts/zero_statistics.py --count 100 --dps 50
```

Each script prints machine-readable JSON Lines so results can be redirected into a dated experiment directory.

## Current baseline

The initial baseline uses `mpmath` for arbitrary-precision arithmetic. It provides:

- evaluation of the completed zeta symmetry residual;
- the Riemann--Siegel theta function;
- Hardy's `Z(t)` function;
- direct retrieval and residual checking of indexed critical-line zeros;
- normalized consecutive-zero gaps;
- the leading zero-counting approximation.

The baseline is intentionally small and transparent. It is designed for verification and extension rather than record-scale zero checking.

## Research discipline

Every result should be labeled as one of:

1. an implementation check;
2. a finite numerical observation;
3. a conjectural pattern suggested by data;
4. a proved mathematical statement.

Finite verification is not a proof of the Riemann Hypothesis. A small residual is not an exact symbolic certificate, and an observed pattern over the first zeros is not automatically asymptotic.

## Reproducibility

A complete experiment record includes the source commit, command, precision, parameter range, software versions, raw output, and a short interpretation note. See [`experiments/README.md`](experiments/README.md).

## License

MIT License. See [LICENSE](LICENSE).

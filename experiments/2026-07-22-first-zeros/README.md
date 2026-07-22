# First indexed zeros baseline

## Question

Does the initial implementation reproduce the first indexed critical-line zeros with small zeta residuals and negligible deviation from real part `1/2` at 60 decimal digits?

## Command

```bash
python scripts/verify_zeros.py --start 1 --count 10 --dps 60 > results.jsonl
```

## Interpretation

This run is an implementation baseline only. It checks a small finite set of values supplied through an indexed-zero routine and reevaluates the zeta function at those points. It is not an independent completeness proof and has no implication for all nontrivial zeros.

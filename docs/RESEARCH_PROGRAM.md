# Research Program

## Central objective

Build a transparent, reproducible environment for finite experiments involving the zeta function and its nontrivial zeros. The goal is not to convert numerical evidence into a proof. The goal is to discover precise finite statements, stress-test proposed lemmas, and produce observations that can be formulated mathematically.

## Initial workstreams

### 1. Numerical validation

Cross-check the implementation through identities that are independent of indexed-zero retrieval:

- the functional equation for the completed zeta function;
- conjugation symmetry;
- real-valuedness of Hardy's `Z(t)` for real `t`;
- agreement between `Z(t)` sign changes and indexed zero ordinates.

### 2. Zero spacing

Record consecutive zero gaps after normalization by the local mean spacing. Compare distributions across disjoint index windows and different precision levels. Treat any apparent regularity as an empirical statement about the tested window only.

### 3. Zero counting

Compare the exact number of indexed zeros below a tested height with successive approximations to the Riemann--von Mangoldt formula. Separate the smooth main term from the oscillatory remainder.

### 4. Critical-line scans

Use Hardy's function to generate sign-change brackets. Investigate missed zeros, closely spaced zeros, and the effect of scan resolution. A sign-change scan is a detection method, not a completeness certificate without additional arguments.

### 5. Candidate finite lemmas

Use computation to reject false universal claims and search for sharp constants in explicitly bounded ranges. Any surviving statement should be reformulated with exact quantifiers before proof work begins.

## Near-term hypotheses

The following are working numerical hypotheses, not established results:

1. Normalized-gap summaries stabilize slowly as the sampled index window moves upward.
2. Uniform-step scans require increasingly fine resolution to preserve the same practical detection rate.
3. The main zero-counting term tracks the correct scale while the residual remains visibly structured.
4. Precision requirements depend more strongly on height and cancellation than on the number of requested zeros alone.

## Reporting rule

Every report must state the index range, height range, working precision, software version, source commit, and detection method. Words such as "verified" must always be followed by a finite range and a numerical tolerance.

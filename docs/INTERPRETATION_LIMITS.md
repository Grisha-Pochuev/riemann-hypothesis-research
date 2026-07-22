# Interpretation Limits

## What finite computation can establish

A reproducible calculation can establish that a particular program, at a stated precision, returned values satisfying stated numerical tolerances over a finite range. It can also disprove a universal numerical conjecture by producing a valid counterexample within its domain.

## What it cannot establish alone

Finite computation cannot prove that every nontrivial zeta zero has real part `1/2`. It cannot infer an asymptotic law solely from a visually convincing finite plot, and it cannot prove that an interval contains no missed zeros unless the computation includes a mathematically justified completeness method.

## Common failure modes

- treating a small floating-point residual as exact equality;
- reporting indexed zeros without an independent evaluation check;
- confusing a sign-change bracket with a complete zero count;
- increasing the sample size without increasing precision;
- selecting only attractive index windows;
- inferring an asymptotic conclusion from wall-clock scaling;
- omitting failed or contradictory runs.

## Language standard

Prefer:

> The first 100 indexed zeros returned residuals below the stated tolerance at 60 decimal digits.

Do not write:

> The Riemann Hypothesis was verified.

The second sentence suppresses the finite range and falsely suggests a proof.

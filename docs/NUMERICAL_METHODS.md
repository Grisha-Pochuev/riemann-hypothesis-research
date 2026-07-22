# Numerical Methods

## Arithmetic

All baseline calculations use arbitrary-precision arithmetic from `mpmath`. The `dps` parameter controls decimal working precision. Reported residuals should be interpreted relative to that precision and recomputed at a higher setting before being treated as stable.

## Indexed zeros

`mpmath.zetazero(n)` supplies an approximation to the `n`-th zero on the critical line. The repository does not accept that value without further checks. It evaluates `zeta(s)` at the returned point and records both the residual and the distance of the real part from `1/2`.

This is still a numerical check, not an exact certificate that the zero is simple, correctly indexed, or part of a complete interval verification.

## Hardy Z function

For real `t`, the baseline computes

\[
Z(t)=e^{i\theta(t)}\zeta\left(\frac12+it\right),
\]

where `theta(t)` is the Riemann--Siegel theta function. Up to numerical error, `Z(t)` is real and has the same critical-line zeros as the zeta function.

A sign change brackets a zero of odd multiplicity. Absence of a sign change does not prove absence of a zero.

## Normalized gaps

For consecutive ordinates `gamma_n < gamma_{n+1}`, the baseline uses

\[
(\gamma_{n+1}-\gamma_n)\frac{\log(\gamma_n/2\pi)}{2\pi}.
\]

This rescales the raw gap by the local average density. Comparisons must identify the sampled index window because finite-height effects are substantial.

## Zero-counting main term

The baseline uses

\[
\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+\frac78.
\]

It is only the smooth main component of the full counting relation. The difference from the observed count must not be called an implementation error without accounting for lower-order and oscillatory terms.

## Validation strategy

A numerical change should pass three levels:

1. unit tests at moderate precision;
2. recomputation at increased precision;
3. comparison through an independent identity or method when available.

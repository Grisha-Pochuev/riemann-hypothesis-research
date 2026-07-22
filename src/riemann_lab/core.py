from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from mpmath import mp


@dataclass(frozen=True)
class ZeroRecord:
    """A numerical record for one indexed nontrivial zero."""

    index: int
    real: mp.mpf
    imaginary: mp.mpf
    residual: mp.mpf
    critical_line_error: mp.mpf

    def as_dict(self, digits: int = 25) -> dict[str, object]:
        return {
            "index": self.index,
            "real": mp.nstr(self.real, digits),
            "imaginary": mp.nstr(self.imaginary, digits),
            "zeta_residual": mp.nstr(self.residual, digits),
            "critical_line_error": mp.nstr(self.critical_line_error, digits),
        }


def hardy_theta(t: float | mp.mpf) -> mp.mpf:
    """Return the Riemann--Siegel theta function for real t."""

    t = mp.mpf(t)
    return mp.im(mp.loggamma(mp.mpf("0.25") + mp.j * t / 2)) - t * mp.log(mp.pi) / 2


def hardy_z(t: float | mp.mpf) -> mp.mpf:
    """Return Hardy's real-valued Z(t) on the critical line."""

    t = mp.mpf(t)
    value = mp.exp(mp.j * hardy_theta(t)) * mp.zeta(mp.mpf("0.5") + mp.j * t)
    return mp.re(value)


def indexed_zero(index: int, *, dps: int = 50) -> ZeroRecord:
    """Retrieve and independently check the indexed critical-line zero."""

    if index < 1:
        raise ValueError("index must be positive")
    if dps < 20:
        raise ValueError("dps must be at least 20")

    with mp.workdps(dps):
        zero = mp.zetazero(index)
        residual = abs(mp.zeta(zero))
        line_error = abs(mp.re(zero) - mp.mpf("0.5"))
        return ZeroRecord(
            index=index,
            real=+mp.re(zero),
            imaginary=+mp.im(zero),
            residual=+residual,
            critical_line_error=+line_error,
        )


def verify_indexed_zeros(indices: Iterable[int], *, dps: int = 50) -> list[ZeroRecord]:
    """Return verification records for a sequence of positive indices."""

    return [indexed_zero(index, dps=dps) for index in indices]


def normalized_gap(gamma_left: float | mp.mpf, gamma_right: float | mp.mpf) -> mp.mpf:
    """Normalize a consecutive zero gap by the local mean spacing."""

    left = mp.mpf(gamma_left)
    right = mp.mpf(gamma_right)
    if left <= 2 * mp.pi:
        raise ValueError("gamma_left must exceed 2*pi")
    if right <= left:
        raise ValueError("gamma_right must exceed gamma_left")
    return (right - left) * mp.log(left / (2 * mp.pi)) / (2 * mp.pi)


def zero_counting_main_term(t: float | mp.mpf) -> mp.mpf:
    """Return the main Riemann--von Mangoldt approximation to N(T)."""

    t = mp.mpf(t)
    if t <= 0:
        raise ValueError("t must be positive")
    return t / (2 * mp.pi) * mp.log(t / (2 * mp.pi)) - t / (2 * mp.pi) + mp.mpf(7) / 8


def completed_zeta_symmetry_residual(s: complex | mp.mpc) -> mp.mpf:
    """Measure the functional-equation residual for the completed zeta function.

    The completed function xi(s) should satisfy xi(s) = xi(1-s).
    """

    s = mp.mpc(s)

    def xi(z: mp.mpc) -> mp.mpc:
        return z * (z - 1) * mp.power(mp.pi, -z / 2) * mp.gamma(z / 2) * mp.zeta(z) / 2

    return abs(xi(s) - xi(1 - s))

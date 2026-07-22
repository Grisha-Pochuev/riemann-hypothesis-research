from mpmath import mp
import pytest

from riemann_lab import (
    completed_zeta_symmetry_residual,
    hardy_z,
    indexed_zero,
    normalized_gap,
    zero_counting_main_term,
)


def test_first_zero_has_small_residual_and_is_on_critical_line() -> None:
    record = indexed_zero(1, dps=50)
    with mp.workdps(50):
        expected = mp.mpf("14.134725141734693790457251983562470270784257115699")
        assert abs(record.imaginary - expected) < mp.mpf("1e-45")
        assert record.residual < mp.mpf("1e-45")
        assert record.critical_line_error < mp.mpf("1e-45")


def test_hardy_z_is_nearly_zero_at_first_ordinate() -> None:
    record = indexed_zero(1, dps=50)
    with mp.workdps(50):
        assert abs(hardy_z(record.imaginary)) < mp.mpf("1e-45")


def test_normalized_gap_is_positive() -> None:
    first = indexed_zero(1, dps=40).imaginary
    second = indexed_zero(2, dps=40).imaginary
    assert normalized_gap(first, second) > 0


def test_zero_counting_main_term_is_reasonable_near_tenth_zero() -> None:
    tenth = indexed_zero(10, dps=40).imaginary
    estimate = zero_counting_main_term(tenth)
    assert 8 < estimate < 12


def test_completed_zeta_function_respects_symmetry_numerically() -> None:
    with mp.workdps(50):
        assert completed_zeta_symmetry_residual(mp.mpc("0.37", "19.25")) < mp.mpf("1e-45")


def test_invalid_inputs_are_rejected() -> None:
    with pytest.raises(ValueError):
        indexed_zero(0)
    with pytest.raises(ValueError):
        normalized_gap(20, 19)
    with pytest.raises(ValueError):
        zero_counting_main_term(0)

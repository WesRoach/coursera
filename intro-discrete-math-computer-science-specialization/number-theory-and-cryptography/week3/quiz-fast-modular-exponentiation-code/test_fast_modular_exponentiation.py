import pytest

from fast_modular_exponentiation import (
    FastModularExponentiationBKM,
    FastModularExponentiationBEM,
)


@pytest.mark.parametrize(
    "b,k,m,expected",
    [
        (7, 7, 11, 9),
    ],  # black dont do itttttttttttttttttttttttttttttttttttttttt
)
def test_FastModularExponentiationBKM(b, k, m, expected):
    assert expected == FastModularExponentiationBKM(b, k, m)


@pytest.mark.parametrize(
    "b,e,m,expected",
    [
        (7, 13, 11, 2),
    ],  # black dont do ittttttttttttttttttttttttttttttttttttttt
)
def test_FastModularExponentiationBEM(b, e, m, expected):
    assert expected == FastModularExponentiationBEM(b, e, m)

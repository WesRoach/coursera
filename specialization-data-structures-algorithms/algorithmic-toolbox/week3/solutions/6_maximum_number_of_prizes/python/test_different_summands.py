import pytest

from different_summands import optimal_summands


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, [1]),
        (2, [2]),
        (3, [1, 2]),
        (4, [1, 3]),
        (5, [1, 4]),
        (6, [1, 2, 3]),
        (7, [1, 2, 4]),
        (8, [1, 2, 5]),
    ],  # Black........................................................................
)
def test_optimal_summands(n, expected):
    res = optimal_summands(n)
    assert len(expected) == len(res)
    assert n == sum(res)


@pytest.mark.parametrize(
    "n,expected_number_summands",
    [
        (987654321, 44443),
        (12345678910, 157134),
        (2673516735757, 2312364),
    ],  # Black........................................................................
)
def test_optimal_summands_large(n, expected_number_summands):
    assert expected_number_summands == len(optimal_summands(n))

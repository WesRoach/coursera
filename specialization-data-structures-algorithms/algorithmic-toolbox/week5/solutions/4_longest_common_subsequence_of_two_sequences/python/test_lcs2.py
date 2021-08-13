import pytest

from lcs2 import lcs2


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ([2, 7, 5], [2, 5], 2),
        ([7], [1, 2, 3, 4], 0),
        ([2, 7, 8, 3], [5, 2, 8, 7], 2),
    ],
)
def test_optimal_sequence(a, b, expected):
    res = lcs2(a, b)
    assert expected == res

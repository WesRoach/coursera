import pytest

from lcs3 import lcs3


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        ([1, 2, 3], [2, 1, 3], [1, 3, 5], 2),
        ([8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7], [6, 8, 3, 1, 4, 7], 3),
    ],
)
def test_optimal_sequence(a, b, c, expected):
    res = lcs3(a, b, c)
    assert expected == res

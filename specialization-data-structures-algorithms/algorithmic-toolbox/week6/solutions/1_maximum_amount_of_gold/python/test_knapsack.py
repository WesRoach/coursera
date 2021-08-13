import pytest

from knapsack import optimal_weight


@pytest.mark.parametrize(
    "W,w,expected",
    [
        (10, [1, 4, 8], 9),
    ],
)
def test_optimal_weight(W, w, expected):
    res = optimal_weight(W, w)
    assert expected == res

import pytest

from majority_element import get_majority_element


@pytest.mark.parametrize(
    "a,expected",
    [
        ([2, 3, 9, 2, 2], 1),
        ([1, 2, 3, 4], 0),
        ([1, 2, 3, 1], 0),
    ],  # black formatting ..........................
)
def test_get_majority_element(a, expected):
    assert expected == get_majority_element(a)

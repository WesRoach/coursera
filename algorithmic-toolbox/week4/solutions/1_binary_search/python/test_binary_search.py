import pytest

from binary_search import binary_search, linear_search


@pytest.mark.parametrize(
    "a,key,expected",
    [
        ([1, 5, 8, 12, 13], 8, 2),
        ([1, 5, 8, 12, 13], 1, 0),
        ([1, 5, 8, 12, 13], 23, -1),
        ([1, 5, 8, 12, 13], 11, -1),
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 2, 1),
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5], 4, 3),
        ([1, 2, 3, 4, 5], 5, 4),
    ],
)
def test_binary_search(a, key, expected):
    # assert expected == linear_search(a, key)
    # assert linear_search(a, key) == binary_search(a,key)
    assert expected == binary_search(a, key)

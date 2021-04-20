import pytest

from partition3 import partition3


@pytest.mark.parametrize(
    "A,expected",
    [
        ([3, 3, 3, 3], 0),
        ([40], 0),
        ([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59], 1),
        ([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25], 1),
    ],
)
def test_partition3(A, expected):
    res = partition3(A)
    assert expected == res

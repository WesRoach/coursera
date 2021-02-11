import pytest

from sorting import partition3, randomized_quick_sort


@pytest.mark.parametrize(
    "a,a_prime,expected",
    [
        ([2, 1, 3, 2, 1], [1, 1, 2, 2, 3], (2, 3))
    ],  # black ......................................................
)
def test_partition3(a, a_prime, expected):
    assert expected == partition3(a, 0, len(a) - 1)
    assert a_prime == a


@pytest.mark.parametrize(
    "a,expected",
    [
        ([2, 3, 9, 2, 2], [2, 2, 2, 3, 9]),
    ],  # black formatting ..........................
)
def test_randomized_quick_sort(a, expected):
    randomized_quick_sort(a, 0, len(a) - 1)
    assert expected == a

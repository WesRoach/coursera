import random

import pytest

from merge_sort import _merge, merge_sort


@pytest.mark.parametrize(
    "array",
    [
        ([2, 1]),
        ([4, 3, 2, 1]),
    ],  # black ...................................................................
)
def test_merge_sort(array):
    expected = sorted(array)
    merge_sort(array)
    assert expected == array


def test_merge_sort_generate():
    for test in range(0, 100):
        array = [random.randint(0, 20) for x in range(0, 100)]
        expected = sorted(array)
        merge_sort(array)
        assert expected == array

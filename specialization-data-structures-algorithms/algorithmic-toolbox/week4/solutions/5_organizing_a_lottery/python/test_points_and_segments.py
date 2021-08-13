import pytest

from points_and_segments import (
    naive_count_segments,
    fast_count_segments,
)


@pytest.mark.parametrize(
    "segments,points,expected",
    [
        ([(0, 5), (7, 10)], [1, 6, 11], [1, 0, 0]),
        ([(-10, 10),], [-100, 100, 0], [0, 0, 1]),
        ([(0, 5), (-3, 2), (7, 10)], [1, 6], [2, 0]),
    ],  # black ......................................................
)
def test_naive_count_segments(segments, points, expected):
    starts = [x for x, y in segments]
    ends = [y for x, y in segments]
    assert expected == naive_count_segments(starts, ends, points)


@pytest.mark.parametrize(
    "segments,points,expected",
    [
        ([(0, 5), (7, 10)], [1, 6, 11], [1, 0, 0]),
        ([(-10, 10),], [-100, 100, 0], [0, 0, 1]),
        ([(0, 5), (-3, 2), (7, 10)], [1, 6], [2, 0]),
    ],  # black ......................................................
)
def test_fast_count_segments(segments, points, expected):
    assert expected == fast_count_segments(segments, points)

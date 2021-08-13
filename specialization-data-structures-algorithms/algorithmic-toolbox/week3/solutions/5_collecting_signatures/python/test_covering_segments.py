import pytest

from covering_segments import optimal_points, Segment


@pytest.mark.parametrize(
    "data,expected",
    [
        ([[1, 3], [2, 5], [3, 6]], [3]),
        ([[4, 7], [1, 3], [2, 5], [5, 6]], [3, 6]),
        ([[1, 3]], [3]),
        ([[1, 5], [2, 3]], [3]),
        ([[1, 5], [2, 3], [4, 6]], [3, 6]),
    ],  # Black........................................................................
)
def test_optimal_points(data, expected):
    segments = [Segment(x, y) for x, y in data]
    assert expected == optimal_points(segments)

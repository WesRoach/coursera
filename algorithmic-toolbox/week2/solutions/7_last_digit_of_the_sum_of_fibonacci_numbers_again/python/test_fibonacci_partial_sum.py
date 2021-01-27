import pytest

from fibonacci_partial_sum import fibonacci_partial_sum


@pytest.mark.parametrize(
    "start,end,expected",
    [
        (3, 7, 1),
        (10, 10, 5),
        (10, 200, 2),
        (1, 2, 2),
        (1, 10000000000, None)
        # Black ..........
    ],
)
def test_fibonacci_partial_sum(start, end, expected):
    if expected is not None:
        assert expected == fibonacci_partial_sum(start, end)

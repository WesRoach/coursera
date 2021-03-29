import pytest

from edit_distance import edit_distance


@pytest.mark.parametrize(
    "s,t,expected",
    [
        ("ab", "ab", 0),
        ("short", "ports", 3),
        ("editing", "distance", 5),
    ],
)
def test_optimal_sequence(s, t, expected):
    res = edit_distance(s, t)
    assert expected == res

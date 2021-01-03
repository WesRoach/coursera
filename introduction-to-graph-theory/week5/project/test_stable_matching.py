import pytest

from stable_matching import stableMatching


@pytest.mark.parametrize(
    "n,menPreferences,womenPreferences,expected",
    [
        (1, [[0]], [[0]], [0]),  # stop black from formatting
        (2, [[0, 1], [1, 0]], [[0, 1], [1, 0]], [0, 1]),
        (
            3,
            [[1, 0, 2], [0, 1, 2], [1, 2, 0]],
            [[2, 0, 1], [1, 2, 0], [0, 1, 2]],
            [0, 1, 2],
        ),
        (
            3,
            [[0, 1, 2], [1, 2, 0], [0, 1, 2]],
            [[1, 0, 2], [2, 0, 1], [0, 1, 2]],
            [0, 2, 1],
        ),
    ],
)
def test_stableMatching(n, menPreferences, womenPreferences, expected):
    assert expected == stableMatching(n, menPreferences, womenPreferences)

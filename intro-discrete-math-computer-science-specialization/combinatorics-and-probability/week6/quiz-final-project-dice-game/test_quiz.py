import pytest
from quiz import count_wins, find_the_best_dice, compute_strategy


@pytest.mark.parametrize(
    "dice1,dice2,expected",
    [
        ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], (15, 15)),
        ([1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9], (16, 20)),
    ],
)
def test_count_wins(dice1, dice2, expected):
    assert expected == count_wins(dice1, dice2)


@pytest.mark.parametrize(
    "dices,expected",
    [
        ([[1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9], [3, 3, 5, 5, 7, 7]], -1),
        ([[1, 1, 2, 4, 5, 7], [1, 2, 2, 3, 4, 7], [1, 2, 3, 4, 5, 6]], 2),
        (
            [
                [3, 3, 3, 3, 3, 3],
                [6, 6, 2, 2, 2, 2],
                [4, 4, 4, 4, 0, 0],
                [5, 5, 5, 1, 1, 1],
            ],
            -1,
        ),
    ],
)
def test_find_the_best_dice(dices, expected):
    assert expected == find_the_best_dice(dices)


@pytest.mark.parametrize(
    "dices,expected",
    [
        (
            [[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]],
            {"choose_first": False, 0: 1, 1: 2, 2: 0},
        ),
        (
            [
                [4, 4, 4, 4, 0, 0],
                [7, 7, 3, 3, 3, 3],
                [6, 6, 2, 2, 2, 2],
                [5, 5, 5, 1, 1, 1],
            ],
            {"choose_first": True, "first_dice": 1},
        ),
    ],
)
def test_compute_strategy(dices, expected):
    assert expected == compute_strategy(dices)

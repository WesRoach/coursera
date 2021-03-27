import pytest

from primitive_calculator import optimal_sequence


@pytest.mark.parametrize(
    "m,operations,sequence",
    [
        (1, 0, {(1,)}),
        (5, 3, {(1, 2, 4, 5), (1, 3, 4, 5)}),
        (
            96234,
            14,
            {
                (
                    1,
                    3,
                    9,
                    10,
                    11,
                    22,
                    66,
                    198,
                    594,
                    1782,
                    5346,
                    16038,
                    16039,
                    32078,
                    96234,
                ),
                (
                    1,
                    3,
                    9,
                    10,
                    11,
                    33,
                    99,
                    297,
                    891,
                    2673,
                    8019,
                    16038,
                    16039,
                    48117,
                    96234,
                ),
            },
        ),
    ],  # black ........................................................
)
def test_optimal_sequence(m, operations: int, sequence: set):
    res_operations, res_sequence = optimal_sequence(m)
    assert res_operations == operations
    assert res_sequence in sequence

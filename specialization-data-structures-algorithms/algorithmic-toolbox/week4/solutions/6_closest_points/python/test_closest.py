import random
import pytest

from closest import (
    euclidean_distance,
    _min_distance,
    minimum_distance,
    brute_minimum_distance,
)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ((0, 0), (1, 1), 1.4142135623730951),
        ((0, 0), (3, 4), 5.0),
    ],  # black .....................................................
)
def test_euclidean_distance(a, b, expected):
    assert expected == euclidean_distance(a, b)


test_cases = [
    ([(0, 0), (3, 4)], 5.0),
    ([(7, 7), (1, 100), (4, 8), (7, 7)], 0.0),
    (
        [
            (4, 4),
            (-2, -2),
            (-3, -4),
            (-1, 3),
            (2, 3),
            (-4, 0),
            (1, 1),
            (-1, -1),
            (3, -1),
            (-4, 2),
            (-2, 4),
        ],
        1.414213,
    ),
    ([(0, 2), (0, 1), (0, 1), (2, 2)], 0.0),
]


@pytest.mark.parametrize(
    "coordinates,expected", test_cases,
)
def test_minimum_distance(coordinates, expected):
    assert expected == pytest.approx(minimum_distance(coordinates), 0.001)


@pytest.mark.parametrize(
    "coordinates,expected", test_cases,
)
def test_brute_minimum_distance(coordinates, expected):
    assert expected == pytest.approx(brute_minimum_distance(coordinates), 0.001)


@pytest.mark.skip(reason="Intentionally loops infinitely.")
def test_via_random_generation():
    """This will run until ctrl-c is passed or a test fails.
    """
    COORDINATE_MAX = 20
    while True:
        coordinates = [
            (random.randint(0, COORDINATE_MAX), random.randint(0, COORDINATE_MAX))
            for x in range(0, 100)
        ]
        print(coordinates)
        assert brute_minimum_distance(coordinates) == pytest.approx(
            minimum_distance(coordinates), 0.001
        )

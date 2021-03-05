import pytest

from change_dp import get_change


@pytest.mark.parametrize(
    "m,expected",
    [
        (2, 2),
        (34, 9),
    ],  # black ........................................................
)
def test_get_change(m, expected):
    assert expected == get_change(m)

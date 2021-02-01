import pytest

from largest_number import largest_number


@pytest.mark.parametrize(
    "n,expected",
    [
        (["21", "2"], "221"),
        (["9", "4", "6", "1", "9"], "99641"),
        (["23", "39", "92"], "923923"),
    ],  # Black........................................................................
)
def test_largest_number(n, expected):
    expected = largest_number(n)

import pytest

from diophantine_equations import diophantine


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (10, 6, 14, (-7, 14)),  # avoid black formatting here
        (391, 299, -69, (9, -12)),
        (3, 6, 18, (6, 0)),
    ],
)
def test_diophantine(a, b, c, expected):
    assert expected == diophantine(a, b, c)


# diophantine(3, 6, 18)
# gcd(3, 6)
# div = 18 / 3
# div = 6
# x = 6 * 1
# x = 6
# y = 6 * 0
# y = 0

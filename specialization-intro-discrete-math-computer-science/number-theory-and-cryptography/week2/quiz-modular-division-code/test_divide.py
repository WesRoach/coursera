import pytest

from divide import divide


@pytest.mark.parametrize(
    "a,b,n,expected", [(7, 2, 9, 8)],
)
def test_divide(a, b, n, expected):
    assert expected == divide(a, b, n)

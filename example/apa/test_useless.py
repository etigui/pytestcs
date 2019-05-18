import useless
import pytest

@pytest.mark.parametrize("a, b, expected", [(1, 2 , 3), (1, 3, 4), (1, 4, 5)])
def test_mod(a, b, expected):
	assert useless.add(a, b) == expected, "Add 2 number from list"


@pytest.mark.parametrize("a, b ,expected",[(3,3, True),(3,3, True), (6,7, False), pytest.param(4,5, True, marks=pytest.mark.xfail)])
def test_eq(a,b, expected):
	assert useless.eq(a,b) == expected, "Compare 2 number from list"

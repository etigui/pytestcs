import useless
import pytest


def test_multilpy():
	assert useless.multilpy(3, 2) == 6

@pytest.mark.skip()
def test_add():
	assert useless.add(3, 2) == 5

@pytest.mark.xpass()
def test_sub():
	assert useless.sub(3, 2) == 1

@pytest.mark.xfail(reason="always xfail")
def test_div():
	assert useless.div(4, 2) == 2.0, "value was odd, should be even"


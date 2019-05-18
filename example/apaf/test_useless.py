import pytest
import useless

def test_add(a, b, expected):
    assert useless.add(int(a), int(b)) == int(expected), "Add 2 number from list"

import pytest

def pytest_addoption(parser):
    parser.addoption("--file", action="store", default="test.txt", help="Add input value from file")

def pytest_generate_tests(metafunc):
    fileName = metafunc.config.getoption("--file")
    if "a" in metafunc.fixturenames and "b" in metafunc.fixturenames and "expected" in metafunc.fixturenames:

        with open(fileName) as f:
            content = f.readlines()

        content = [x.strip().split() for x in content]
        metafunc.parametrize("a, b, expected", content)

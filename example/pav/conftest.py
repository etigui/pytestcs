import pytest

def pytest_addoption(parser):
    parser.addoption("--const", action="store", default="0", help="Add const result as arg")

@pytest.fixture
def const(request):
    return request.config.getoption("--const")
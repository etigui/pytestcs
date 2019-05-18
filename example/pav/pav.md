Pass arguments value to test function

## Run

    py.test -ra -v --const=0
    py.test -ra -v --junitxml results.xml --const=0

## Files

```python
# file: useless.py

def multilpy(a,b):
	return a * b
```

```python
# file: test_useless.py

import pytest
import useless

def test_multiply(const):
    assert useless.multilpy(1, 0) == int(const), "Multiply 2 number"
```

```python
# file: conftest.py

import pytest

def pytest_addoption(parser):
    parser.addoption("--const", action="store", default="0", help="Add const as arg")

@pytest.fixture
def const(request):
    return request.config.getoption("--const")
```


## Output

    PS C:\Users\Admin\Documents\GitHub\pytestcs\example\pav> py.test -ra -v --const=0
    ============================================================================================================================================ test session starts =============================================================================================================================================
    platform win32 -- Python 3.7.2, pytest-4.5.0, py-1.8.0, pluggy-0.11.0 -- c:\users\admin\appdata\local\programs\python\python37-32\python.exe
    cachedir: .pytest_cache
    rootdir: C:\Users\Admin\Documents\GitHub\pytestcs\example\pav
    collected 1 item                                                                                                                                                                                                                                                                                              

    test_useless.py::test_multiply PASSED                                                                                                                                                                                                                                                                   [100%]

    ========================================================================================================================================== 1 passed in 0.06 seconds ==========================================================================================================================================

## Ref
- [Basic patterns and examples](https://docs.pytest.org/en/latest/example/simple.html#pass-different-values-to-a-test-function-depending-on-command-line-options)
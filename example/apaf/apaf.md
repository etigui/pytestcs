Add multiple value from file to test function

## Run

    py.test -ra -v --file=test.txt
    py.test -ra -v --junitxml results.xml --file=test.txt

## Files

```python
# file: useless.py

def add(a,b):
	return a + b
```

```python
# file: test_useless.py

import pytest
import useless

def test_add(a, b, expected):
    assert useless.add(int(a), int(b)) == int(expected), "Add 2 number from list"
```

```python
# file: conftest.py

import pytest

def pytest_addoption(parser):
    parser.addoption("--file", action="store", default="test.txt", help="Add input value from file")

def pytest_generate_tests(metafunc):
    fileName = metafunc.config.getoption("--file")
    if "a" in metafunc.fixturenames and "b" in metafunc.fixturenames and "expected" in metafunc.fixturenames:

        with open(fileName) as f:
            content = f.readlines()
        metafunc.parametrize("a, b, expected", [x.strip().split() for x in content])
```

```python
# file: test.txt

1 1 2
2 2 4
3 3 6
4 4 8
5 5 10
6 6 12
```

# Output

    ========================================================================================================================================== 6 passed in 0.06 seconds ==========================================================================================================================================
    PS C:\Users\Admin\Documents\GitHub\pytestcs\example\apaf> py.test -ra -v --file=test.txt
    ============================================================================================================================================ test session starts =============================================================================================================================================
    platform win32 -- Python 3.7.2, pytest-4.5.0, py-1.8.0, pluggy-0.11.0 -- c:\users\admin\appdata\local\programs\python\python37-32\python.exe
    cachedir: .pytest_cache
    rootdir: C:\Users\Admin\Documents\GitHub\pytestcs\example\apaf
    collected 6 items                                                                                                                                                                                                                                                                                             

    test_useless.py::test_add[1-1-2] PASSED                                                                                                                                                                                                                                                                 [ 16%]
    test_useless.py::test_add[2-2-4] PASSED                                                                                                                                                                                                                                                                 [ 33%]
    test_useless.py::test_add[3-3-6] PASSED                                                                                                                                                                                                                                                                 [ 50%]
    test_useless.py::test_add[4-4-8] PASSED                                                                                                                                                                                                                                                                 [ 66%]
    test_useless.py::test_add[5-5-10] PASSED                                                                                                                                                                                                                                                                [ 83%]
    test_useless.py::test_add[6-6-12] PASSED                                                                                                                                                                                                                                                                [100%]

    ========================================================================================================================================== 6 passed in 0.08 seconds ==========================================================================================================================================

## Ref

-[Parameterize tests using excel in Pytest](https://stackoverflow.com/questions/51950921/parameterize-tests-using-excel-in-pytest)
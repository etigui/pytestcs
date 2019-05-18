Add multimple value to test function


## Run

	py.test -ra -v
	py.test -ra -v --junitxml results.xml

## Files

```python
# file: useless.py

def add(a,b):
	return a + b

def eq(a, b):
	if a == b:
		return True
	return False
```

```python
# file: test_useless.py

import useless
import pytest

@pytest.mark.parametrize("a, b, expected", [(1, 2 , 3), (1, 3, 4), (1, 4, 5)])
def test_mod(a, b, expected):
	assert useless.add(a, b) == expected, "Add 2 number from list"


@pytest.mark.parametrize("a, b ,expected",[(3,3, True),(3,3, True), (6,7, False), pytest.param(4,5, True, marks=pytest.mark.xfail)])
def test_eq(a,b, expected):
	assert useless.eq(a,b) == expected, "Compare 2 number from list"
```


## Output

    ==================================================================================================================================== 6 passed, 1 xfailed in 0.10 seconds =====================================================================================================================================
    PS C:\Users\Admin\Documents\GitHub\pytestcs\example\apa> py.test -ra -v
    ============================================================================================================================================ test session starts =============================================================================================================================================
    platform win32 -- Python 3.7.2, pytest-4.5.0, py-1.8.0, pluggy-0.11.0 -- c:\users\admin\appdata\local\programs\python\python37-32\python.exe
    cachedir: .pytest_cache
    rootdir: C:\Users\Admin\Documents\GitHub\pytestcs\example\apa
    collected 7 items                                                                                                                                                                                                                                                                                             

    test_useless.py::test_mod[1-2-3] PASSED                                                                                                                                                                                                                                                                 [ 14%]
    test_useless.py::test_mod[1-3-4] PASSED                                                                                                                                                                                                                                                                 [ 28%]
    test_useless.py::test_mod[1-4-5] PASSED                                                                                                                                                                                                                                                                 [ 42%]
    test_useless.py::test_eq[3-3-True0] PASSED                                                                                                                                                                                                                                                              [ 57%]
    test_useless.py::test_eq[3-3-True1] PASSED                                                                                                                                                                                                                                                              [ 71%]
    test_useless.py::test_eq[6-7-False] PASSED                                                                                                                                                                                                                                                              [ 85%]
    test_useless.py::test_eq[4-5-True] XFAIL                                                                                                                                                                                                                                                                [100%]

    ========================================================================================================================================== short test summary info ===========================================================================================================================================
    XFAIL test_useless.py::test_eq[4-5-True]
    ==================================================================================================================================== 6 passed, 1 xfailed in 0.10 seconds =====================================================================================================================================
Mark test as skip, pass, fail, etc..

## Run

	py.test -ra -v
	py.test -ra -v --junitxml results.xml

## Files

```python
# file: useless.py

def multilpy(a,b):
	return a * b
	
def add(a,b):
	return a + b
	
def sub(a,b):
	return a - b
	
def div(a,b):
	return a / b

def mod(a, b):
	return a % b

def eq(a, b):
	if a == b:
		return True
	return False
```


```python
# file: test_useless.py

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
```

## Output

	PS C:\Users\Admin\Documents\GitHub\pytestcs\example\mark> py.test -ra -v
	============================================================================================================================================ test session starts =============================================================================================================================================
	platform win32 -- Python 3.7.2, pytest-4.5.0, py-1.8.0, pluggy-0.11.0 -- c:\users\admin\appdata\local\programs\python\python37-32\python.exe
	cachedir: .pytest_cache
	rootdir: C:\Users\Admin\Documents\GitHub\pytestcs\example\mark
	collected 4 items                                                                                                                                                                                                                                                                                             

	test_useless.py::test_multilpy PASSED                                                                                                                                                                                                                                                                   [ 25%]
	test_useless.py::test_add SKIPPED                                                                                                                                                                                                                                                                       [ 50%]
	test_useless.py::test_sub PASSED                                                                                                                                                                                                                                                                        [ 75%]
	test_useless.py::test_div XPASS                                                                                                                                                                                                                                                                         [100%]

	============================================================================================================================================== warnings summary ==============================================================================================================================================
	c:\users\admin\appdata\local\programs\python\python37-32\lib\site-packages\_pytest\mark\structures.py:324
	c:\users\admin\appdata\local\programs\python\python37-32\lib\site-packages\_pytest\mark\structures.py:324: PytestUnknownMarkWarning: Unknown pytest.mark.xpass - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
		PytestUnknownMarkWarning,

	-- Docs: https://docs.pytest.org/en/latest/warnings.html
	========================================================================================================================================== short test summary info ===========================================================================================================================================
	SKIPPED [1] test_useless.py:8: unconditional skip
	XPASS test_useless.py::test_div always xfail
	========================================================================================================================= 2 passed, 1 skipped, 1 xpassed, 1 warnings in 0.06 seconds =========================================================================================================================
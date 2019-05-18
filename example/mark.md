Mark test as skip, pass, fail, etc..

## Run



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

@pytest.fixture
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
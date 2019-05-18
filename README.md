# Pytest cheat sheet

Pytest is a framework that makes building simple and scalable tests easy. Tests are expressive and readable-no boilerplate code required. Get started in minutes with a small unit test or complex functional test for your application or library.

## Install

	pip install pytest
	
## Exemple

In these exemple I will mostly use 3 file :
- `useless.py` which is the code you want to test
- `test_useless.py` which is the test file you will run
- `conftest.py` which contain directory-specific hook implementations


*Exemple:*
1. [Mark test as skip, pass, fail, etc..]()
2. [Add particular arguments]()
3. [Add particular arguments from file]()


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
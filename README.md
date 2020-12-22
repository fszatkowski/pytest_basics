# pytest basics

## Setup
- install pytest
```shell script
pip install pytest pytest-cov
```
- setup pythonpath to use pytest from CLI
```shell script
export PYTHONPATH=2_pytest_syntax/src/main/python
```

## About
- unit test python framework
- cool CLI
- extensions
- well-maintained
- integrated into pycharm

## Test detections
- test function or method names should start with "test" 
- test functions or methods in different files can have the same names
- test files should start or end with "test"
- test files can be placed anywhere, but must have unique names

## Organizing projects
- best way is to separate code into src and tests directories (but it's no necessary)
- in tests root directory, create conftest.py - config file for pytest

## CLI
- `pytest` finds and runs all tests in the directory
- `pytest <directory>` executes subset of tests in given directory
- `pytest -k <keyword>` executes only tests including keyword (works on module, file and function level)
- `pytest -q` or `pytest -v` for quiet / verbose execution
- `pytest --cov` for code coverage report

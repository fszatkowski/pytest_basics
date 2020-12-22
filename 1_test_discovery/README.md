# Examples on how pytest detects tests
For details, check source files where tests are commented.

To run pytest in this directory:
```shell script
pytest -k 1_
``` 
If there are errors with imports, set up PYTHONPATH
```shell script
export PYTHONPATH=2_pytest_syntax/src/main/python
```
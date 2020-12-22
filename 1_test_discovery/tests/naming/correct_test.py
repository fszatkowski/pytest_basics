from naming.utils import fn_to_test

""" The import is resolved because conftest is present in tests directory
    pytest adds path to conftest directory to PYTHONPATH """


# detected
def test_detects_correct_name():
    assert True


# not run, becouse it doesn't start with 'test'
def incorrect_test():
    assert True


# detected
def test_utils_fn():
    assert fn_to_test() == 1


# detected - multiple test can have the same name if they are in different files
def test_wandering():
    assert True

import pytest
from human import Human

""" 
Notice how in 1_test we use John twice
This can be simplified with pytest fixtures
Fixtures can be declared in conftest to keep our test file clean
"""


@pytest.fixture(scope="session")
def john():
    # fixture annotation will initialize this object once for pytest session
    # if we want to create new object per module or per function, we need to change scope
    # if we want the fixture to run for all tests, set autouse=True
    yield Human("John", 2000)


def test_describes_correctly(john):
    # fixtures are accessed like a globals
    assert john.describe() == "John is 20 years old."


@pytest.mark.usefixtures("john")
def test_correctly_calculates_age(john):
    # Classes or functions can be annotated with usefixtures, but in this case it's just more typing
    assert john.age() == 20

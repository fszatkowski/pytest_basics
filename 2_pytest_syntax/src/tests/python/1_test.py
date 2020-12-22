import pytest
from human import Human

"""
Those are just basic tests for Human class
"""


def test_describes_correctly():
    john = Human("John", 2000)
    assert john.describe() == "John is 20 years old."


def test_cant_be_born_in_future():
    # to test exceptions, use pytest.raises with context manager
    with pytest.raises(ValueError) as e:
        Human("John", 2077)
    assert str(e.value) == "This is impossible"


@pytest.mark.parametrize("name,yob,expected", [("John", 2000, 20), ("Anna", 1995, 25)])
def test_correctly_calculates_age(name, yob, expected):
    # to run multiple tests with different values of arguments, use parametrized test
    assert Human(name, yob).age() == expected

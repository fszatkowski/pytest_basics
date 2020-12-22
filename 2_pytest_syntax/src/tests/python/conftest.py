import random

import pytest
from human import Human

"""
If we want to split conftest into different files, they can added as below:
pytest_plugins = [module.file]
"""


@pytest.fixture(scope="session")
def random_age_human():
    # This is factory fixture, it returns function that creates customized objects
    yob = random.randint(1900, 2020)

    def _human(name):
        return Human(name, yob)

    return _human

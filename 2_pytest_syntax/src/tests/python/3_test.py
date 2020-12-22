# All fixtures declared in conftest.py are available for tests
# Check how random_age_human fixture is defined in conftest


def test_random_age_factory(random_age_human):
    michael = random_age_human("Michael")
    assert michael.name == "Michael"
    assert 0 <= michael.age() <= 120

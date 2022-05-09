import pytest

# this is a fixture. !!When you include the fixture name in the parameter list of a test function, pytest knows to run it before running the test!!
@pytest.fixture()
def some_data():
    return 42

def test_some_data(some_data):
    assert some_data == 42
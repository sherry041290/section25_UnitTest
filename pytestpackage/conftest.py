import pytest


@pytest.fixture()
def setUp():
    print("--Before test: ")
    yield
    print("--After test! ")


@pytest.fixture(scope="module")
def oneTimeSetUp():
    print("-- Before test 1")
    yield
    print("--After test 1")

def browser():


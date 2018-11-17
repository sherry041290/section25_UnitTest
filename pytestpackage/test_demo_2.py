import pytest


@pytest.fixture()
def setUp():
    print(" - Run once before test 2")
    yield
    print("- Run after test done 2")


def test_demo2_methodA(setUp):
    print("Test demo2 method A")


def test_demo2_methodB(setUp):
    print("Test demo2 method B")

import pytest


@pytest.fixture()
def setUp():
    print(" -Print once before test")


def test_demo1_methodA(setUp):
    print("Test demo1 method A")


def test_demo1_methodB(setUp):
    print("Test demo1 method B")

import pytest


# B, A, D , C, F, E
@pytest.mark.run(order=2)
def test_method_A(setUp):
    print("--Test method A--")


@pytest.mark.run(order=1)
def test_method_B(setUp):
    print("--Test method B--")


@pytest.mark.run(order=4)
def test_method_C(setUp):
    print("--Test method C--")


@pytest.mark.run(order=3)
def test_method_D(setUp):
    print("--Test method D--")


@pytest.mark.run(order=6)
def test_method_E(setUp):
    print("--Test method E--")


@pytest.mark.run(order=5)
def test_method_F(setUp):
    print("--Test method F--")


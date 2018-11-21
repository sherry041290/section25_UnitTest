import pytest
from pytestpackage.class_to_test import SomeClassToTest


@pytest.mark.usefixtures("setUp", "oneTimeSetUp")
class TestClassDemo:

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.abc = SomeClassToTest(10)

    def test_method1(self):
        result = self.abc.Plus2Number(5, 9)
        assert result == 24
        print("Done test method 1")

    def test_method2(self):
        result = self.abc.Multi2Number(2, 5)
        assert result == 100
        print("Done test method 2")


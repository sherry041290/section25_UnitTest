import unittest


class DemoTestCase(unittest.TestCase):
    def setUp(self):
        print("Will run once every test")

    def test_method_1(self):
        print("Test method 1")

    def test_method_2(self):
        print("Test method 2")

    def tearDown(self):
        print("Always run after finish every test")


if __name__ == '__main__':
    unittest.main(verbosity=2)

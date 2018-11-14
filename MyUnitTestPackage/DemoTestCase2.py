import unittest


class DemoTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("--"*20)
        print("Will run only once before all test")
        print("**"*20)

    def setUp(self):
        print("Will run once before every test")

    def test_method_1(self):
        print("Test method 1")

    def test_method_2(self):
        print("Test method 2")

    def tearDown(self):
        print("Always run after finish every test")

    @classmethod
    def tearDownClass(cls):
        print("--"*20)
        print("Will run only once after all test")
        print("**"*20)


if __name__ == '__main__':
    unittest.main(verbosity=2)

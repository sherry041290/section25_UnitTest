import unittest


class DemoAssert(unittest.TestCase):
    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a,"a is not True")
        b = False
        self.assertFalse(b, " b is not False")

    def test_assertEqual(self):
        a = "Test"
        b = "Test"
        self.assertNotEqual(a, b, " a is equal b")


if __name__ == '__main__':
    unittest.main(verbosity=2)


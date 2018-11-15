import unittest
from MyUnitTestPackage.test_class1 import TestClass1
from MyUnitTestPackage.test_class2 import TestClass2

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestClass2)

test_suite = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner(verbosity=2).run(test_suite)

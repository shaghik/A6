import numpy as np
from Test import myCalculator as mt

class unitTest:
    def test_equal(str1, str2):
        np.testing.assert_string_equal(str1, str2)

    def test_num_equal(num1, num2):
        np.testing.assert_equal(num1, num2)

    def testAdd(num1, num2, expected):
        np.testing.assert_equal(mt.add(num1, num2), expected)

    def testAddFail(num1, num2, expected):
        np.testing.assert_equal(mt.failAdd(num1, num2), expected)
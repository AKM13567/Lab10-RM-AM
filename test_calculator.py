# https://github.com/AKM13567/Lab10-RM-AM.git
# Partner 1 - Aarya Maskara
# Partner 2 - Rutheshkhanna Manikandan

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(mul(2, 8), 16)

    def test_divide(self):
        self.assertEqual(div(10, 5), 2)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, -1)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(6, 8), 10)

    def test_sqrt(self):
        self.assertEqual(square_root(16), 4.0)

    def test_add(self):
        self.assertEqual(add(2,3), 5)

    def test_subtract(self):
        self.assertEqual(sub(8,2),6)

    def test_divide_by_zero(self):
        try:
            div(134, 0)  
            self.fail("ZeroDivisionError was not raised")  
        except ZeroDivisionError:
            pass

    def test_logarithm(self):
        self.assertEqual(logarithm(2,8),3.0)

    def test_log_invalid_base(self):
        try:
            logarithm(1, 5)
            self.fail("ValueError was not raised")
        except ValueError:
            pass

if __name__ == '__main__':
    unittest.main()
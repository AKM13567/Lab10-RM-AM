# https://github.com/AKM13567/Lab10-RM-AM.git
# Partner 1 - Aarya Maskara
# Partner 2 - Ruteshkhanna Manikhandhan

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(mul(2, 8), 16)

    def test_divide(self):
        self.assertEqual(div(5, 10), 2)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, -1)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(6, 8) 10)

    def test_sqrt(self):
        self.assertEqual(square_root(16), 4.0)

if __name__ == '__main__':
    unittest.main()
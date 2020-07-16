import unittest
from pymultiply import PyMultiplier
import numpy as np


class TestPyCalculate(unittest.TestCase):

    def test_multiply(self):
        test_multiplier = PyMultiplier(2.0)
        test_data = np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=np.double)

        result = test_multiplier.multiply(test_data)
        expected = np.array([2.0, 4.0, 6.0, 8.0, 10.0], dtype=np.double)

        self.assertIsInstance(expected, np.ndarray)
        self.assertTrue((result == expected).all())


if __name__ == '__main__':
    unittest.main()

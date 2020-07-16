import unittest
from pycalculate import py_multiply, py_divide
import numpy as np


class TestPyCalculate(unittest.TestCase):

    def setUp(self):
        self.test_array = np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=np.double)

    def test_multiply(self):
        result = py_multiply(self.test_array, 5.0)
        expected = np.array([5.0, 10.0, 15.0, 20.0, 25.0], dtype=np.double)

        self.assertIsInstance(expected, np.ndarray)
        self.assertTrue((result == expected).all())

    def test_divide(self):
        result = py_divide(self.test_array, 2.0)
        expected = np.array([0.5, 1.0, 1.5, 2.0, 2.5], dtype=np.double)

        self.assertIsInstance(expected, np.ndarray)
        self.assertTrue((result == expected).all())


if __name__ == '__main__':
    unittest.main()

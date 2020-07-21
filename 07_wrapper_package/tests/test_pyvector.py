import unittest
from pymath.pyvector import PyVector
import numpy as np


class TestPyVector(unittest.TestCase):

    def setUp(self):
        self.test_pyvector = PyVector(
            np.array([1.0, 3.0, 5.0, 7.0, 9.0], dtype=np.double)
        )

    def test_sum(self):
        result = self.test_pyvector.sum()
        expected = np.double(25.0)

        self.assertIsInstance(expected, np.double)
        self.assertEqual(result, expected)

    def test_get_length(self):
        result = self.test_pyvector.get_length()
        expected = 5

        self.assertIsInstance(expected, int)
        self.assertEqual(result, expected)

    def test_get_data(self):
        result = self.test_pyvector.get_data()
        expected = np.array([1.0, 3.0, 5.0, 7.0, 9.0], dtype=np.double)

        self.assertIsInstance(expected, np.ndarray)
        self.assertTrue((result == expected).all())

    def test_multiply(self):
        self.test_pyvector.multiply(2.0)

        result = self.test_pyvector.get_data()
        expected = np.array([2, 6, 10, 14, 18], dtype=np.double)

        self.assertIsInstance(expected, np.ndarray)
        self.assertTrue((result == expected).all())


if __name__ == '__main__':
    unittest.main()

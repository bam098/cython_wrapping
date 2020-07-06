import unittest
from pymath.pyvector import PyVector
import numpy as np


class TestKeypointFinder(unittest.TestCase):

    def setUp(self):
        self.test_pyvector = PyVector(
            np.array([1, 3, 5, 7, 9], dtype=np.double)
        )

    def test_sum(self):
        result = self.test_pyvector.sum()
        expected = 25.0

        self.assertEqual(result, expected)

    def test_get_length(self):
        result = self.test_pyvector.get_length()
        expected = 5

        self.assertEqual(result, expected)

    def test_get_data(self):
        result = self.test_pyvector.get_data()
        expected = np.array([1, 3, 5, 7, 9], dtype=np.double)

        self.assertTrue((result == expected).all())

    def test_multiply(self):
        result = self.test_pyvector.multiply(2.0)
        expected = np.array([2, 6, 10, 14, 18], dtype=np.double)


if __name__ == '__main__':
    unittest.main()

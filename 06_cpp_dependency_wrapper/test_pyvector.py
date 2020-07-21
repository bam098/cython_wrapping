import unittest
from pyvector import PyVector
import numpy as np


class TestPyCalculate(unittest.TestCase):

    def setUp(self):
        test_data = np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=np.double)
        self.test_pyvector = PyVector(test_data)

    def test_get_length(self):
        result = self.test_pyvector.get_length()
        expected = 5

        self.assertIsInstance(expected, int)
        self.assertEqual(result, expected)

    def test_get_data(self):
        result = self.test_pyvector.get_data()
        expected = np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=np.double)

        self.assertIsInstance(expected, np.ndarray)
        self.assertTrue((result == expected).all())

    def test_sum(self):
        result = self.test_pyvector.sum()
        expected = np.double(15.0)

        self.assertIsInstance(expected, np.double)
        self.assertEqual(result, expected)

    def test_multiply(self):
        other_array = np.array([6.0, 7.0, 8.0, 9.0, 10.0], dtype=np.double)

        result = self.test_pyvector.multiply(other_array)
        expected = np.double(130.0)

        self.assertIsInstance(expected, np.double)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

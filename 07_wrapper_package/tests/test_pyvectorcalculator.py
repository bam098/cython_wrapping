import unittest
from pymath.pyvectorcalculator import PyVectorCalculator
from pymath.pyvector import PyVector
import numpy as np


class TestPyVectorCalculator(unittest.TestCase):

    def setUp(self):
        test_pyvector1 = PyVector(
            np.array([1.0, 3.0, 5.0, 7.0, 9.0], dtype=np.double)
        )
        test_pyvector2 = PyVector(
            np.array([2.0, 4.0, 6.0, 8.0], dtype=np.double)
        )

        self.test_pyvectorcalculator = PyVectorCalculator(
            test_pyvector1, test_pyvector2
        )

    def test_sum(self):
        result = self.test_pyvectorcalculator.sum()
        expected = np.double(45.0)

        self.assertIsInstance(expected, np.double)
        self.assertTrue((result == expected).all())

    def test_get_vec1(self):
        result = self.test_pyvectorcalculator.get_vec1().get_data()
        expected = np.array([1.0, 3.0, 5.0, 7.0, 9.0], dtype=np.double)

        self.assertIsInstance(expected, np.ndarray)
        self.assertTrue((result == expected).all())

    def test_get_vec2(self):
        result = self.test_pyvectorcalculator.get_vec2().get_data()
        expected = np.array([2.0, 4.0, 6.0, 8.0], dtype=np.double)

        self.assertIsInstance(expected, np.ndarray)
        self.assertTrue((result == expected).all())

    def test_multiply(self):
        self.test_pyvectorcalculator.multiply(2.0)

        result_pyvector1 = self.test_pyvectorcalculator.get_vec1().get_data()
        result_pyvector2 = self.test_pyvectorcalculator.get_vec2().get_data()

        expected1 = np.array([2.0, 6.0, 10.0, 14.0, 18.0], dtype=np.double)
        expected2 = np.array([4.0, 8.0, 12.0, 16.0], dtype=np.double)

        self.assertIsInstance(expected1, np.ndarray)
        self.assertIsInstance(expected2, np.ndarray)
        self.assertTrue((result_pyvector1 == expected1).all())
        self.assertTrue((result_pyvector2 == expected2).all())


if __name__ == '__main__':
    unittest.main()

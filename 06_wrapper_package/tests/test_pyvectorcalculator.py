import unittest
from pymath.pyvectorcalculator import PyVectorCalculator
from pymath.pyvector import PyVector
import numpy as np


class TestPyVectorCalculator(unittest.TestCase):

    def setUp(self):
        test_pyvector1 = PyVector(np.array([1, 3, 5, 7, 9], dtype=np.double))
        test_pyvector2 = PyVector(np.array([2, 4, 6, 8], dtype=np.double))

        self.test_pyvectorcalculator = PyVectorCalculator(
            test_pyvector1, test_pyvector2
        )

    def test_sum(self):
        result = self.test_pyvectorcalculator.sum()
        expected = 45.0

    def test_get_vec1(self):
        result = self.test_pyvectorcalculator.get_vec1().get_data()
        expected = np.array([1, 3, 5, 7, 9], dtype=np.double)

        self.assertTrue((result == expected).all())

    def test_get_vec2(self):
        result = self.test_pyvectorcalculator.get_vec2().get_data()
        expected = np.array([2, 4, 6, 8], dtype=np.double)

        self.assertTrue((result == expected).all())

    def test_multiply(self):
        self.test_pyvectorcalculator.multiply(2.0)

        pyvec1 = self.test_pyvectorcalculator.get_vec1().get_data()
        pyvec2 = self.test_pyvectorcalculator.get_vec2().get_data()

        expected1 = np.array([2, 6, 10, 14, 18], dtype=np.double)
        expected2 = np.array([4, 8, 12, 16], dtype=np.double)

        self.test_pyvectorcalculator.multiply(0.5)

        self.assertTrue((pyvec1 == expected1).all())
        self.assertTrue((pyvec2 == expected2).all())


if __name__ == '__main__':
    unittest.main()

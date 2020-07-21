from pymath.pyvector import PyVector
import numpy as np


class PyVectorCalculator:
    def __init__(self, vec1: PyVector, vec2: PyVector) -> None:
        self._vec1 = vec1
        self._vec2 = vec2

    def sum(self) -> np.double:
        return self._vec1.sum() + self._vec2.sum()

    def multiply(self, multiplier: np.double) -> None:
        self._vec1.multiply(multiplier)
        self._vec2.multiply(multiplier)

    def get_vec1(self) -> PyVector:
        return self._vec1

    def get_vec2(self) -> PyVector:
        return self._vec2

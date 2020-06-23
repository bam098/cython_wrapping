# distutils: language = c++

import numpy as np

cdef extern from "calculate.hpp":
    void multiply(double* array, const double k, unsigned int n)

def py_multiply(array: np.ndarray, k: double) -> np.ndarray:
    if not array.flags['C_CONTIGUOUS']:
        array = np.ascontiguousarray(array)

    cdef double[::1] array_memview = array

    multiply(&array_memview[0], k, array_memview.shape[0])

    return array

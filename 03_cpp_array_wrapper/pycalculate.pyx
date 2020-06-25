import numpy as np

cdef extern from "calculate.hpp":
    void multiply(double* array, const unsigned int array_length, const double multiplier)

def py_multiply(array: np.ndarray[np.double], multiplier: np.double) -> np.ndarray[np.double]:
    if not array.flags['C_CONTIGUOUS']:
        array = np.ascontiguousarray(array)

    cdef double[::1] array_memview = array
    multiply(&array_memview[0], array_memview.shape[0], multiplier)

    return array

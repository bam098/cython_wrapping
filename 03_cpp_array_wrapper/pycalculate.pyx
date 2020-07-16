import numpy as np
from libcpp.vector cimport vector

cdef extern from "calculate.hpp":
    void multiply(double* array, const unsigned int array_length, const double multiplier)
    void divide(vector[double]& vec, const double divisor)

def py_multiply(array: np.ndarray[np.double], multiplier: np.double) -> np.ndarray[np.double]:
    if not array.flags['C_CONTIGUOUS']:
        array = np.ascontiguousarray(array)

    cdef double[::1] array_memview = array
    multiply(&array_memview[0], array_memview.shape[0], multiplier)

    return array

def py_divide(array: np.ndarray[np.double], divisor: np.double) -> np.ndarray[np.double]:
    if not array.flags['C_CONTIGUOUS']:
        array = np.ascontiguousarray(array)

    cdef double[::1] array_memview = array

    cdef vector[double] vec;
    vec.assign(&array_memview[0], &array_memview[0] + array_memview.shape[0])

    divide(vec, divisor)
    
    return np.asarray(vec, dtype=np.double)

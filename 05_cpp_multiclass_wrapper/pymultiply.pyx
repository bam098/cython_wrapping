from cython cimport view
import numpy as np

cdef extern from "Vector.hpp":
    cdef cppclass Vector:
        Vector() except +
        Vector(double*, unsigned int) except +
        double sum()
        unsigned int get_length();
        double* get_data()

cdef extern from "Multiplier.hpp":
    cdef cppclass Multiplier:
        Multiplier(double) except +
        Vector multiply(Vector&)

cdef class PyMultiplier:
    cdef Multiplier *thisptr

    def __cinit__(self, k: np.double) -> None:
        self.thisptr = new Multiplier(k)

    def __dealloc__(self) -> None:
        del self.thisptr

    def multiply(self, data: np.ndarray[np.double]) -> np.ndarray[np.double]:
        if not data.flags['C_CONTIGUOUS']:
            data = np.ascontiguousarray(data)

        cdef double[::1] data_memview = data
        cdef Vector in_vec = Vector(&data_memview[0], data_memview.shape[0])

        cdef Vector out_vec = self.thisptr.multiply(in_vec)
        result_len = out_vec.get_length()
        cdef double* result_data = out_vec.get_data()

        return np.asarray(<double[:result_len]>result_data)

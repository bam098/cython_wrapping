from cython cimport view
import numpy as np


cdef extern from "Vector.hpp":
    cdef cppclass Vector:
        Vector(double* array, unsigned int multiplier) except +
        double sum()
        unsigned int get_length();
        double* get_data()
        double multiply(double* other_array, const unsigned int other_array_length)


cdef class PyVector:
    cdef Vector *thisptr
    cdef double[::1] data_memview

    def __cinit__(self, data: np.ndarray[np.double]) -> None:
        if not data.flags['C_CONTIGUOUS']:
            data = np.ascontiguousarray(data)

        self.data_memview = np.array(data, copy=True)
        self.thisptr = new Vector(&self.data_memview[0], self.data_memview.shape[0])

    def __dealloc__(self) -> None:
        del self.thisptr

    def sum(self) -> np.double:
        return self.thisptr.sum()

    def get_length(self) -> int:
        return self.thisptr.get_length();

    def get_data(self) -> np.ndarray[np.double]:
        cdef double* c_data = self.thisptr.get_data(); 
        data = np.asarray(<double[:self.thisptr.get_length()]>c_data)
        return data;

    def multiply(self, other_array: np.array[np.double]) -> np.double:
        if not other_array.flags['C_CONTIGUOUS']:
            other_array = np.ascontiguousarray(other_array)

        cdef double[::1] array_memview = other_array

        return self.thisptr.multiply(&array_memview[0], array_memview.shape[0]) 

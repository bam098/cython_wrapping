from cython cimport view
import numpy as np

cdef extern from "Vector.hpp":
    cdef cppclass Vector:
        Vector(double*, unsigned int) except +
        double sum()
        unsigned int get_length();
        double* get_data()
        void multiply(const double)

cdef class PyVector:
    cdef Vector *thisptr

    def __cinit__(self, data):
        if not data.flags['C_CONTIGUOUS']:
            data = np.ascontiguousarray(data)

        cdef double[::1] data_memview = data
        self.thisptr = new Vector(&data_memview[0], data_memview.shape[0])

    def __dealloc__(self):
        del self.thisptr

    def sum(self):
        return self.thisptr.sum()

    def get_length(self):
        return self.thisptr.get_length();

    def get_data(self):
        cdef double* data = self.thisptr.get_data(); 
        data_array = np.asarray(<double[:self.thisptr.get_length()]>data)
        return data_array;

    def multiply(self, k):
        return self.thisptr.multiply(k) 

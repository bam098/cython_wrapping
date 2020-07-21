cdef extern from "Vector.hpp":
    cdef cppclass Vector:
        Vector(double* array, unsigned int multiplier) except +
        double sum()
        unsigned int get_length();
        double* get_data()
        void multiply(const double multiplier)
#ifndef VECTOR_HPP
#define VECTOR_HPP

class Vector {
    private:
        double* _data;
        unsigned int _length;

    public:
        Vector(double* array, unsigned int array_length);
        ~Vector();

        double sum();
        unsigned int get_length();
        double* get_data();
        double multiply(double* other_array, const unsigned int other_array_length);
};

#endif
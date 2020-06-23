#ifndef VECTOR_HPP
#define VECTOR_HPP

class Vector {
    private:
        double* _data;
        unsigned int _length;

    public:
        Vector(double* data, unsigned int length);
        ~Vector();

        double sum();
        unsigned int get_length();
        double* get_data();
        void multiply(const double k);
};

#endif
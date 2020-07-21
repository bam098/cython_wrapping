#include "Vector.hpp"

Vector::Vector(double* array, unsigned int array_length) {
    _data = array;
    _length = array_length;
}

Vector::~Vector() { } 

double Vector::sum() {
    double sum = 0.0;
    for (int i = 0; i < _length; ++i) {
        sum += _data[i];
    }

    return sum;
}

unsigned int Vector::get_length() {
    return _length;
}

double* Vector::get_data() {
    return _data;
}

void Vector::multiply(const double multiplier) {
    for (int i = 0; i < _length; ++i) {
        _data[i] *= multiplier;
    }
}
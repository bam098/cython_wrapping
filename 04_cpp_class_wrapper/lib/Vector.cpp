#include "Vector.hpp"

Vector::Vector(double* data, unsigned int length) {
    _data = data;
    _length = length;
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

void Vector::multiply(const double k) {
    for (int i = 0; i < _length; ++i) {
        _data[i] *= k;
    }
}
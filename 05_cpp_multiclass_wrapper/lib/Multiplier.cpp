#include "Multiplier.hpp"
#include "Vector.hpp"

Multiplier::Multiplier(double k) {
    _k = k;
}

Multiplier::~Multiplier() { } 

Vector Multiplier::multiply(Vector& vec) {
    unsigned int length = vec.get_length();
    double* in_data = vec.get_data();
    double* out_data = new double[length];

    for (int i = 0; i < length; ++i) {
        out_data[i] = in_data[i] * _k;
    }

    return Vector(out_data, length);
}
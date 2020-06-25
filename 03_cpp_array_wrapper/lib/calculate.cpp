#include "calculate.hpp"

void multiply(double* array, const unsigned int array_length, const double multiplier) {
    for (int i = 0; i < array_length; ++i) {
        array[i] *= multiplier;
    }
}

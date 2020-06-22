#include "calculate.hpp"

void multiply(double* array, const double k, const unsigned int n) {
    for (int i = 0; i < n; ++i) {
        array[i] *= k;
    }
}

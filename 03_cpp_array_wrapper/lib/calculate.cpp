#include <vector>
#include <algorithm>
#include "calculate.hpp"

void multiply(double* array, const unsigned int array_length, const double multiplier) {
    for (int i = 0; i < array_length; ++i) {
        array[i] *= multiplier;
    }
}

void divide(std::vector<double>& vec, const double divisor) {
    std::transform(
        vec.begin(), vec.end(), vec.begin(), 
        [&divisor](auto& x){ 
            return x / divisor; 
        }
    ); 
}

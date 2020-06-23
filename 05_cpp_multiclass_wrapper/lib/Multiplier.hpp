#ifndef MULTIPLIER_HPP
#define MULTIPLIER_HPP

#include "Vector.hpp"

class Multiplier {
    private:
        double _k;

    public:
        Multiplier(double k);
        ~Multiplier();

        Vector multiply(Vector& vec);
};

#endif
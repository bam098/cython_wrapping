#include <opencv2/opencv.hpp>
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

double Vector::multiply(double* other_array, const unsigned int other_array_length) {
    cv::Mat array_as_mat(1, _length, CV_64FC1, _data);
    cv::Mat other_array_as_mat(1, other_array_length, CV_64FC1, other_array);

    return array_as_mat.dot(other_array_as_mat);
}
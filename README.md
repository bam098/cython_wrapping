# Cython Wrapping

A collection of examples to wrap C++-Code using Cython to be able to use it within Python.

## Prerequisites

Cython, [Cython on PyPi](https://pypi.org/project/Cython/)

## 01 Simple C Wrapper

Wrapping a function in C that takes a string and prints that string on the console.

*References:*

- [Wrapping C libraries with Cython](https://stavshamir.github.io/python/making-your-c-library-callable-from-python-by-wrapping-it-with-cython/)
- [Convert str to bytes](https://mkyong.com/python/python-3-convert-string-to-bytes/)

## 02 Simple C++ Wrapper

*References:*

- [Wrapping C libraries with Cython](https://stavshamir.github.io/python/making-your-c-library-callable-from-python-by-wrapping-it-with-cython/)
- [Convert str to bytes](https://mkyong.com/python/python-3-convert-string-to-bytes/)

Wrapping a function in C++ that takes a string and prints that string on the console.

## 03 C++ Array Wrapper

Wrapping a function in C++ that takes an array and a number and multiplies that number to each element of the array.

*References:*

- [MemoryViews in Cython](https://cython.readthedocs.io/en/latest/src/userguide/memoryviews.html)
- [Numpy in Cython](https://cython.readthedocs.io/en/latest/src/userguide/numpy_tutorial.html)

## 04 C++ Class Wrapper

Wrapping a class in C++ that encapsulates an array and provides various functions to handle that array (sum of its elements, getting array length, getting array itself, multiplying each element by a constant).

*References:*

- [From C++ to Numpy](https://stackoverflow.com/questions/43021574/cast-c-array-into-numpy-array-cython-typed-memoryview-in-cython-code)
- [From C++ to Numpy (old?)](http://gael-varoquaux.info/programming/cython-example-of-exposing-c-computed-arrays-in-python-without-data-copies.html)
- [MemoryViews in Cython](http://docs.cython.org/en/latest/src/userguide/memoryviews.html)
- [C++ in Cython](https://cython.readthedocs.io/en/latest/src/userguide/wrapping_CPlusPlus.html)

## 05 C++ MultiClass Wrapper

Wrapping multiple class in C++. Again, we have one class that encapsulates an array. Furthermore, we have another class that takes a constant as input and offers a function which takes a vector class and multiplies each element of the vector class by the constant.

*References:*

- [C++ in Cython](https://cython.readthedocs.io/en/latest/src/userguide/wrapping_CPlusPlus.html)
- [Nullary Constructor](https://stackoverflow.com/questions/55086112/initialize-class-with-only-one-static-method-no-constructor)

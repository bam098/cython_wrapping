# Cython Wrapping
A collection of examples to wrap C++-Code using Cython to be able to use it within Python.


## Prerequisites
Cython, [https://pypi.org/project/Cython/](https://pypi.org/project/Cython/)


## 01 Simple C Wrapper
Wrapping a function in C that takes a string and prints that string on the console.

*Reference:* [https://stavshamir.github.io/python/making-your-c-library-callable-from-python-by-wrapping-it-with-cython/](https://stavshamir.github.io/python/making-your-c-library-callable-from-python-by-wrapping-it-with-cython/)


## 02 Simple C++ Wrapper
Wrapping a function in C++ that takes a string and prints that string on the console.


## 03 C++ Array Wrapper
Wrapping a function in C++ that takes an array and a number and multiplies that number to each element of the array.

*Reference:* 
- [https://cython.readthedocs.io/en/latest/src/userguide/memoryviews.html](https://cython.readthedocs.io/en/latest/src/userguide/memoryviews.html)
- [https://cython.readthedocs.io/en/latest/src/userguide/numpy_tutorial.html](https://cython.readthedocs.io/en/latest/src/userguide/numpy_tutorial.html)


## 04 C++ Class Wrapper
Wrapping a class in C++ that encapsulates an array and provides various functions to handle that array (sum of its elements, getting array length, getting array itself, multiplying each element by a constant).

*Reference:* 
- [https://stackoverflow.com/questions/43021574/cast-c-array-into-numpy-array-cython-typed-memoryview-in-cython-code](https://stackoverflow.com/questions/43021574/cast-c-array-into-numpy-array-cython-typed-memoryview-in-cython-code)
- [http://gael-varoquaux.info/programming/cython-example-of-exposing-c-computed-arrays-in-python-without-data-copies.html](http://gael-varoquaux.info/programming/cython-example-of-exposing-c-computed-arrays-in-python-without-data-copies.html)
- [http://docs.cython.org/en/latest/src/userguide/memoryviews.html](http://docs.cython.org/en/latest/src/userguide/memoryviews.html)
- [https://cython.readthedocs.io/en/latest/src/userguide/wrapping_CPlusPlus.html](https://cython.readthedocs.io/en/latest/src/userguide/wrapping_CPlusPlus.html)

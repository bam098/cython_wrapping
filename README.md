# Cython Wrapping

A collection of examples to wrap C++-Code using Cython to be able to use it within Python.

## Prerequisites

1. Create a virtual Python environment (e.g. using [conda](https://docs.conda.io/projects/continuumio-conda/en/latest/user-guide/install/index.html))<br>
    <code>conda create -n wrapper Python=3.7</code><br>

2. Inside the created environment install the required packages<br>
   <code>conda activate wrapper</code><br>
   <code>conda install -c anaconda pip</code><br>
   <code>pip install -r requirements.txt</code><br>

3. Go to one of the subdirectories (e.g. <code>01_simple_c_wrapper</code>) and follow the steps
   there (stay in the <code>wrapper</code> virtual environment).<br>

The code has been tested on MacOS (10.9) and Linux (Ubuntu 18.04 LTS).

## 01 Simple C Wrapper

Wrapping a function in C that takes a string and prints that string on the console.

*References:*

- [Wrapping C libraries with Cython](https://stavshamir.github.io/python/making-your-c-library-callable-from-python-by-wrapping-it-with-cython/)
- [Convert str to bytes](https://mkyong.com/python/python-3-convert-string-to-bytes/)

## 02 Simple C++ Wrapper

Wrapping a function in C++ that takes a string and prints that string on the console.

*References:*

- [Wrapping C libraries with Cython](https://stavshamir.github.io/python/making-your-c-library-callable-from-python-by-wrapping-it-with-cython/)
- [Convert str to bytes](https://mkyong.com/python/python-3-convert-string-to-bytes/)
- [How do I check the operating system in Python?](https://stackoverflow.com/questions/8220108/how-do-i-check-the-operating-system-in-python)
- [sys.platform](https://docs.python.org/3/library/sys.html#sys.platform)
- [GCC -fPIC option](https://stackoverflow.com/questions/5311515/gcc-fpic-option)
- [cc1plus: warning: command line option “-Wstrict-prototypes” is valid for Ada/C/ObjC but not for C++](https://stackoverflow.com/questions/8106258/cc1plus-warning-command-line-option-wstrict-prototypes-is-valid-for-ada-c-o)

## 03 C++ Array Wrapper

Wrapping a function in C++ that takes an array and a number and multiplies that number to each 
element of the array.

*References:*

- [MemoryViews in Cython](https://cython.readthedocs.io/en/latest/src/userguide/memoryviews.html)
- [Numpy in Cython](https://cython.readthedocs.io/en/latest/src/userguide/numpy_tutorial.html)
- [How do I check the operating system in Python?](https://stackoverflow.com/questions/8220108/how-do-i-check-the-operating-system-in-python)
- [sys.platform](https://docs.python.org/3/library/sys.html#sys.platform)
- [GCC -fPIC option](https://stackoverflow.com/questions/5311515/gcc-fpic-option)
- [cc1plus: warning: command line option “-Wstrict-prototypes” is valid for Ada/C/ObjC but not for C++](https://stackoverflow.com/questions/8106258/cc1plus-warning-command-line-option-wstrict-prototypes-is-valid-for-ada-c-o)
- [Best way to convert numpy array to C++ vector?](https://groups.google.com/forum/#!topic/cython-users/sqeY7GO3U7k)
- [How to initialize std::vector from C-style array?](https://stackoverflow.com/questions/2434196/how-to-initialize-stdvector-from-c-style-array)
- [Getting Started With Testing in Python](https://realpython.com/python-testing/)
- [Best way to assert for numpy.array equality?](https://stackoverflow.com/questions/3302949/best-way-to-assert-for-numpy-array-equality)
- [Python test to check instance type](https://stackoverflow.com/questions/33657463/python-test-to-check-instance-type)
- [Using nose2](https://docs.nose2.io/en/latest/usage.html)

## 04 C++ Class Wrapper

Wrapping a class in C++ that encapsulates an array and provides various functions to handle that 
array (sum of its elements, getting array length, getting array itself, multiplying each element by 
a constant).

*References:*

- [From C++ to Numpy](https://stackoverflow.com/questions/43021574/cast-c-array-into-numpy-array-cython-typed-memoryview-in-cython-code)
- [From C++ to Numpy (old?)](http://gael-varoquaux.info/programming/cython-example-of-exposing-c-computed-arrays-in-python-without-data-copies.html)
- [MemoryViews in Cython](http://docs.cython.org/en/latest/src/userguide/memoryviews.html)
- [C++ in Cython](https://cython.readthedocs.io/en/latest/src/userguide/wrapping_CPlusPlus.html)
- [How do I check the operating system in Python?](https://stackoverflow.com/questions/8220108/how-do-i-check-the-operating-system-in-python)
- [sys.platform](https://docs.python.org/3/library/sys.html#sys.platform)
- [GCC -fPIC option](https://stackoverflow.com/questions/5311515/gcc-fpic-option)
- [cc1plus: warning: command line option “-Wstrict-prototypes” is valid for Ada/C/ObjC but not for C++](https://stackoverflow.com/questions/8106258/cc1plus-warning-command-line-option-wstrict-prototypes-is-valid-for-ada-c-o)
- [Getting Started With Testing in Python](https://realpython.com/python-testing/)
- [Best way to assert for numpy.array equality?](https://stackoverflow.com/questions/3302949/best-way-to-assert-for-numpy-array-equality)
- [Python test to check instance type](https://stackoverflow.com/questions/33657463/python-test-to-check-instance-type)
- [Using nose2](https://docs.nose2.io/en/latest/usage.html)

## 05 C++ MultiClass Wrapper

Wrapping multiple class in C++. Again, we have one class that encapsulates an array. Furthermore, we 
have another class that takes a constant as input and offers a function which takes a vector class 
and multiplies each element of the vector class by the constant.

*References:*

- [C++ in Cython](https://cython.readthedocs.io/en/latest/src/userguide/wrapping_CPlusPlus.html)
- [Nullary Constructor](https://stackoverflow.com/questions/55086112/initialize-class-with-only-one-static-method-no-constructor)
- [How do I check the operating system in Python?](https://stackoverflow.com/questions/8220108/how-do-i-check-the-operating-system-in-python)
- [sys.platform](https://docs.python.org/3/library/sys.html#sys.platform)
- [GCC -fPIC option](https://stackoverflow.com/questions/5311515/gcc-fpic-option)
- [cc1plus: warning: command line option “-Wstrict-prototypes” is valid for Ada/C/ObjC but not for C++](https://stackoverflow.com/questions/8106258/cc1plus-warning-command-line-option-wstrict-prototypes-is-valid-for-ada-c-o)
- [Getting Started With Testing in Python](https://realpython.com/python-testing/)
- [Best way to assert for numpy.array equality?](https://stackoverflow.com/questions/3302949/best-way-to-assert-for-numpy-array-equality)
- [Python test to check instance type](https://stackoverflow.com/questions/33657463/python-test-to-check-instance-type)
- [Using nose2](https://docs.nose2.io/en/latest/usage.html)

## 06 Wrapper Package

Creating a package called <code>pymath</code> containing a regular Python class and a Cython class 
that wraps a C++ class. The package can be installed using pip.

*ToDo:*

- Add third-party libraries

*References:*

- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
- [Creating a Python package](https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/#creating-a-python-package)
- [Choose an open source license](https://choosealicense.com/)
- [Classifiers](https://pypi.org/classifiers/)
- [How do I install a Python package with a .whl file?](https://stackoverflow.com/questions/27885397/how-do-i-install-a-python-package-with-a-whl-file?rq=1)
- [Install dependencies from setup.py](https://stackoverflow.com/questions/26900328/install-dependencies-from-setup-py)
- [install_requires vs requirements files](https://packaging.python.org/discussions/install-requires-vs-requirements/)
- [How do I check the operating system in Python?](https://stackoverflow.com/questions/8220108/how-do-i-check-the-operating-system-in-python)
- [sys.platform](https://docs.python.org/3/library/sys.html#sys.platform)
- [GCC -fPIC option](https://stackoverflow.com/questions/5311515/gcc-fpic-option)
- [cc1plus: warning: command line option “-Wstrict-prototypes” is valid for Ada/C/ObjC but not for C++](https://stackoverflow.com/questions/8106258/cc1plus-warning-command-line-option-wstrict-prototypes-is-valid-for-ada-c-o)
- [OS detecting makefile](https://stackoverflow.com/questions/714100/os-detecting-makefile)
- [Getting Started With Testing in Python](https://realpython.com/python-testing/)
- [Best way to assert for numpy.array equality?](https://stackoverflow.com/questions/3302949/best-way-to-assert-for-numpy-array-equality)
- [Python test to check instance type](https://stackoverflow.com/questions/33657463/python-test-to-check-instance-type/33657562)
- [Using nose2](https://docs.nose2.io/en/latest/usage.html)
- [What is the correct way to share package version with setup.py and the package?](https://stackoverflow.com/questions/17583443/what-is-the-correct-way-to-share-package-version-with-setup-py-and-the-package)
- [5 common patterns to version your Python package](https://milkr.io/kfei/5-common-patterns-to-version-your-Python-package)
- [Distributing Cython modules](http://docs.cython.org/en/latest/src/userguide/source_files_and_compilation.html#distributing-cython-modules)
- [How should I structure a Python package that contains Cython code](https://stackoverflow.com/questions/4505747/how-should-i-structure-a-python-package-that-contains-cython-code) 

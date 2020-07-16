import pycalculate
import numpy as np

if __name__ == '__main__':
    array = np.ones(5, dtype=np.double)

    result = pycalculate.py_multiply(array, 5.0)

    print("length: {}".format(len(result)))
    print(result)

    print()

    result = pycalculate.py_divide(result, 2.0)

    print("length: {}".format(len(result)))
    print(result)

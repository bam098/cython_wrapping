from pymath.pyvector import PyVector
from pymath.pyvectorcalculator import PyVectorCalculator
import numpy as np

if __name__ == '__main__':
    data1 = np.array([1, 3, 5, 7, 9], dtype=np.double)
    data2 = np.array([2, 4, 6, 8], dtype=np.double)

    pyvec1 = PyVector(data1)
    pyvec2 = PyVector(data2)

    print("pyvec1: {}".format(pyvec1.get_data()))
    print("pyvec2: {}".format(pyvec2.get_data()))
    print()

    print("length pyvec1: {}".format(pyvec1.get_length()))
    print("length pyvec2: {}".format(pyvec2.get_length()))
    print()

    print("sum pyvec1: {}".format(pyvec1.sum()))
    print("sum pyvec2: {}".format(pyvec2.sum()))
    print()

    pyvec1.multiply(2.0)
    print("pyvec1 * 2: {}".format(pyvec1.get_data()))
    print()

    pyveccalc = PyVectorCalculator(pyvec1, pyvec2)

    print("pyvec1 of pyveccalc: {}".format(pyveccalc.get_vec1().get_data()))
    print("pyvec2 of pyveccalc: {}".format(pyveccalc.get_vec2().get_data()))
    print()

    print("sum pyvec1 and pyvec2: {}".format(pyveccalc.sum()))
    print()

    pyveccalc.multiply(0.5)

    print("pyvec1 of pyveccalc * 0.5: {}".format(pyveccalc.get_vec1().get_data()))
    print("pyvec2 of pyveccalc * 0.5: {}".format(pyveccalc.get_vec2().get_data()))
    print()

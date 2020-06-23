import pyvector
import numpy as np

if __name__ == '__main__':
    data = np.array([1, 2, 3, 4, 5], dtype=np.double)

    multiplier = pyvector.PyMultiplier(2.0)
    result1 = multiplier.multiply(data)

    result2 = data * 2.0

    print("equal: {}".format((result1 == result2).all()))
    print(result1)
    print(result2)

import pyvector
import numpy as np

if __name__ == '__main__':
    data = np.array([1, 2, 3, 4, 5], dtype=np.double)
    vec = pyvector.PyVector(data)
    vec.multiply(2.0)

    data = vec.get_data()

    print("sum: {}".format(vec.sum()))
    print(data)

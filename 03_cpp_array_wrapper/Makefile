LIB_DIR = lib

default: pycalculate

pycalculate: setup.py pycalculate.pyx $(LIB_DIR)/libcalculate.a
	python3 setup.py build_ext --inplace && rm -f pycalculate.cpp && rm -Rf build

$(LIB_DIR)/libcalculate.a:
	make -C $(LIB_DIR) libcalculate.a

clean:
	rm *.so
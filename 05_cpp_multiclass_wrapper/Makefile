LIB_DIR = lib

default: pymultiply

pymultiply: setup.py pymultiply.pyx $(LIB_DIR)/libmultiply.a
	python3 setup.py build_ext --inplace && rm -f pymultiply.cpp && rm -Rf build

$(LIB_DIR)/libmultiply.a:
	make -C $(LIB_DIR) libmultiply.a

clean:
	rm *.so
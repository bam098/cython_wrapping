LIB_DIR = lib

default: pyhello

pyhello: setup.py pyhello.pyx $(LIB_DIR)/libhello.a
	python3 setup.py build_ext --inplace && rm -f pyhello.c && rm -Rf build

$(LIB_DIR)/libhello.a:
	make -C $(LIB_DIR) libhello.a

clean:
	rm *.cpp *.so
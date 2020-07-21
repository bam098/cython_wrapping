LIB_DIR = lib

default: pyvector

pyvector: setup.py pyvector.pyx $(LIB_DIR)/libvector.a
	python3 setup.py build_ext --inplace && rm -f pyvector.cpp && rm -Rf build

$(LIB_DIR)/libvector.a:
	make -C $(LIB_DIR) libvector.a

clean:
	rm *.so
	rm -rf __pycache__
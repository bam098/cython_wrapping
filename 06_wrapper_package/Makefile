LIB_DIR = pymath/lib

UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Darwin)
	export MACOSX_DEPLOYMENT_TARGET=10.9
endif

default: pymath

pymath: setup.py pymath/pyvector.pyx $(LIB_DIR)/libvector.a
	python3 setup.py build_ext --inplace sdist bdist_wheel && rm -f pymath/pyvector.cpp && rm -Rf build

$(LIB_DIR)/libvector.a:
	make -C $(LIB_DIR) libvector.a

clean:
	rm -f pymath/*.so
	rm -rf dist pymath.egg-info 
	rm -rf pymath/__pycache__
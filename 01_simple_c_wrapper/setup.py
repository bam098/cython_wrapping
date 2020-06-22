from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

hello_extension = Extension(
    name="pyhello",
    sources=["pyhello.pyx"],
    libraries=["hello"],
    library_dirs=["lib"],
    include_dirs=["lib"]
)

setup(
    name="pyhello",
    ext_modules=cythonize(hello_extension)
)

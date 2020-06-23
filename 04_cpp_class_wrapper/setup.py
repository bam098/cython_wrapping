from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

vector_extension = Extension(
    name="pyvector",
    sources=["pyvector.pyx"],
    libraries=["vector"],
    library_dirs=["lib"],
    include_dirs=["lib"],
    language="c++",
    extra_compile_args=['-std=c++11', "-mmacosx-version-min=10.9"],
    extra_link_args=["-stdlib=libc++", "-mmacosx-version-min=10.9"]
)

setup(
    name="pyvector",
    ext_modules=cythonize(
        vector_extension,
        compiler_directives={'language_level': "3"}
    )
)

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

hello_extension = Extension(
    name="pyhello",
    sources=["pyhello.pyx"],
    libraries=["hello"],
    library_dirs=["lib"],
    include_dirs=["lib"],
    language="c++",
    extra_compile_args=['-std=c++11', "-mmacosx-version-min=10.9"],
    extra_link_args=["-stdlib=libc++", "-mmacosx-version-min=10.9"]
)

setup(
    name="pyhello",
    ext_modules=cythonize(
        hello_extension,
        compiler_directives={'language_level': "3"}
    )
)

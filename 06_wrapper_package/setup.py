from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize

with open("README.md", "r") as fh:
    long_description = fh.read()

pyvector_extension = Extension(
    name="pymath.pyvector",
    sources=["pymath/pyvector.pyx"],
    libraries=["vector"],
    library_dirs=["pymath/lib"],
    include_dirs=["pymath/lib"],
    language="c++",
    extra_compile_args=['-std=c++11', "-mmacosx-version-min=10.9"],
    extra_link_args=["-stdlib=libc++", "-mmacosx-version-min=10.9"],
)

setup(
    name="pymath",
    version="0.0.1",
    author="bam098",
    author_email="bam098@example.com",
    description="A small math example package containing a C++ wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bam098/cython_wrapping/06_wrapper_package",
    ext_modules=cythonize(
        pyvector_extension,
        compiler_directives={'language_level': "3"}
    ),
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS"
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy>=1.16.4',
        'cython>=0.29.19'
    ]
)

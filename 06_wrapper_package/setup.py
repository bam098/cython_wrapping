from setuptools import setup, find_packages
from distutils.extension import Extension
import distutils.sysconfig
from Cython.Build import cythonize
from sys import platform

compile_args = ["-std=c++11"]
link_args = []

if platform == "linux":
    cfg_vars = distutils.sysconfig.get_config_vars()
    for key, value in cfg_vars.items():
        if type(value) == str:
            cfg_vars[key] = value.replace("-Wstrict-prototypes", "")
elif platform == "darwin":
    compile_args.append("-mmacosx-version-min=10.9")
    link_args.append("-mmacosx-version-min=10.9")
    link_args.append("-stdlib=libc++")

with open("README.md", "r") as fh:
    long_description = fh.read()

pyvector_extension = Extension(
    name="pymath.pyvector",
    sources=["pymath/pyvector.pyx"],
    libraries=["vector"],
    library_dirs=["pymath/lib"],
    include_dirs=["pymath/lib"],
    language="c++",
    extra_compile_args=compile_args,
    extra_link_args=link_args,
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
        "Operating System :: MacOS",
        "Operating System :: Unix"
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy>=1.16.4',
        'cython>=0.29.19'
    ]
)

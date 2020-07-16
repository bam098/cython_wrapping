from distutils.core import setup
from distutils.extension import Extension
import distutils.sysconfig
from Cython.Build import cythonize
from sys import platform

compile_args = ["-std=c++17"]
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

calculate_extension = Extension(
    name="pycalculate",
    sources=["pycalculate.pyx"],
    libraries=["calculate"],
    library_dirs=["lib"],
    include_dirs=["lib"],
    language="c++",
    extra_compile_args=compile_args,
    extra_link_args=link_args
)

setup(
    name="pyhello",
    ext_modules=cythonize(
        calculate_extension,
        compiler_directives={'language_level': "3"}
    )
)

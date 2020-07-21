# Wrapper Package

There are two options to build the pymath package. You can build it either without (Option A) or
with (Option B) recompiling the C++ and Cython source code. Option A will be necessary, if you don't
want to have Cython installed in your enviroment (here we installed Cython through our
<code>requirements.txt</code> file into our <code>wrapper</code> environment). Option B will be
necessary, if you change the source code or if you want to install it on Linux or on a MacOS version
other than 10.9 (requires Cython to be installed). Furthermore, if another MacOS version than 10.9
is used, the environment variable <code>MACOSX_DEPLOYMENT_TARGET</code> in the <code>Makefile</code>
need to be adapted to the used version.

Option A - To build the package without recompiling C++ and Cython source code:

1. Make sure <code>pymath/pyvector.cpp</code> exits<br>

2. Build <code>pymath</code> package<br>
   <code>make clean</code>  *(optional)*<br>
   <code>make</code><br>

Option B - To build the package with recompiling C++ and Cython source code:

1. Build C++ library<br>
    <code>cd pymath/lib</code><br>
    <code>make clean</code> *(optional)*<br>
    <code>make</code><br>
    <code>cd -</code><br>

2. Install Cython<br>
   <code>pip install cython==0.29.19</code><br>

3. Build <code>pymath</code> package<br>
   <code>make cleanall</code>  *(optional)*<br>
   <code>make</code><br>

To install the package in a new environment:

1. Create a fresh virtual environment and install <code>pymath</code> package<br>
   <code>conda deactivate</code><br>
   <code>conda create -n pymath-test Python=3.7</code><br>
   <code>conda activate pymath-test</code><br>
   <code>conda install -c anaconda pip</code><br>
   <code>pip install dist/pymath-0.0.1-cp37-cp37m-macosx_10_9_x86_64.whl</code> *(name of <code>.whl</code> file can differ)*<br>

2. Test installed <code>pymath</code> package<br>
   <code>pip install nose2==0.9.2</code><br>
   <code>nose2</code><br>

3. Remove test environment and go back to <code>wrapper</code> environment *(optional)*<br>
   <code>conda deactivate</code><br>
   <code>conda remove -n pymath-test --all</code><br>
   <code>conda activate wrapper</code><br>

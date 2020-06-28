# Wrapper Package

To build the wrapper:

1. Build C++ library<br>
    <code>cd pymath/lib</code><br>
    <code>make clean</code> *(optional)*<br>
    <code>make</code><br>
    <code>cd -</code><br>

2. Build <code>pymath</code> package<br>
   <code>make clean</code>  *(optional)*<br>
   <code>make</code><br>

3. Create a fresh virtual environment and install <code>pymath</code> package<br>
   <code>conda deactivate</code><br>
   <code>conda create -n pymath-test Python==3.7</code><br>
   <code>conda activate pymath-test</code><br>
   <code>conda install -c anaconda pip</code><br>
   <code>pip install dist/pymath-0.0.1-cp37-cp37m-macosx_10_9_x86_64.whl</code> *(name of <code>.whl</code> file can differ)*<br>

4. Test installed <code>pymath</code> package<br>
   <code>cd tests</code><br>
   <code>python test.py</code><br>

5. Go back to <code>wrapper</code> virtual environment *(optional)*<br>
   <code>cd -</code><br>
   <code>conda deactivate</code><br>
   <code>conda activate wrapper</code><br>

This has been tested for MacOS 10.9. If another MacOS version is used, the environment variable 
<code>MACOSX_DEPLOYMENT_TARGET</code> need to be adapted to the used version.

# Simple C++ Wrapper

To build the wrapper:

1. Build C++ library<br>
    <code>cd lib</code><br>
    <code>make clean</code> *(optional)*<br>
    <code>make</code><br>
    <code>cd ..</code>

2. Build Python module using Cython<br>
   <code>make clean</code> *(optional)*<br>
   <code>make</code>

3. Test Python module<br>
   <code>python test.py</code>

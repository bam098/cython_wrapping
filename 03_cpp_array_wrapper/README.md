# C++ Array Wrapper

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
   <code>nose2</code>

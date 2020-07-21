# C++ Class Wrapper

To build the wrapper:

1. Install OpenCV 4 for C++, references:<br>

   - [Install OpenCV 4 on Ubuntu 18.04](https://www.learnopencv.com/install-opencv-4-on-ubuntu-18-04/)
   - [How to install OpenCV 4 on Ubuntu](https://www.pyimagesearch.com/2018/08/15/how-to-install-opencv-4-on-ubuntu/)

2. Go to <code>vector_extension</code> in <code>setup.py</code> and add the following:<br>

   - path to the OpenCV lib folder to <code>library_dirs</code> *(default: <code>/usr/local/lib</code>)*<br> 
   - path to the OpenCV include folder to <code>include_dirs</code> *(default: <code>/usr/local/include/opencv4</code>)*<br>

3. Build C++ library<br>
   <code>cd lib</code><br>
   <code>make clean</code> *(optional)*<br>
   <code>make</code><br>
   <code>cd ..</code>

4. Build Python module using Cython<br>
   <code>make clean</code>  *(optional)*<br>
   <code>make</code>

5. Test Python module<br>
   <code>nose2</code>

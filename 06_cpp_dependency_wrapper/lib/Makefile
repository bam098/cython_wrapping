CC = g++
INC += -I/usr/local/include/opencv4

default: libvector.a

libvector.a: Vector.o
	ar rcs $@ $^

Vector.o: Vector.cpp Vector.hpp
	$(CC) -std=c++11 -c $< -fPIC $(INC) $(LIBPATH) $(LIB)

clean:
	rm *.o *.a
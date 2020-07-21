CC = g++

default: libvector.a

libvector.a: Vector.o
	ar rcs $@ $^

Vector.o: Vector.cpp Vector.hpp
	$(CC) -c $< -fPIC

clean:
	rm *.o *.a
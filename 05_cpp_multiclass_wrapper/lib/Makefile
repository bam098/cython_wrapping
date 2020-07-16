CC = g++

default: libmultiply.a

libmultiply.a: Vector.o Multiplier.o
	ar rcs $@ $^

Vector.o: Vector.cpp Vector.hpp
	$(CC) -c $<

Multiplier.o: Multiplier.cpp Multiplier.hpp
	$(CC) -c $< -fPIC

clean:
	rm *.o *.a
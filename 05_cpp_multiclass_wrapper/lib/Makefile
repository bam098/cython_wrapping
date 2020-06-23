CC = g++

default: libvector.a

libvector.a: Vector.o Multiplier.o
	ar rcs $@ $^

Vector.o: Vector.cpp Vector.hpp
	$(CC) -c $<

Multiplier.o: Multiplier.cpp Multiplier.hpp
	$(CC) -c $<

clean:
	rm *.o *.a
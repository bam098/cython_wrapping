CC = g++

default: libcalculate.a

libcalculate.a: calculate.o
	ar rcs $@ $^

calculate.o: calculate.cpp calculate.hpp
	$(CC) -c $< -fPIC

clean:
	rm *.o *.a
CC = g++

default: libhello.a

libhello.a: hello.o
	ar rcs $@ $^

hello.o: hello.cpp hello.hpp
	$(CC) -c $<

clean:
	rm *.o *.a
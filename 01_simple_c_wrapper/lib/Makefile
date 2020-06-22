CC = gcc

default: libhello.a

libhello.a: hello.o
	ar rcs $@ $^

hello.o: hello.c hello.h
	$(CC) -c $<

clean:
	rm *.o *.a
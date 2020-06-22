cdef extern from "hello.h":
    void hello(const char* name)

def py_hello(name: bytes) -> None:
    hello(name)
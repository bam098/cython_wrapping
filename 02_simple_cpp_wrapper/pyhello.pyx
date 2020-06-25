from libcpp.string cimport string

cdef extern from "hello.hpp":
    void hello(const string name)

def py_hello(name: str) -> None:
    hello(name.encode())
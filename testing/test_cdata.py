import py
from ffi import FFI
from ffi.backend_base import BackendBase

class FakeBackend(BackendBase):

    def load_library(self):
        return "fake library"

    def new_primitive_type(self, name):
        return FakePrimitiveType(name)

class FakePrimitiveType(object):

    def __init__(self, cdecl):
        self.cdecl = cdecl


def test_typeof():
    ffi = FFI(backend=FakeBackend())
    clong = ffi.typeof("signed long int")
    assert isinstance(clong, FakePrimitiveType)
    assert clong.cdecl == 'long'

def test_global_struct_instance():
    py.test.skip("in-progress")
    ffi = FFI(backend=FakeBackend())
    ffi.cdef("struct foo { int a; } globaz;")
    ffi.C.globaz

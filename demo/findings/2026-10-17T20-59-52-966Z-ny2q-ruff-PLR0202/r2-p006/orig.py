def make():
    x = 99
    class C:
        def m(cls):
            return x
        m = classmethod(m)
    return C
C = make()
print(C.m())

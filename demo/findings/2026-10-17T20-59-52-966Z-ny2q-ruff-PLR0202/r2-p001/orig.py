class C:
    f: 'm'
    def m(cls):
        return 42
    m = classmethod(m)
print(C.f.__class__)

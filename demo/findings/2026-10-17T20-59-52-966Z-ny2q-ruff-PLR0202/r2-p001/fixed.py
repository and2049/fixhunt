class C:
    f: 'm'
    @classmethod
    def m(cls):
        return 42
print(C.f.__class__)

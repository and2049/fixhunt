def make():
    x = 99
    class C:
        @classmethod
        def m(cls):
            return x
    return C
C = make()
print(C.m())

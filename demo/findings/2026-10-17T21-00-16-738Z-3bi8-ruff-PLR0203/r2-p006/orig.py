def make_class():
    x = 10
    class C:
        def get():
            nonlocal x
            return x
        get = staticmethod(get)
    return C
C = make_class()
print(C().get())

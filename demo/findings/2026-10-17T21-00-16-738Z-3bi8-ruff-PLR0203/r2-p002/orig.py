class C:
    def f():
        return 9
    def g(x=f):
        return x()
    f = staticmethod(f)
print(C().g())

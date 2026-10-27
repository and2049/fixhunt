def outer():
    class F(metaclass=abc.ABCMeta):
        def f(self): return 1
    return F
F = outer()
f = F()
print(f.f())

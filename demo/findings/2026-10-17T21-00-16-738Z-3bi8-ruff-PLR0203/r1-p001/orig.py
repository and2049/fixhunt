class C:
    def f():
        def g():
            return f
        return g
    f = staticmethod(f)

c = C()
g = c.f()
print(type(g()))

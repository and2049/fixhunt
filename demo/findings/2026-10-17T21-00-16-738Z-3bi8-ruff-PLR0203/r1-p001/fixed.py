class C:
    @staticmethod
    def f():
        def g():
            return f
        return g

c = C()
g = c.f()
print(type(g()))

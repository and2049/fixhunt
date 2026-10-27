class C:
    def make():
        return [lambda: f for _ in range(1) if (f := lambda: 42) is not None]
    make = staticmethod(make)

funcs = C.make()
print(funcs[0]())

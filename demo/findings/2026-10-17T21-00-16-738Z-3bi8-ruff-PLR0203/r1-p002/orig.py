class C:
    f = 99
    def f():
        return 'function'
    f = staticmethod(f)

print(C.f)
print(C.f())

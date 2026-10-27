class C:
    def f() -> 'return_f()':
        pass
    def return_f():
        return f
    f = staticmethod(f)

try:
    C.f()
except Exception as e:
    print(type(e).__name__, str(e))

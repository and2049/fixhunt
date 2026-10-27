class C:
    def f(x: f) -> int:
        return x
    f = staticmethod(f)
try:
    c = C()
    print(c.f(1))
except Exception as e:
    print(type(e).__name__, str(e))

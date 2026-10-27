class C:
    @staticmethod
    def f(x: f) -> int:
        return x
try:
    c = C()
    print(c.f(1))
except Exception as e:
    print(type(e).__name__, str(e))

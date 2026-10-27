class C:
    @property
    def f():
        return 42
    f = staticmethod(f)
try:
    print(C().f)
except Exception as e:
    print(type(e).__name__, str(e))

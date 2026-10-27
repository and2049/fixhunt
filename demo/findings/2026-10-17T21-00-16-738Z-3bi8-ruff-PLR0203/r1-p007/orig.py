class C:
    def fails():
        try:
            raise ValueError('bad')
        finally:
            raise RuntimeError('worse')
    fails = staticmethod(fails)

try:
    C.fails()
except Exception as e:
    print(type(e).__name__, str(e))

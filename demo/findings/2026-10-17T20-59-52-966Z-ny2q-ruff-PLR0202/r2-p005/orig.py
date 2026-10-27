class C:
    @property
    def m(cls):
        return 'prop'
    m = classmethod(m)
try:
    print(C.m)
except Exception as e:
    print(type(e).__name__, e)

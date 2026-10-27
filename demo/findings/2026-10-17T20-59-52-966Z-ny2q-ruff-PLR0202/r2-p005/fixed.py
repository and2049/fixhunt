class C:
    @classmethod
    @property
    def m(cls):
        return 'prop'
try:
    print(C.m)
except Exception as e:
    print(type(e).__name__, e)

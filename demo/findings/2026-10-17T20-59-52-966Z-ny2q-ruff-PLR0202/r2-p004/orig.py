class C:
    def m(cls):
        """doc"""
        return __doc__
    m = classmethod(m)
print(C.m())

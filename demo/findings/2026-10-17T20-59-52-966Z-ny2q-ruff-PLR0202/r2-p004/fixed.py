class C:
    @classmethod
    def m(cls):
        """doc"""
        return __doc__
print(C.m())

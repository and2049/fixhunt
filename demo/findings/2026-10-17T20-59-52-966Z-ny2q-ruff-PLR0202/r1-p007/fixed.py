class C:
    @classmethod
    def m(cls): return 'exported'
    __all__ = ['m']

# Simulate star import: check what's in __all__
print('C.__all__:', C.__all__)
print('hasattr C.m:', hasattr(C, 'm'))
print('C.m():', C.m())

class C:
    def m(cls): return 'exported'
    m = classmethod(m)
    __all__ = ['m']

# Simulate star import: check what's in __all__
print('C.__all__:', C.__all__)
print('hasattr C.m:', hasattr(C, 'm'))
print('C.m():', C.m())

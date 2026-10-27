class C:
    def f():
        return 'original'
    orig = f
    f = staticmethod(f)
print('orig:', orig())
print('f:', C().f())
print('same?', orig is C.__dict__['f'])

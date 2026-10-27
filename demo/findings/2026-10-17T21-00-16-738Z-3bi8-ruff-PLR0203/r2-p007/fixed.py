class C:
    @staticmethod
    def f():
        return 'original'
    orig = f
print('orig:', orig())
print('f:', C().f())
print('same?', orig is C.__dict__['f'])

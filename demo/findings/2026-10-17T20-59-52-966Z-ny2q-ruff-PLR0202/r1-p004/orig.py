class C:
    def m(cls):
        '''This is a docstring'''
        return 42
    m = classmethod(m)

print('C.m.__doc__:', repr(C.m.__doc__))
print('C.m():', C.m())

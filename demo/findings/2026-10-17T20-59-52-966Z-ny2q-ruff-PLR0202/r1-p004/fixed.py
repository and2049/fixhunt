class C:
    @classmethod
    def m(cls):
        '''This is a docstring'''
        return 42

print('C.m.__doc__:', repr(C.m.__doc__))
print('C.m():', C.m())

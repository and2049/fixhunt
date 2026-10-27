class C:
    def m(cls): return 42
    m = classmethod(m)
    n = m  # alias to original function

try:
    print('n:', n)  # should be function
    print('n():', n())  # fails: missing cls
    print('C.m():', C.m())  # works: 42
    print('C.n():', C.n())  # after fix: would fail if n is descriptor
    
except Exception as e:
    print(type(e).__name__, ':', e)

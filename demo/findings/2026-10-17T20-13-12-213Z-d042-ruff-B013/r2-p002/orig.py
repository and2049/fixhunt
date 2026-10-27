class D:
    def __get__(self, obj, objtype=None):
        return 'descriptor'
class C:
    x = D()
c = C()
try:
    c.x  # triggers descriptor
    raise KeyError
except (KeyError,):
    print(c.x)

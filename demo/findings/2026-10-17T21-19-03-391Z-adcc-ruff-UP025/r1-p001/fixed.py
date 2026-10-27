class D:
    def __init__(self):
        self.val = None
    def __get__(self, obj, owner):
        return getattr(obj, '_d', 'test')

class C:
    d = D()
    def __init__(self):
        self._d = None

c = C()
print(c.d)
c._d = 'changed'
print(c.d)

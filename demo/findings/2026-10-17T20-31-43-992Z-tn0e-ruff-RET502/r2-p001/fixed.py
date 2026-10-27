class C:
    @property
    def val(self):
        if self._x > 0:
            return None
        return self._x

    def __init__(self, x):
        self._x = x

c = C(5)
print(c.val)
c._x = -1
print(c.val)

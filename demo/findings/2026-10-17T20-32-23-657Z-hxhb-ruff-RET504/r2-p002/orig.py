class C:
    @property
    def value(self):
        return self._v
    @value.setter
    def value(self, v):
        self._v = v * 2

def f():
    c = C()
    c.value = 5
    return c.value

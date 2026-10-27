class C:
    def __init__(self):
        self._v = 0
        self.count = 0
    @property
    def v(self):
        return self._v
    @v.setter
    def v(self, val):
        self._v = val
        self.count += 1
c = C()
_.v = c.v if not False else 5
print(c.count)

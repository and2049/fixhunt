class Container:
    def __init__(self):
        self._lst = [1, 2, 3]
    @property
    def lst(self):
        return self._lst
    @lst.setter
    def lst(self, v):
        self._lst = v
c = Container()
c.lst = c.lst[::-1]
print(c._lst)

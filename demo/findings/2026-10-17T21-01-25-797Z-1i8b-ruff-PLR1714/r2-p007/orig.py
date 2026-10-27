class C:
    def __init__(self):
        self._x = 0
    @property
    def x(self):
        self._x += 1
        return self._x

c = C()
if c.x == 1 or c.x == 2:
    print(c._x)
else:
    print('none')

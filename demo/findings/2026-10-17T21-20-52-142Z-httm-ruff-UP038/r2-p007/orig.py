class A:
    attr = 1
    @property
    def prop(self):
        return self._val
    def __init__(self):
        self._val = 2
a = A()
isinstance(a.attr, (int,))
isinstance(a.prop, (int,))

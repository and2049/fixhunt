class C:
    attr = 'class'
    @property
    def prop(self): return self._prop
    @prop.setter
    def prop(self, v): self._prop = v.upper()
c = C()
c.prop = 'set'
try:
    assert c.prop == 'SET', print(c.attr)
except AssertionError as e:
    print(type(e).__name__, ':', e)
else:
    print('no raise')

class C:
    @property
    def val(self):
        return self._v
    def __init__(self):
        try:
            self._v = 5
            raise ValueError('oops')
        except ValueError as exc:
            self._v = exc
            raise exc
c = C()
try:
    _ = c.val
except ValueError as e:
    print('caught:', e)

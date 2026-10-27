class C:
    @property
    def val(self):
        self._seen = True
        return 42
def f():
    c = C()
    _ = c.val
    return None
f()
c = C()
print(hasattr(c, '_seen'))

class A:
    _val = None
    @property
    def x(self):
        if self._val is None:
            self._val = [len(self.__dict__)]  # side effect: capture size
        return self._val

a = A()
print('first access:', a.x or [1])  # triggers property, returns [0]
print('second access:', a.x or [1])  # returns [1] (cached)

# If rewritten to `[1]`, property never called, _val remains None,
# and all results are [1] regardless of state

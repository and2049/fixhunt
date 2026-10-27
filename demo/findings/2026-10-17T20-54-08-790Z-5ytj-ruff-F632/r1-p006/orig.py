class Container:
    def __init__(self):
        self._data = None
    @property
    def data(self):
        return [] if self._data is None else self._data
    def set_data(self, val):
        self._data = val
c = Container()
print(c.data is [])   # Always False (new list each time)
print(c.data == [])   # True → fix changes behavior
# Before: identity → False; after: equality → True

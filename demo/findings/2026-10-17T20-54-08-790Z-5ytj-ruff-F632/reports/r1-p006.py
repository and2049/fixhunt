class Container:
    def __init__(self):
        self._data = None
    @property
    def data(self):
        return [] if self._data is None else self._data
c = Container()
print(c.data is [])   # Always False (new list each time)

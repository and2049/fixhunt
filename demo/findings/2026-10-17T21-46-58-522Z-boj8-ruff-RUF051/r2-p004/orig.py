class Store:
    def __init__(self):
        self._log = []
        self._data = {'a': 1}
    @property
    def container(self):
        return self._data
    def __delitem__(self, key):
        self._log.append(f'del {key}')
        super().__delitem__(key)
s = Store()
if 'a' in s.container:
    del s.container['a']
print('log:', s._log)
print('data:', s._data)

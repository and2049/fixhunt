class MaybeDict:
    def __init__(self, fail_on_keys=False):
        self.fail_on_keys = fail_on_keys
        self._data = {'a': 1}
    def __getattr__(self, name):
        if name == 'keys' and self.fail_on_keys:
            raise AttributeError('keys failed')
        if name == 'values':
            return self._data.values()
        if name == 'items':
            return self._data.items()
        raise AttributeError(name)

obj = MaybeDict(fail_on_keys=True)
print('Testing zip...')
try:
    list(zip(obj.keys(), obj.values()))
except AttributeError as e:
    print('Zip error:', str(e))
obj2 = MaybeDict(fail_on_keys=False)
print('Testing items...')
try:
    list(obj2.items())
except AttributeError as e:
    print('Items error:', str(e))

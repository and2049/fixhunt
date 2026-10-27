class CustomDict(dict):
    def get(self, key, default):
        if default is None:
            return self.__missing__(key)
        return super().get(key, default)
    def __missing__(self, key):
        return f'missing:{key}'

cd = CustomDict({'a': 1})
print(cd.get('b', None))  # Should log missing via __missing__
cd['b'] = 2
print(cd.get('b', None))  # Now returns 2

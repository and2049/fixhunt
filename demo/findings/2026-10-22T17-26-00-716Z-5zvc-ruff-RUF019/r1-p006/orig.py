class SillyDict(dict):
    def __missing__(self, key):
        return 'default'
    def get(self, key, default=None):
        return 'overridden'
d = SillyDict({'a': 1})
print("in+get:", 'a' in d and d.get('a'))
print("direct get:", d.get('a'))

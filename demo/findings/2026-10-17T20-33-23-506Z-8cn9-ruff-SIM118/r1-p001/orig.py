class BadDict:
    def keys(self):
        return ['a', 'b']
    def __contains__(self, item):
        return item == 'special'
d = BadDict()
print('a in d:', 'a' in d)
print('a in d.keys():', 'a' in d.keys())

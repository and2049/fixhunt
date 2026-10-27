class Desc:
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj['x']  # assumes dict-like storage

    def __set__(self, obj, value):
        obj['x'] = value  # writes to internal dict

class MyDict(dict):
    attr = Desc()

d = MyDict()
d.attr = 42
print(d.attr)
print(d['x'])

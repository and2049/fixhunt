class Map:
    def __iter__(self):
        return iter([('a', 1), ('b', 2)])
    def items(self):
        return list(self.__iter__())
d = Map()
try:
    for k, v in d.items():
        print(k)
except AttributeError as e:
    print(f'{type(e).__name__}: {e}')

class OddLen:
    def __len__(self): return 1
    def __bool__(self): return False
lst = [(None, OddLen()) for _ in range(1)]
print('list is false:', not lst)
d = dict(lst)
print('dict value is OddLen:', isinstance(d[None], OddLen))
# Dict comp version
L = [OddLen()]
d2 = dict((None, x) for x in L)
print('dict comp value:', d2[None])

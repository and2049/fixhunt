class ListLike:
    def __init__(self):
        self.data = []
        self.called = False
    def __iter__(self):
        return iter(self.data)
    def __bool__(self):
        self.called = True
        return bool(self.data)
L = ListLike()
L.data = [1, 2]
# Force list build then check truthiness
lst = [(x, x) for x in L]
print('list bool during:', bool(lst))
d = dict(lst)
print('dict from list:', d)
# Now dict comp: truthiness checked during build?
L2 = ListLike()
L2.data = [1, 2]
d2 = dict((x, x) for x in L2)
print('dict comp bool called:', L2.called)

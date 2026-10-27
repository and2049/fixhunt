class ListLike(list):
    def __iter__(self):
        return super().__iter__()
L = ListLike([1,2])
for x in list(L):
    print('copy:', x is L[0])
for x in L:
    print('direct:', x is L[0])

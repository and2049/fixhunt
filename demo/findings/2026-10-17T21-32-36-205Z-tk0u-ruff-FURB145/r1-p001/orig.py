class MyList(list):
    def __getitem__(self, key):
        return super().__getitem__(key) * 2
lst = MyList([1, 2, 3])
slice_copy = lst[:]
method_copy = lst.copy()
print('slice type:', type(slice_copy).__name__, 'values:', slice_copy)
print('method type:', type(method_copy).__name__, 'values:', method_copy)

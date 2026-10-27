class A:
    _val = 0
    @property
    def val(self):
        A._val += 1
        return self._x
    def __init__(self, x):
        self._x = x
lst = [A(1), A(2)]
sorted_lst = sorted(lst, key=lambda i: i.val)
list_wrapped = list(sorted_lst)
print('Access count via property:', A._val)
print('Sorted result:', [(i._x, i.val) for i in list_wrapped])

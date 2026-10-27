class EmptyListLike:
    def __len__(self):
        return 0
    def __bool__(self):
        return False
    def __ne__(self, other):
        return len(self) != len(other) if hasattr(other, '__len__') else True
    def __eq__(self, other):
        return len(self) == len(other) if hasattr(other, '__len__') else False

a = EmptyListLike()
b = EmptyListLike()
c = []
print('not a != b:', not a != b)
print('a == b:', a == b)
print('not a != c:', not a != c)
print('a == c:', a == c)
print('a is []:', a is [])
print('bool(a):', bool(a))
# After fix: not x != y -> x == y
print('Fixed a==b:', a == b)
print('Fixed a==c:', a == c)
assert (not a != b) == (a == b)
assert (not a != c) == (a == c)
print('Custom bool/len comparisons consistent')

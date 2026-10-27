class A:
    def __bool__(self): return False
    def __len__(self): return 1
a = A()
print('bool(a):', bool(a))
print('len(a):', len(a))
assert a, print('a is truthy?')
try:
    if not a:
        raise AssertionError('expected')
except AssertionError as e:
    print('Caught:', e)

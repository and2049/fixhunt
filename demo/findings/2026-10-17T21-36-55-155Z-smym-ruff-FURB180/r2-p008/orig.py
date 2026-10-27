class Truthy(metaclass=abc.ABCMeta):
    def __bool__(self):
        return False
    def __len__(self):
        return 5
    def __init__(self, val):
        self.val = val
obj = Truthy(10)
print(f'bool(obj): {bool(obj)}')
print(f'len(obj): {len(obj)}')
print(f'obj is None: {obj is None}')
print(f'obj == 0: {obj == 0}')
if not obj:
    print('obj is falsy')
else:
    print('obj is truthy')

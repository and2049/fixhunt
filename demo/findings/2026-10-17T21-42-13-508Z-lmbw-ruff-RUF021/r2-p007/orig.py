class Flag:
    def __init__(self, name, val):
        self.name = name
        self._val = val
    def __bool__(self):
        print(f'{self.name} accessed')
        return self._val

a = Flag('A', True)
b = Flag('B', False)
c = Flag('C', True)
res = a or b and c
print('Result:', res)

class A:
    def __bool__(self):
        print('A bool')
        return False
    def __len__(self):
        return 0
a = A()
b = []
if a or (b and True):
    print('yes')
else:
    print('no')
if a or (b and True):
    print('yes')
else:
    print('no')

class Obj:
    def __len__(self):
        return 0
    def __eq__(self, other):
        return False
a = Obj()
b = []
c = {}
if a is b and b is c:
    print('identity')
elif a == b and b == c:
    print('equality')
else:
    print(f'a={bool(a)}, b={bool(b)}, c={bool(c)}')

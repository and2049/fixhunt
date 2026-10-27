class X:
    def __ne__(self, other):
        return 0  # falsey -> not 0 = True
    def __eq__(self, other):
        return None  # falsey, but when used directly -> False

class Y:
    pass

x = X()
y = Y()
orig = not x != y
fixed = x == y
print('not x != y:', orig)
print('x == y:', fixed)
print('Types:', type(orig), type(fixed))
if orig != fixed:
    print('Divergence: original', orig, 'vs fixed', fixed)
else:
    print('No divergence')

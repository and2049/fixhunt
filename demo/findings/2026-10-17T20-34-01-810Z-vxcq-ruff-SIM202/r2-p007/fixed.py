class Nanoid(float):
    def __eq__(self, other):
        return True  # violates NaN expectations
    def __ne__(self, other):
        return not super().__eq__(other)

x = Nanoid(float('nan'))
print('x != x:', x != x)
print('not x != x:', not x != x)
print('x == x:', x == x)
# Original: not (x != x) -> not True -> False
# Fixed: x == x -> True
orig = not x != x
fixed = x == x
print('Original result:', orig)
print('Fixed result:', fixed)
if orig != fixed:
    print('Divergence due to __eq__ override')
else:
    print('Same result')

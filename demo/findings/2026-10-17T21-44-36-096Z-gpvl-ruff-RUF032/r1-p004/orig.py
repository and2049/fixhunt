a = Decimal(1.0)  # triggers
b = Decimal(2)     # does not trigger (int)
c = Decimal(True)  # does not trigger (bool, but 1.0 -> might trigger? bool is subclass of int, but Decimal(True) is allowed)
# Actually, Decimal(True) is valid and equals Decimal(1). Rule does not fire on bool because it's not a float literal.
# So adjust: use 1.0 * True -> still 1.0
val = 1.0 * True
d = Decimal(val)   # triggers because val is float 1.0
print(f'a: {a}, b: {b}, c: {c}, d: {d}')
print(f'a == d: {a == d}')  # Should be True
# After fix: d becomes Decimal('1.0') -> same value
# Test rounding context
from decimal import getcontext
getcontext().prec = 2
e = Decimal(1.0 / 3.0)  # triggers
print(f'e: {e}')
# After fix: Decimal(str(1.0/3.0)) -> Decimal('0.3333333333333333') vs original Decimal(0.3333333333333333) -> same

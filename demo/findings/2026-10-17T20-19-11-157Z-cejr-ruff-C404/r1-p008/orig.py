from decimal import Decimal, ROUND_DOWN
x = Decimal('3.5')
y = Decimal('2')
d = dict([(int(x // y), float(x / y)) for _ in [1]])
print('dict:', dict(d))

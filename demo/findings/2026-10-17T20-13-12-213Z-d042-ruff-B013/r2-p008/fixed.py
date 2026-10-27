from decimal import Decimal, getcontext
getcontext().prec = 2
try:
    x = Decimal('1') / Decimal('3')
    if x > Decimal('0.33'):
        raise TypeError
except TypeError as e:
    y = float(Decimal('2.5'))
    print(int(y), bool(y))

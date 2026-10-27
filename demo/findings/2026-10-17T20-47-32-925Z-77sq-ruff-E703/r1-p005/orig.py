from decimal import Decimal, getcontext
getcontext().prec = 3
x = Decimal('1') / Decimal('3');
print(round(float(x), 2))

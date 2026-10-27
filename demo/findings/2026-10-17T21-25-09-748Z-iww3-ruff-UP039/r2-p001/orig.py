class X():
    a = float(int(Decimal('5')) // 2)

from decimal import Decimal
print(X.a)
del X

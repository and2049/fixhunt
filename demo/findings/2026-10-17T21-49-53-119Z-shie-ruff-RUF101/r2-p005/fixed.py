from decimal import Decimal
x = Decimal(eval('10')) / Decimal('3')  # noqa: S307
print(round(x, 2))
print(float(x))
print(bool(x))

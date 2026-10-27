from decimal import Decimal
x = Decimal(eval('10')) / Decimal('3')  # noqa: PGH001
print(round(x, 2))
print(float(x))
print(bool(x))

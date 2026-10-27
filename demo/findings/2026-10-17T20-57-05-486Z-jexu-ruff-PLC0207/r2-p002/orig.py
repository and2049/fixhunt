from decimal import Decimal
s = '3.14 2.71'
parts = s.split()
a = int(parts[0])  # truncate
b = float(parts[1])  # keep
c = Decimal(parts[0]) / Decimal(parts[1])
print(a, b, round(c, 2))

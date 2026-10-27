from decimal import Decimal
x = 5
y = 5.0
z = True
d = Decimal('5')
for v in [x, y, z, d]:
    print(isinstance(v, (int, float)), type(v).__name__)

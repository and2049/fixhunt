from decimal import Decimal

d = {}
# Insert keys that collide under hash but differ as strings vs ints
d[Decimal(str(0))] = 'first'
d[Decimal(0)] = 'second'  # This overwrites because Decimal('0') == Decimal(0)
print(len(d))
for k in d:
    print(repr(k), d[k])

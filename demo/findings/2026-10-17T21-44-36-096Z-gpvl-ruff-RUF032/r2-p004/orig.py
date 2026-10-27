from decimal import Decimal
d = {}
d[Decimal(1.0 + 2.0)] = 'first'
d[Decimal('3.0')] = 'second'
print(f'Dict length: {len(d)}')
for k, v in d.items():
    print(f'key: {k!r} ({type(k)}), value: {v!r}')
s = {Decimal(1.0 + 2.0), Decimal('3.0')}
print(f'Set length: {len(s)}')

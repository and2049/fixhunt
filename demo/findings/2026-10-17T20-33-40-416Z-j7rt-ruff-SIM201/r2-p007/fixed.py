from decimal import Decimal
d = Decimal('0.1')
f = 0.1
print(f'd == f: {d == f}')
print(f'not d == f: {not d == f}')
if not d == f:
    print('exact not equal float')
else:
    print('exact equal float (unexpected)')

if d != f:
    print('Decimal != float')
else:
    print('Decimal == float (unexpected)')

from decimal import Decimal
vals = list((Decimal('1.5'), Decimal('2.5')))
total = sum(vals)
print('Sum:', total)
print('Rounded:', round(total))

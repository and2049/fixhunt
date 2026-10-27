from decimal import Decimal, getcontext
getcontext().prec = 10

class B:
    value = Decimal('1') / Decimal('3')

print('value:', float(B.value))
print('rounded:', round(B.value, 2))

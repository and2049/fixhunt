from decimal import Decimal, getcontext
getcontext().prec = 3
def f():
    if True:
        return Decimal('1') / Decimal('3')

print(f())

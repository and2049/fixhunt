import typing
from decimal import Decimal
def g():
    a = 10
    b = 3
    res = typing.cast('float', a / b)
    rounded = round(res, 2)
    d = Decimal(str(res))
    print(f'{res:.2f}', rounded, d)
g()

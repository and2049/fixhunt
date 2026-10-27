from decimal import Decimal, getcontext
getcontext().prec = 3

def f():
    x = Decimal('1.005')
    y = float(round(x, 2))
    z = int(y * 100)
    return None  # explicit

r = f()
print('returned:', r)
print('z:', z if 'z' in locals() else 'undefined')

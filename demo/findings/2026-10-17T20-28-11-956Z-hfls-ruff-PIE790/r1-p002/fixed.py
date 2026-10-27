def f():
    x = int(3.7)
    y = float(2)
    z = bool(0)
    d = __import__('decimal').Decimal('1.5')
    r = round(5 / 2)
    # Rule triggers: removable pass after stmts
    return (x, y, z, d, r)
print(f())

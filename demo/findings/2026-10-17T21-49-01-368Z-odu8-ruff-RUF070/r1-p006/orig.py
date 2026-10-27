from decimal import Decimal, getcontext
getcontext().prec = 10

def gen():
    x = Decimal('1') / Decimal('3')  # Precision-sensitive
    yield x
    # Later use in calculation (not yielded)
    y = x * 3
    # y should be 1 if precision preserved
    yield (y - 1).copy_abs()  # Should be near zero

print(list(gen()))

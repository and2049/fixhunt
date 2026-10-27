def make_decimal(*, base=str):
    def inner(val=base(0)):
        return Decimal(val)
    return inner
f = make_decimal()
print('first:', f())
print('second:', f(5))
# second call uses str(5) -> '5' -> Decimal('5'), fix would break by using 5 directly

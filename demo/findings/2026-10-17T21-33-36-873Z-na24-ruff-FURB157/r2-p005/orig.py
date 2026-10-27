def compute():
    return 1 + Decimal(str(2)) * 3  # str(2) -> '2' -> Decimal('2'), then *3 then +1
# Without str: 1 + Decimal(2) * 3 -> same due to Decimal __mul__ precedence? Actually Decimal*int is allowed.
# But: make it depend on string vs int in addition
class Dummy:
    def __add__(self, other):
        return f'add({self}, {other})'
    def __mul__(self, other):
        return f'mul({self}, {other})'
d = Dummy()
print('with str:', 1 + d * 3)  # d*3 first -> mul(d,3), then 1 + that -> add(1, mul(d,3))
# If we had str(d) it would be different, but rule doesn't apply.
# Instead: show that str() affects type in expression
print('Decimal(str(2)) * 3:', Decimal(str(2)) * 3)
print('Decimal(2) * 3:', Decimal(2) * 3)
# Same value, but if we had overloaded * for str vs int...

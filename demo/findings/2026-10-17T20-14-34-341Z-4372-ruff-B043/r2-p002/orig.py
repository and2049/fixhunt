from decimal import Decimal
class C:
    pass
x = C()
x.a = 5
delattr(x, 'a')  # triggers rule
try:
    print(x.a)
except AttributeError as e:
    print(e)

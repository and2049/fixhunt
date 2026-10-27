from decimal import Decimal
class C:
    pass
x = C()
x.a = 5
del x.a  # triggers rule
try:
    print(x.a)
except AttributeError as e:
    print(e)

from decimal import Decimal
val = 42
# User might think str(val) -> bytes, but it's str
s = str(val)
print('str(val):', repr(s), type(s))
try:
    b = s.encode('utf-8')
    print('encoded:', b)
except:
    pass
# Rule target: Decimal(str(42))
d1 = Decimal(str(42))
d2 = Decimal(42)
print('d1:', d1, 'd2:', d2, 'equal:', d1 == d2)
# If mistakenly used bytes: Decimal(b'42') would fail
try:
    Decimal(b'42')
    print('bytes worked')
except Exception as e:
    print('bytes fail:', type(e).__name__)

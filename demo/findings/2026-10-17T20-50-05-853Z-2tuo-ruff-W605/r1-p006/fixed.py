from decimal import Decimal
s = r'\.'
print(bool(s))
print(int(s, 16) if all(c in '0123456789abcdefABCDEF' for c in s.replace('\\', '')) else 'NaN')
d = Decimal('1.5')
print(d / 2)
print(round(2.5))

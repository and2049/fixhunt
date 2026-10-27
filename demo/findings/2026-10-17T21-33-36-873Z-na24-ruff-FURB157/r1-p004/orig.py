from decimal import Decimal
# str(integer) always returns ASCII digits, even if locale set
import locale
try:
    locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')
except:
    pass
s = str(42)
print('str(42) repr:', repr(s), 'is ascii:', s.isascii())
print('Decimal(str(42)):', Decimal(str(42)))
print('Decimal(42):', Decimal(42))
print('Equal?', Decimal(str(42)) == Decimal(42))

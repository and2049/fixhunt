from decimal import Decimal
val = Decimal(1.0 + 2.0)
s1 = '%s' % val
s2 = f'{val}'
s3 = str(val)
s4 = repr(val)
print(f'%s: {s1!r}, f-string: {s2!r}, str(): {s3!r}, repr(): {s4!r}')

from decimal import Decimal
seq = [Decimal('1.5'), Decimal('2.5')]
first = int(list(seq)[0])  # RUF015 trigger
print(f'first:{first}')

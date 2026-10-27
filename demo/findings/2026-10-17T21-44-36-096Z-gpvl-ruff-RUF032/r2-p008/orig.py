from decimal import Decimal
try:
    result = Decimal(1.0 + 2.0)
    print(f'Success: {result}')
except Exception as e:
    print(f'Exception: {type(e).__name__}: {e}')
else:
    print('Else block executed')
finally:
    print('Finally block executed')

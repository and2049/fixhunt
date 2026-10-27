from decimal import Decimal, InvalidOperation
try:
    d1 = Decimal(float('inf'))
    print(f'inf Decimal: {d1}')
except Exception as e:
    print(f'inf error: {type(e).__name__}: {e}')
try:
    d2 = Decimal(float('nan'))
    print(f'nan Decimal: {d2}')
except Exception as e:
    print(f'nan error: {type(e).__name__}: {e}')
print(f'Decimal("Inf"): {Decimal("Inf")}')
print(f'Decimal("NaN"): {Decimal("NaN")}')

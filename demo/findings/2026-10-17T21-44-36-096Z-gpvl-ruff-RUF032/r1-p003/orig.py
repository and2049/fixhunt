import math
inf_val = float('inf')
an_val = float('nan')
dec_inf = Decimal(inf_val)
dec_nan = Decimal(nan_val)
print(f'inf comparison: {dec_inf == Decimal("inf")}')
print(f'nan comparison: {dec_nan != dec_nan}')  # NaN != NaN
# After fix: Decimal('inf'), Decimal('nan') -> same behavior? But test if operations differ
print(f'inf + 1: {dec_inf + 1}')
print(f'nan + 1: {dec_nan + 1}')

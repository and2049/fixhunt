from decimal import Decimal
values = [1.0, 2.0, 3.0]
# Rule fires here: rewrites {int(v) for v in values} to set(map(int, values))? No - wait
# Actually rule only fires when output equals iteration variable
# So we need: {v for v in values} -> set(values)
# Hazard: if values contains floats that are equal but different types?
# Better: use Decimal and float that compare equal
vals = [Decimal('1.0'), float(1.0), True]
# Rule fires: {v for v in vals} -> set(vals)
# In set(), Decimal('1.0') == float(1.0) == True -> all hash to same value?
# Actually: Decimal and float are not equal, but True == 1
result = {v for v in vals}
print(f'Comprehension result: {result} (length: {len(result)})')
result2 = set(vals)
print(f'set() result:         {result2} (length: {len(result2)})')
# Show individual equality
print(f'Decimal("1.0") == float(1.0): {Decimal("1.0") == float(1.0)}')
print(f'float(1.0) == True:         {float(1.0) == True}')
print(f'Decimal("1.0") == True:     {Decimal("1.0") == True}' )

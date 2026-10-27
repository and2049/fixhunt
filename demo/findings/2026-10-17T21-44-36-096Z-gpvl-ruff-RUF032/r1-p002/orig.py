result = Decimal(1.0 + 2.0)
print(result)
# After fix: Decimal('3.0') instead of Decimal(3.0) -> same value but different internal handling; test via equality with string-made Decimal
print(result == Decimal('3.0'))

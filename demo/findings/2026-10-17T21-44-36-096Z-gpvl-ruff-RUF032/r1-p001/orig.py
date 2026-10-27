x = 1.5
print(type(Decimal(x)))
# After fix: Decimal(str(1.5)) -> Decimal('1.5')

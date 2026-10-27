ZERO = '0'
def get_zero():
    return ZERO
print('before fix:', Decimal(str(get_zero())))
# After fix: Decimal(get_zero()) -> Decimal('0') works, but if ZERO were int, str(ZERO) vs ZERO matters
# To show hazard: make ZERO a string that looks like int but isn't
ZERO = '0x0'
print('after reassignment:', Decimal(str(ZERO)))
# Fix would do Decimal(ZERO) -> invalid literal

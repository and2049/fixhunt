from decimal import Decimal, getcontext
getcontext().traps[Decimal.InvalidOperation] = 0
# Create sNaN via operation that differs by construction
try:
    inf1 = Decimal('inf')  # via float
    inf2 = Decimal('inf')         # direct string
    diff = inf1 - inf2
    print('inf1 - inf2:', diff, 'is_nan:', diff.is_nan())
    if diff.is_nan():
        print('  signaling:', diff.is_snan())
except Exception as e:
    print(type(e).__name__, str(e))
# Reset context
getcontext().traps[Decimal.InvalidOperation] = 1

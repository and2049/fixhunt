from decimal import Decimal
s = 'infinity'  # Not canonical
try:
    v = Decimal(float(s))
    print('float(s) works:', v)
except Exception as e:
    print('float(s) fail:', type(e).__name__, str(e))
try:
    v = Decimal(s)  # Direct string
    print('Decimal(s):', v)
except Exception as e:
    print('Decimal(s) fail:', type(e).__name__, str(e))
# Show rule would incorrectly fire if s were 'infinity' (but it doesn't, per spec)
print("Rule only fires on 'inf','-inf','nan' variants")

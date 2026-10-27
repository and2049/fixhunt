# Hazard refers to Python 2 behavior; this version intentionally avoids triggering the rule.
# Using explicit inheritance to avoid being a candidate for UP039 while still illustrating concept.
try:
    class Z(object): pass
    print(type(Z))
except Exception as e:
    print(f'{type(e).__name__}: {e}')

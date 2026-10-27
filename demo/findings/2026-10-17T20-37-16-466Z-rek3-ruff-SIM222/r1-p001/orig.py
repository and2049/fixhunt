def f(/, a, *, b=None):
    return a, b

def g(x, /, *, y=None, **kw):
    return f(x, b=(y or [1]), **kw)

# Test: y=None triggers fallback to [1]
try:
    r = g(10)
except Exception as e:
    print('error:', type(e).__name__, str(e))
else:
    print('g(10):', r)

# Now simulate rule rewrite: (y or [1]) -> [1] always
# This breaks fallback when y is provided
print('g(10, y=[]):', g(10, y=[]))  # Should use [], but rewrite forces [1]

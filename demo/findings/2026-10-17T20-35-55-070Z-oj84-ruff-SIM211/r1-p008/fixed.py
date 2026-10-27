from decimal import Decimal

# Test values that are falsy/truthy and see how 'not' behaves
# All should be equivalent to conditional
vals = [0, 0.0, Decimal('0'), 1, 1.0, Decimal('1'), -0.0]
for v in vals:
    orig = False if v else True
    rewritten = not v
    print(f'Value: {v!r} ({type(v).__name__}), orig: {orig}, rewritten: {rewritten}')
    assert orig == rewritten, f'Mismatch for {v}'

# Special case: float NaN is truthy
import math
nan = float('nan')
orig_nan = False if nan else True
rewritten_nan = not nan
print(f'NaN: orig={orig_nan}, rewritten={rewritten_nan}')
assert orig_nan == rewritten_nan  # Both False because nan is truthy
print('All numeric cases equivalent')

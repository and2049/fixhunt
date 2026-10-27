def f(pos, /, kw=None, *, kw_only=False):
    return (pos, kw, kw_only)

x = True
result_before = f(1, x == True, kw_only=x == True)
print('Before:', result_before)
# After rewrite: x == True becomes x -> f(1, x, kw_only=x)
# Since x is True, both calls should behave same here.
# But if we make x something else...
x = 1
result_after = f(1, x == True, kw_only=x == True)
print('After:', result_after)

call_count = 0
def func():
    global call_count
    call_count += 1
    return True

# Type annotation: if we put == True here, rule would fire, but annotations are expressions.
# However, ruff does not lint inside type annotations? Actually it might.
# Let's use it in a default arg that is annotated.
def f(x: int = func() == True):  # Rule fires on default value
    return x

print('First call:', f())  # func() called once, returns True -> True==True -> True
print('Call count after first:', call_count)
print('Second call:', f())  # Default is pre-evaluated? No: in Python, default args are evaluated at definition time.
# So func() was called once at definition.
# Thus second call uses same default.
print('Call count after second:', call_count)
# After rewrite: default becomes func()
# So func() called at definition -> returns True -> default=True
# Same behavior in this case.
# Need where func() returns non-True.
# Redefine.

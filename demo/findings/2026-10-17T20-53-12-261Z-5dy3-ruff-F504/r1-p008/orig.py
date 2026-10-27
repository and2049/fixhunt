list = [1, 2, 3]  # shadow built-in
mapping = {'x': 'test', 'list': [4, 5]}  # list unused in format, but shadows
# Format uses only 'x', so 'list' key is superfluous
result = 'X: %(x)s' % mapping
print('Result:', result)
# After fix, mapping loses 'list' key -> list built-in accessible again?
# But we don't rely on that; instead, we show that 'list' var still shadows
try:
    x = list(range(2))  # This should fail because list is shadowed
    print('list() worked:', x)
except Exception as e:
    print('list() failed:', type(e).__name__, str(e))

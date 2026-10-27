round = lambda x, ndigits=None: x if ndigits == 0 else __builtins__.round(x, ndigits)
print('Before:', round.__name__)
x = round(5, 0)
y = 10
if isinstance(y, int):
    y = round  # shadow built-in later
z = round(3, 0)
print('x:', x, type(x))
print('z:', z, type(z))
try:
    w = round(2.5, 0)
except Exception as e:
    print('Error:', type(e).__name__, str(e))

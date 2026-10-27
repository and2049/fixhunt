from six.moves import range
range = 5
try:
    print(range(3))
except Exception as e:
    print(type(e).__name__, str(e))

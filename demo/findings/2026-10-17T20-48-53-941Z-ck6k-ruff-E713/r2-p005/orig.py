in = lambda x, y: x not in y  # shadow 'in'
print(in(1, [1,2]))  # calls our lambda
print(not 1 in [1,2])  # triggers rule; uses built-in 'in'
in = 42  # redefine later
try:
    print(in)
except Exception as e:
    print(type(e).__name__, e)

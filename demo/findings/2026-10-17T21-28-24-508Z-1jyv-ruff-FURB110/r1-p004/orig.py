funcs = []
for i in range(2):
    x = i if (x := i) else -1
    funcs.append(lambda: x)
print('ternary lambda results:', [f() for f in funcs])
# After fix: x = x or -1
funcs = []
for i in range(2):
    x = x or -1  # x from prior iteration!
    funcs.append(lambda: x)
print('or     lambda results:', [f() for f in funcs])

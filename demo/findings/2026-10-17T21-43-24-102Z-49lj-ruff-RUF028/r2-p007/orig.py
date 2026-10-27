# fmt: off
funcs = []
for i in range(3):
    if (x := i) == 0:
        pass
    funcs.append(lambda: x)
print([f() for f in funcs])

fns = []
for i in range(2):
    if (x := i) == 0:
        fns.append(lambda: isinstance(x, (int, str)))
    else:
        fns.append(lambda: isinstance(x, (int, str)))
print(fns[0]())
print(fns[1]())

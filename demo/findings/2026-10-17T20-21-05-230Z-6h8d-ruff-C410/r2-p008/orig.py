fns = []
for i in range(3):
    if (lst := list((i, i+1))) and len(lst) == 2:
        fns.append(lambda: lst[0])
print([f() for f in fns])

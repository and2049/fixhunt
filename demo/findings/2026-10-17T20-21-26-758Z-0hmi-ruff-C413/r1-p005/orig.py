funcs = []
for i in range(3):
    if (tmp := sorted([i, 0])):
        f = lambda: tmp
        funcs.append(f)
list_wrapped = list(sorted([0]))
print('Closure results:', [f() for f in funcs])
print('List wrapped:', list_wrapped)

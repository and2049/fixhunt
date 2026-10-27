d = {'a': 1}
for k, v in d.items():
    v = 99  # reassign loop var
    print(v)  # prints 99 (stale)

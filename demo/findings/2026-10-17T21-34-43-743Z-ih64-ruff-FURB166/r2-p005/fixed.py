funcs = []
for prefix in ['0b0', '0b1']:
    funcs.append(lambda: int(prefix[2:], 2))
print([f() for f in funcs])

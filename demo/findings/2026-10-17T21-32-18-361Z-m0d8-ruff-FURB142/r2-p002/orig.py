funcs = []
s = set()
for i in range(3):
    if (x := i) not in s:
        s.add(x)
        funcs.append(lambda: x)
print([f() for f in funcs])  # Should be [0,1,2] but may change if rewritten

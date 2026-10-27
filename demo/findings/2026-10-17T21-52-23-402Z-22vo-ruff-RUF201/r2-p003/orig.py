rules = ["C901"]  # max-complexity -> ignore
funcs = []
for i in range(2):
    if (n := len(rules)) > 0:
        def make_func(idx=i):
            return lambda: print(f'Complexity limit: {rules[idx]}')
        funcs.append(make_func())
for f in funcs:
    f()
# Later reassignment
rules = ["unused-variable"]
print(f'After: {rules[0] if rules else "none"}')

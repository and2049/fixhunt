keys = ['a', 'b']
# Before fix: dict.fromkeys(keys, [])
# After fix:  {k: [] for k in keys}
fns = []
for k in keys:
    fns.append(lambda: k)
# Capture current k via walrus in comprehension (simulating post-fix behavior)
d = {(k := k): [] for k in keys}  # This line is the fix target
print('Lambda results:', [f() for f in fns])
print('Dict keys:', list(d.keys()))

flags = [0, 0, 0]
# Walrus in list comprehension: each iteration should see updated flag via assignment
results = [(flag := i) or [1] for i in flags]
print('walrus results:', results)

# Simulate rewrite: (flag := i) or [1] -> [1] always
# Then results would be [[1], [1], [1]], losing the walrus assignment effect
# Also show that flag ends up as last i only if walrus runs
print('final flag:', flag)

# Lambda late-binding: each lambda should capture current value of `or` expression
funcs = [lambda: (x or [1]) for x in [0, 0, 0]]
print('lambda results:', [f() for f in funcs])

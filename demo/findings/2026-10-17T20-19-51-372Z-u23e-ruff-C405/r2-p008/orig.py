side_effects = []
def f():
    side_effects.append(len(side_effects))
    return [side_effects[-1]]
s = set(f())
print(f'Side effects log: {side_effects}')
print(f'Set from f(): {s}')
# If f() called twice due to rewrite, log would be [0,1]

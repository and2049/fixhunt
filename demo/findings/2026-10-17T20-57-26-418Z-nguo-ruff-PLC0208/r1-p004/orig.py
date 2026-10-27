effects = []
def f(x):
    effects.append(x)
    return x
for _ in {f(1), f(2)}:
    pass
print(effects)

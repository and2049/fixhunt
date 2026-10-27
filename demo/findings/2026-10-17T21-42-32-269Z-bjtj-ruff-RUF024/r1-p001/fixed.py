def f(x=dict.fromkeys(['a','b'], [])):
    x['a'].append(1)
    return x
print(f())
print(f())

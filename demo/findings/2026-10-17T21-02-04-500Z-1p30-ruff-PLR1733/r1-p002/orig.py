v = 99  # outer scope
def f(d):
    trace = []
    for k, v in d.items():  # inner v shadows outer v
        trace.append(v)     # refers to inner v (dict value)
        x = d[k]            # triggers PLR1733: would become x = v (still inner)
        trace.append(x)
    return trace
print(f({'a': 1, 'b': 2}))

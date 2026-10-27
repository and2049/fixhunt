def make_funcs():
    x = []
    funcs = [lambda: len(x) for _ in range(2)]
    x.append(1)
    return [f() for f in funcs]

print(make_funcs())

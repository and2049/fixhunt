def make_funcs():
    funcs = []
    for i in range(2):
        if (obj := type('Obj', (), {'x': i})) is not None:
            val = getattr(obj, 'x')
            funcs.append(lambda: val)
    return funcs

f1, f2 = make_funcs()
print(f1(), f2())

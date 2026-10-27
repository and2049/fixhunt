def make_funcs():
    fs = []
    for i in range(2):
        if (x := i) is not None and isinstance(x, int) or isinstance(x, str):
            fs.append(lambda: x)
    return fs
fs = make_funcs()
print([f() for f in fs])

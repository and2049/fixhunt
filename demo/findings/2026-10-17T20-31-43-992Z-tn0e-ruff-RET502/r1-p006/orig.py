def gen_vals():
    vals = []
    for i in range(3):
        if (x := i) == 1:
            return
        vals.append(x*2)
    return vals
print(gen_vals())

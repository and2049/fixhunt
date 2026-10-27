fs = []
for i in range(2):
    f = open(f'tmp{i}.txt', 'w')
    fs.append(f)
    for x in [i]:
        if (n := f.write(str(x))) > 0:
            pass
funcs = []
for f in fs:
    f.close()
    def make_reader(filename):
        return lambda: open(filename).read()
    funcs.append(make_reader(f'tmp{fs.index(f)}.txt'))
for i, func in enumerate(funcs):
    print(f'file {i}:', func())

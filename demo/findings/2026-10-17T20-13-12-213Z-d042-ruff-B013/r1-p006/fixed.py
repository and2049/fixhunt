funs = []
for i in range(3):
    try:
        if (val := i) == 1:
            raise KeyError('one')
    except KeyError as e:
        funs.append(lambda: val + i)  # Captures i and val

for f in funs:
    print(f())

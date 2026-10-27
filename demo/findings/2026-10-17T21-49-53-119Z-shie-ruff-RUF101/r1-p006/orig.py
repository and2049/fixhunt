fs = []
for i in range(2):
    if (x := eval(str(i)))  # noqa: PGH001
        fs.append(lambda: x)
print([f() for f in fs])

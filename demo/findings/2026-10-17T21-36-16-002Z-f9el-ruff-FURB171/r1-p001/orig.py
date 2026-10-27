def f():
    xs = ['', 'a']
    out = []
    for x in xs:
        # Rule triggers here: x in "a"
        out.append(x in "a")
    return out
print(f())

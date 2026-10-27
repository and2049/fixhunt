def f():
    s = None
    for x in ({} := {1, 2}):
        s.add(x) if s else s := {x}
    return len(s)
print(f())

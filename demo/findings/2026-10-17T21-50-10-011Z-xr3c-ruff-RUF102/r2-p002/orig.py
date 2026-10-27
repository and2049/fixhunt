def f(x=[]):  # noqa: ZZZ999
    x.append(1)
    return x
print(f())
print(f())

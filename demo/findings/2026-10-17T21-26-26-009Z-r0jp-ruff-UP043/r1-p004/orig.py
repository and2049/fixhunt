def f(*, g: Generator[int, None, None] = (i for i in [1])):
    return sum(g)
print(f())

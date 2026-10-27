T = eval('int')  # noqa: PGH001
def g(x: T) -> T:
    return x + 1
print(g(5))
print(T)

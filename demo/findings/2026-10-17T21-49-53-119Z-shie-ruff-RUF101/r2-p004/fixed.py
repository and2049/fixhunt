T = eval('int')  # noqa: S307
def g(x: T) -> T:
    return x + 1
print(g(5))
print(T)

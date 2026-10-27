import typing
T = typing.List[int]
def f(x):
    if isinstance(x, T):
        return len(x)
    else:
        pass
print(f([1, 2]))
print(f("hi"))

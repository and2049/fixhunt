import typing
T = list[int]
def f() -> T:
    return [1,2]
s = set(f())
print(type(s), s)

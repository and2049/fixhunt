def f(a=None):
    if a is None:
        a = []
    if TYPE_CHECKING:
        pass
    a.append(1)
    return a
print(f())
print(f())

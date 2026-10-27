import typing
def h(x):
    return typing.cast(int | str, x)
print(h(123))
print(h('abc'))

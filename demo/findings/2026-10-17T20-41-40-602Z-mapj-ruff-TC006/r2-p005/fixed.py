import typing
def i():
    name = 'Bob'
    val = typing.cast('list[int]', [len(f'{name!r}')])
    return sum(val)
print(i())

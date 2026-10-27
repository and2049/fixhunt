import typing
def bad(l=None):
    if l is None:
        l = []
    l.append(typing.cast(int, len(l)))
    return l
print(bad())
print(bad())
print(bad([]))

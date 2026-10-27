def f(lst=None):
    if lst is None:
        lst = []
    lst.extend(list(x for x in [1, 2]))
    return lst

print(f())
print(f())

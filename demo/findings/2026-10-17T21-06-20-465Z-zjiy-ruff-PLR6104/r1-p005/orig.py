def g(a, *, lst=[]):
    lst = lst + [a]  # Trigger
    return lst
print(g(1))
print(g(2))
# After fix: lst += [a] shares default list -> [1, 2]

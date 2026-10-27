def f(lst=[]):
    lst.append(1)
    return lst
g = []
for x in list(f()):
    g.append(x)
print(len(g), g)

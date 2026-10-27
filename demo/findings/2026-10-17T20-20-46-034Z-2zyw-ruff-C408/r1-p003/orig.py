dict = lambda: {'shadow': True}
x = dict()
print(x)
del dict
x = dict()
print(sorted(x.items()))

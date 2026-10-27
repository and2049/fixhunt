def f(x, container=[]):
    # Rule triggers on: not x in container
    if not x in container:
        container.append(x)
    return container.copy()
a = f(1)
b = f(2, a)
c = f(3)
print('a:', a, 'b:', b, 'c:', c)

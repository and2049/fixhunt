x = 5
def g():
    x = 'hello'
    return isinstance(x, int) or isinstance(x, str)
print(g())

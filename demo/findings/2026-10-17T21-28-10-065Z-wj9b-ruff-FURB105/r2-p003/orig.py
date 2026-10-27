print = lambda *args, **kwargs: None  # shadow
def g():
    print('', sep='')
g()
del print
print('restored:', end=' ')
print('hello')

def f(x=None, cache=[]):
    if type(x) is type(None):
        cache.append('none')
    else:
        cache.append(x)
    return cache

print('First call :', f())
print('Second call:', f(1))
print('Third call :', f())

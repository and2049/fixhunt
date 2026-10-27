def func(x, cache=[]):
    if isinstance(x, list) or isinstance(x, tuple):
        cache.append(x)
        return len(cache)
    return -1
print(func([1]))
print(func((2,)))
print(func([3]))

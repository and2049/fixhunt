import builtins
original_sorted = builtins.sorted
cache = []
def cached_sorted(*args, **kwargs):
    if not cache:
        cache.append(original_sorted(*args, **kwargs))
    return cache[0]
builtins.sorted = cached_sorted
x = [3, 1, 2]
a = list(sorted(x))
b = sorted(x)
print(a is b)

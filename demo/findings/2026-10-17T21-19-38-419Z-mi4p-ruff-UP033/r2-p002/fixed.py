import functools

cache_hits = []

@functools.cache
def func_with_mutable_default(x, lst=[]):
    lst.append(x)
    cache_hits.append(len(lst))
    return lst.copy()

print(func_with_mutable_default(1))  # [1]
print(func_with_mutable_default(2))  # [1, 2] - cached!
print(func_with_mutable_default(3))  # [1, 2, 3] - cached!
print(cache_hits)                    # Shows if args were re-evaluated

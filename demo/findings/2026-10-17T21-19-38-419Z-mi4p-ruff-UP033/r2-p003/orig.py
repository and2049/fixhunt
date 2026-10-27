import functools

def get_kw():
    return {'maxsize': None, 'typed': True}

@functools.lru_cache(**get_kw())
def func(x):
    return x * 2

print(func(5))
print(func(5))  # Should be cached
# After fix: becomes @functools.cache(**get_kw()) which is INVALID
# functools.cache doesn't accept **kwargs -> TypeError at runtime

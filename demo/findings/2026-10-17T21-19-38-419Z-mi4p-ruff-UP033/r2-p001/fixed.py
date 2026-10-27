import functools

def make_func(a, /, b, *, c=42):
    return a + b + c

@functools.cache
def wrapper(pos_only, /, norm, *, kw_only=99):
    return make_func(pos_only, norm, kw_only)

print(wrapper(1, 2))          # First call
print(wrapper(1, 2))          # Cached
wrapper(1, 2, kw_only=5)      # Different kw_only
print(wrapper(1, 2))          # Should still be cached for kw_only=99

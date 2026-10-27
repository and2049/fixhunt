import functools, decimal
@functools.lru_cache
def divide_cached(a, b):
    return round(float(a) / float(b), 4)
d = decimal.Decimal('10')
print(divide_cached(d, 3))  # Decimal -> float via float()
print(divide_cached(True, False))  # Bool division: True/False -> 1.0/0.0 -> ZeroDivisionError
print(divide_cached(5, 2))  # Should hit cache on second call
# Second call to same args should return cached value
print(divide_cached(5, 2))

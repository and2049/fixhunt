import functools
@functools.cache
def gen():
    yield 1
    yield 2
    yield 3
it = gen()
print('List from first iter:', list(it))
print('List from second iter:', list(it))  # Should be empty due to caching consuming iterator once

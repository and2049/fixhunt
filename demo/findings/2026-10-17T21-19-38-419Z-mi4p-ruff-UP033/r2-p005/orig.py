import functools

counter = 0

def get_maxsize():
    global counter
    counter += 1
    print(f'get_maxsize called {counter} times')
    return None

@functools.lru_cache(maxsize=get_maxsize())
def compute(x):
    return x ** 2

print('First call:')
print(compute(4))
print('Second call:')
print(compute(4))  # Should NOT call get_maxsize again
print(f'Total counter: {counter}')

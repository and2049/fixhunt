# Simulate module side effect via function that modifies globals
_registry = []
def register_zip_call(args):
    _registry.append(args)
    return list(zip(*args))

def foo():
    a = [1, 2]
    b = [3, 4]
    return register_zip_call((a, b))

print(foo())  # Should print [(1,3),(2,4)]
print('_registry:', _registry)

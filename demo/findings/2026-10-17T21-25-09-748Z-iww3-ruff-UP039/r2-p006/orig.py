# Placeholder for potential future syntax: class params
# Though not valid now, simulating token sensitivity
class C():
    __params__ = ()

print(hasattr(C, '__params__'))
del C

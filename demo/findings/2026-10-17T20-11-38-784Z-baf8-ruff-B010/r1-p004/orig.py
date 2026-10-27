class ModLike:
    pass
m = ModLike()
setattr(m, '__builtins__', {'len': lambda x: 42})
print('m.__builtins__["len"]([1,2,3]):', m.__builtins__['len']([1,2,3]))

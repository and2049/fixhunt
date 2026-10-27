def inspect_args(func):
    import inspect
    sig = inspect.signature(func)
    return len(sig.parameters)
@inspect_args
def wrapper(*args, **kwargs):
    print(*args, sep='')
    return args
print(wrapper(1, 2))

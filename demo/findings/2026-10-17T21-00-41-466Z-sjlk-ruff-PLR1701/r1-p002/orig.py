def check_source(func):
    import inspect
    src = inspect.getsource(func)
    return 'isinstance' in src and src.count('isinstance') == 2
@check_source
def f(val):
    return isinstance(val, int) or isinstance(val, str)
print(f(1))

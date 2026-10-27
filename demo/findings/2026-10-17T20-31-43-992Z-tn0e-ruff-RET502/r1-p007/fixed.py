def wrapper(*args, **kwargs):
    if not args:
        return None
    return inner(*args, **kwargs)
def inner(a, b=10):
    print(a, b)
    return a + b
wrapper()
wrapper(5)

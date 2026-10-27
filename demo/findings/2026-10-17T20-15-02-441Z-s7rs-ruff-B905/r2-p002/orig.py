def wrapper(f, arg):
    return f(arg)

def target(x, y=None):
    return (x, y)

a = [1, 2]
b = [3, 4]
print(wrapper(target, zip(a, b)))  # before fix: ((1, 3), (2, 4))
# After bad fix: wrapper(target, zip(a, b, strict=True)) -> wrapper gets 2 args but target expects 1 or 2
# Actually: wrapper gets (zip_obj, None) because second arg missing -> target(zip_obj, None)

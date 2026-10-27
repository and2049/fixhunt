def f(a, /, b, *, c=print, d=None):
    c(f'a={a}, b={b}, c={c.__name__ if callable(c) else c}, d={d}')

lst = [1, 2]
def wrapper(*args, **kwargs):
    return f(*args, **kwargs)

for i, x in enumerate(lst):
    # Rule triggers on lst[i] -> should become x
    wrapper(lst[i], b=x, c=print, d=lst[i])

def f(*, lst=[1, 2, 3]):
    lst = lst[::-1]
    return lst
print('first call:', f())
print('second call:', f())

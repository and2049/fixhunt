def f(a=[], b=''):
    a.append(1)
    print(f'a={len(a)}, b={repr(b)}')
f()
f()
f([])

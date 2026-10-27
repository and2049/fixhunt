def f():
    x, y, z = [], [], True
    r1 = not x is y and z
    r2 = x is not y and z
    print('Original:', r1)
    print('Rewritten form evaluates to:', r2)

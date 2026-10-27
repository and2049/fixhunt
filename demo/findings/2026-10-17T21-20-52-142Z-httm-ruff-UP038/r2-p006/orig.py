def f(x, types=(int, str)):
    print(isinstance(x, types))
f(5)
f('hello')
f([1, 2])

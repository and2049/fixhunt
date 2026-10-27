is = lambda a, b: a == b  # shadow built-in 'is'
x, y = 1, 1
result = not x is y
print('Result with shadowed is:', result)
del is  # restore built-in
result2 = not x is y
print('Result after restore:', result2)

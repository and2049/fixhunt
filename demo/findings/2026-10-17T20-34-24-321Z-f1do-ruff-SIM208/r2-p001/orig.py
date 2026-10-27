def f(arg):
    global counter
    counter += arg
    return arg
counter = 0
result = f(not (not True))
expected_calls = 2
actual_calls = counter
print(f'{expected_calls=} {actual_calls=}')

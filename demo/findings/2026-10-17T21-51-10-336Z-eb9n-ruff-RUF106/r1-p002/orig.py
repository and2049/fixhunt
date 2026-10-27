def f():
    print('side', end='')
    return 1
# Side effect in ignored expression: function call with print
a, b = f(), 2  # ruff: ignore[F841]
print(a, b)

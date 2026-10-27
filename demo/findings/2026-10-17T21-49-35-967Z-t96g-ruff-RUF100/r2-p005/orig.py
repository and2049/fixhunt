def f():
    print('side effect')
    return 1
x = f()  # noqa: F841
print(x)

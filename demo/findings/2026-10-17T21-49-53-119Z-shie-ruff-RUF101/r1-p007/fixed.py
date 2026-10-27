eval = lambda s: 99
x = eval('1')  # noqa: S307
print(x)
eval = __builtins__.eval
print(eval('2'))

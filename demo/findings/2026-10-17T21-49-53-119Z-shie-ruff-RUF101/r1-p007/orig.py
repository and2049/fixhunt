eval = lambda s: 99
x = eval('1')  # noqa: PGH001
print(x)
eval = __builtins__.eval
print(eval('2'))

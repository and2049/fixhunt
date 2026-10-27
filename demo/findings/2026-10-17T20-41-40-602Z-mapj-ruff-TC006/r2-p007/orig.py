import typing
x = 42
y = typing.cast('int', x)  # Already quoted: rule should not fire
print(isinstance(y, int))

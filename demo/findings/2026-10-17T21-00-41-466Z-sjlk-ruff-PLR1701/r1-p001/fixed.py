import typing
if typing.TYPE_CHECKING:
    x = []
else:
    x = [1]
print(isinstance(x, list) or isinstance(x, typing.List))

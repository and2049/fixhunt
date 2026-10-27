import typing
x = []  # type: list[int]  #
if hasattr(typing, 'List'):
    y = typing.List[int]  # type: ignore  #
x.append(1)
try:
    z = x[0]
    print('value:', z)
except Exception as e:
    print(type(e).__name__, str(e))

import typing
f = lambda: [] if typing.TYPE_CHECKING else [print(1)]
try:
    f()
except SyntaxError as e:
    print(f'SyntaxError: {e}')

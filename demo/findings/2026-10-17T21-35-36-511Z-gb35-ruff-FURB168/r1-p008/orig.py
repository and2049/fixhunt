def func(x: int) -> None:
    pass
if isinstance(func.__annotations__['return'], type(None)):
    print('returns none')
else:
    print('returns something else')

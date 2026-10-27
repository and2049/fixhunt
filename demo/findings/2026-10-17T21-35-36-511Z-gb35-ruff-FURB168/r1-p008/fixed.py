def func(x: int) -> None:
    pass
if func.__annotations__['return'] is None:
    print('returns none')
else:
    print('returns something else')

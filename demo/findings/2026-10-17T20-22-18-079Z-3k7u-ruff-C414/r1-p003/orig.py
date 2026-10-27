def make_list():
    print('make_list called')
    return [1, 2]
ALL_ITEMS = list(tuple(make_list()))
print(f'ALL_ITEMS: {ALL_ITEMS}')
__all__ = ['ALL_ITEMS']
print(f'__all__: {__all__}')

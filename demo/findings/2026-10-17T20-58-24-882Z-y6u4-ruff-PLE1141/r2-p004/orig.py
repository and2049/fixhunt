pairs = [('a', 1), ('b', 2)]
print('Iterating pairs directly:')
for k, v in pairs:  # Rule fires: pairs is list, not dict
    print(f'{k}->{v}', end=' ')
print()
print('Now trying .items() on list:')
try:
    for k, v in pairs.items():  # This line would be the fix, but we show error
        pass
except AttributeError as e:
    print(f'AttributeError: {e}')

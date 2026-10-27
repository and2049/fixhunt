d = {'a': 1, 'b': 2}
d['super'] = lambda: None
try:
    d['super'].__call__()  # triggers PLW0245 -> d['super']().__call__()
except AttributeError as e:
    print(f'AttributeError: {e}')
print(len(d))

obj = type('O', (), {'x': 1})()
try:
    delattr(obj, 'x')  # triggers rule
except AttributeError as e:
    print('caught:', e)
print(hasattr(obj, 'x'))

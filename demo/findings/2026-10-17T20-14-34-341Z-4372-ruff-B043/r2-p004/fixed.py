obj = type('O', (), {'x': 1})()
try:
    del obj.x  # triggers rule
except AttributeError as e:
    print('caught:', e)
print(hasattr(obj, 'x'))

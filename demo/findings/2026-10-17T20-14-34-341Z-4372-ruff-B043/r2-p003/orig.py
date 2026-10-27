obj = type('O', (), {'foobar': 1})()
delattr(obj, 'foo' + 'bar')  # no trigger
print(hasattr(obj, 'foobar'))

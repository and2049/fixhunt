obj = type('O', (), {'foo': 42})()
delattr(obj, 'foo')  # remove foo
print('has foo:', hasattr(obj, 'foo'))

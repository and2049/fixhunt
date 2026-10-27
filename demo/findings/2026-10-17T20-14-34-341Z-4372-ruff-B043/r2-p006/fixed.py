obj = type('O', (), {'foo': 42})()
del obj.foo  # remove foo
print('has foo:', hasattr(obj, 'foo'))

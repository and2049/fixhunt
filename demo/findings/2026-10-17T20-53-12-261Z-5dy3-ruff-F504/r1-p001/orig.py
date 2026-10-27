mapping = {'x': 'keep', 'y': 'remove'}  # y unused
result = '%(x)s' % mapping
print('First:', result)
mapping['y'] = 'changed'
result = '%(x)s' % mapping
print('Second:', result)

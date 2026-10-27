value = None
result = 'value is %s' % (None if (value is None) else value)
print('Formatted:', result)

value = 42
result = 'value is {}'.format(None if (value is None) else value)
print('Formatted:', result)

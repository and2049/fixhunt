value = None
result = 'value is %s' % (None if type(value) is type(None) else value)
print('Formatted:', result)

value = 42
result = 'value is {}'.format(None if type(value) is type(None) else value)
print('Formatted:', result)

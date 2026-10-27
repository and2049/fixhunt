d = {}
try:
    d.pop('key', None)
except KeyError:
    print('This should not print')
else:
    print('No error')

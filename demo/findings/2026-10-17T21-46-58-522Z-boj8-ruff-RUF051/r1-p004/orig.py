d = {}
try:
    if 'key' in d:
        del d['key']
except KeyError:
    print('This should not print')
else:
    print('No error')

d = {'x': [1]}
ad = d
try:
    if 'x' in d and len(d.pop('x')):
        pass
except KeyError:
    print('KeyError caught')
print('d now:', d)
print('ad still has x?', 'x' in ad)

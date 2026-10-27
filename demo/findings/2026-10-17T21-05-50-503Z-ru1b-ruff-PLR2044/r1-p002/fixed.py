key = 'a'
d = {key: 1, 'b': 2}
print(len(d))
if 'a' in d:
    print(d['a'])
else:
    print('missing')
del d
key = 'a'
d = {key: 1, 'b': 2}  # real comment
print(len(d))

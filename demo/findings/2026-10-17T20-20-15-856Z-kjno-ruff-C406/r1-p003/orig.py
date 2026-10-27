def side():
    print('side')
    return [('a', 1)]
print('before')
d = dict(side())
print('after')
print('before')
d = {k: v for k, v in side()}
print('after')

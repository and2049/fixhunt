seq = []
log = lambda x: (seq.append(x), x)[1]
d = {'a': 1}
def test(): return log('default')
val = d.get('b', test())
print('result:', val, 'log:', seq)

suffix = u'_end'
results = [ (n := i) + len(suffix) for i in range(3) ]
print('results:', results)
print('final n:', n)
sufix = 'changed'  # typo intentional: suffix not rebound
lamb = lambda: len(suffix)
print('lambda result:', lamb())

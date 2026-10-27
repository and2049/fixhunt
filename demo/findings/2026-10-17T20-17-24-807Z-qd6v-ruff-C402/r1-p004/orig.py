refs = []
def make_pair(i):
    refs.append(i)
    return (i, i*10)
d = dict(make_pair(i) for i in [1,2] if (refs.append(i+100) or True))
print('refs:', refs)
print('dict:', d)

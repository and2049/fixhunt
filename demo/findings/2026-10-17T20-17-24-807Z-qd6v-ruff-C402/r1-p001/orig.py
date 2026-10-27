def check_id(obj):
    return id(obj)
gen = ((k, v) for k, v in [(1, 'a'), (2, 'b')])
d = dict(gen)
print('dict id:', check_id(d))
print('type:', type(d))
print('generator consumed?', gen.__length_hint__())

class FakeDict:
    def __contains__(self, key):
        return key == 'x'
    def __delitem__(self, key):
        raise RuntimeError('deleted')
d = FakeDict()
try:
    if 'x' in d:
        del d['x']
except RuntimeError as e:
    print('Caught:', type(e).__name__, str(e))

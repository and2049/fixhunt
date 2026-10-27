class ReadOnlyProxy:
    def __setattr__(self, name, value):
        raise AttributeError('read-only')

class Obj:
    @property
    def p(self):
        return ReadOnlyProxy()

obj = Obj()
try:
    obj.p.x = 1
except AttributeError as e:
    print('setattr error:', type(e).__name__, ':', e)
else:
    print('setattr succeeded')

try:
    obj.p.x = 1  # rewritten by autofix
except AttributeError as e:
    print('assignment error:', type(e).__name__, ':', e)
else:
    print('assignment succeeded')

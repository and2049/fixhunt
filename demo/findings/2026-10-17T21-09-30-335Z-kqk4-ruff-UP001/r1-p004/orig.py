def make_method(val=[]):
    def method(self, *, kw=val):
        return kw
    return method

class D:
    __metaclass__ = type
    method = make_method([])

D().method(kw=99)
print('default captured:', D().method())

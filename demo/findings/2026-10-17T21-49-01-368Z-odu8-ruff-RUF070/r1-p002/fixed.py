class A:
    @property
    def prop(self):
        print('prop accessed')
        return 42

def gen():
    a = A()
    x = a.prop  # Triggers property access
    yield x
    return

list(gen())  # Should print 'prop accessed' once

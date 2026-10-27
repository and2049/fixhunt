import functools
class A:
    @functools.lru_cache(maxsize=None)
    def prop(self):
        print('Prop called')
        return 42
a = A()
print('First access:', a.prop())
print('Second access:', a.prop())  # Should not re-print if cached

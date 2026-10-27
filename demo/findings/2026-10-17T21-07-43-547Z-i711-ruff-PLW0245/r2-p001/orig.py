class Meta(type):
    def __get__(cls, obj, typ=None):
        print('get', end='')
        return super
    def __call__(cls, *a, **kw):
        print('call', end='')
        return super().__call__(*a, **kw)
class A(metaclass=Meta):
    pass
try:
    A.super.method()  # triggers PLW0245 -> becomes A.super().method()
except AttributeError as e:
    print(f'AttributeError: {e}')

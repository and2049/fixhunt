class Base:
    def __init_subclass__(cls):
        raise ValueError('bad')
try:
    class C:
        pass
except ValueError as e:
    print('caught:', e)
else:
    print('no ex')
finally:
    print('finally')

class ExcSelector:
    def __get__(self, obj, owner):
        print('ExcSelector accessed')
        return IOError
class Test:
    exc = ExcSelector()
try:
    raise Test.exc('fail')
except OSError as e:
    print('caught:', e)
except OSError as e:
    print('caught OS:', e)

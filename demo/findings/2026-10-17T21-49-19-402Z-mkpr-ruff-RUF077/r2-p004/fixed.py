def bad():
    raise ValueError('bad')
class F:
    def m(self=bad()):
        try:
            return 1
        except ValueError:
            return 2
        finally:
            return 3
try:
    print(F().m())
except Exception as ex:
    print(f'{type(ex).__name__}: {ex}')

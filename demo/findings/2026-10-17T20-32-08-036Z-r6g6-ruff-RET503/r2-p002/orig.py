class Ctx:
    def __enter__(self):
        print('enter')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit:', exc_type)
        return False

def f():
    with Ctx():
        raise ValueError('fail')

try:
    f()
except ValueError as e:
    print('caught:', e)

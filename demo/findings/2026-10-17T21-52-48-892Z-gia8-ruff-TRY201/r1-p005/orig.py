import inspect
def trace_raise(func):
    src = inspect.getsource(func)
    def wrapper():
        if 'raise exc' in src:
            print('Trace: raise exc detected')
        else:
            print('Trace: raise exc NOT detected')
        return func()
    return wrapper
@trace_raise
def func():
    try:
        raise ValueError('test')
    except ValueError as exc:
        print('In handler')
        raise exc
func()

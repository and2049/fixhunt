__all__ = []

class _Hidden(object):
    value = 42

def init():
    globals().update(_Hidden.__dict__)
    __all__.append('value')

init()
print(value)

class Obj:
    pass
obj = Obj()
setattr(obj, 'foo"bar', 42)
# This line triggers B043 but rewrite will be invalid
try:
    delattr(obj, 'foo"bar')
    print('Value:', getattr(obj, 'foo"bar', 'missing'))
except AttributeError as e:
    print(f'{type(e).__name__}: {e}')

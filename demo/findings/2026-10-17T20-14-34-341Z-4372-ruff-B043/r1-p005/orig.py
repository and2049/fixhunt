class Obj:
    pass
obj = Obj()
# These attributes exist via setattr but are not valid identifiers
setattr(obj, '123', 'numeric')
setattr(obj, 'foo-bar', 'hyphenated')
try:
    val = getattr(obj, '123')
    print('getattr 123:', val)
    delattr(obj, '123')  # triggers B043
    print('After del 123:', getattr(obj, '123', 'gone'))
except AttributeError as e:
    print(f'{type(e).__name__}: {e}')

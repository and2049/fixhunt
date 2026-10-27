from __future__ import annotations
def f() -> 'List[int]':
    return [1, 2]
s = set(f())
print(f'set from annotation-resolved list: {s}')
if hasattr(f.__annotations__['return'], '__class__'):
    print('Annotation type:', f.__annotations__['return'].__class__)

from __future__ import annotations
def f() -> 'assert False':
    return 42
try:
    ann = f.__annotations__['return']
    print('annotation value:', ann)
except Exception as e:
    print('Annotation error:', type(e).__name__, str(e))

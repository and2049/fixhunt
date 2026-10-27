def f() -> 'List[int]':
    from typing import List  # used in annotation
    x = [1, 2]
    return x  # triggers PIER790 on pass
print(f())

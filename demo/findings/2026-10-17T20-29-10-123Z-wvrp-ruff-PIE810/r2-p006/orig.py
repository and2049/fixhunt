def check(s, *, prefix='a'):
    if s.startswith(prefix) or s.startswith('b'):
        return True
    return False
print(check('apple'))
print(check('banana'))

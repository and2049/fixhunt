def make_list():
    return [1, 2, 3]
def check(x, allowed=make_list()):
    before = x in allowed
    allowed_set = set(allowed)
    after  = x in allowed_set
    print(f'x={x}: before={before}, after={after}')
    return before, after
check(2)
check(4)

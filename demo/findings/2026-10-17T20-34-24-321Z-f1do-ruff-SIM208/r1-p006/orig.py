class BoolLike:
    def __init__(self, val):
        self.val = val
    def __bool__(self):
        return bool(self.val)
    def __repr__(self):
        return f'BoolLike({self.val})'

x = BoolLike(0)
forced = not (not x)
direct = x
print('forced type:', type(forced), forced)
print('direct type:', type(direct), direct)
print('are they same object?', forced is direct)

class BadAdd:
    def __init__(self):
        self.count = 0
    def __hash__(self):
        return id(self)
    def __eq__(self, other):
        return self is other
    def __repr__(self):
        return f'BadAdd({self.count})'

s = set()
bad_items = [BadAdd(), BadAdd(), BadAdd()]
bad_items[1].__hash__ = lambda: (_ for _ in ()).throw(ValueError('fail'))  # type: ignore

try:
    s.update(bad_items)
except ValueError as e:
    print(f'Caught: {e}, s={s}')

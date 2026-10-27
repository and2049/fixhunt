class Vec:
    def __init__(self, x):
        self.x = x
    def __add__(self, other):
        return Vec(self.x + other.x)
    def __iadd__(self, other):
        self.x += other.x * 2  # different behavior!
        return self
    def __repr__(self):
        return f'Vec({self.x})'

items = [Vec(1), Vec(2)]
start = Vec(0)
result_sum = sum(items, start)  # uses __add__
# After fix: reduce(iadd, items, start) uses __iadd__
print('sum result:', result_sum)
print('start after sum:', start)  # start mutated if iadd used

class Counter:
    def __init__(self):
        self.count = 0
    @property
    def value(self):
        self.count += 1
        return self.count
c = Counter()
if c.value < 3 and c.value < 5:
    print(f'count={c.count}')
else:
    print(f'count={c.count}')

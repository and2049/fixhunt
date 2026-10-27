class Show:
    def __init__(self, n): self.n = n
    def __str__(self):
        print(f'__str__ called for {self.n}')
        return str(self.n)
    __repr__ = __str__

items = [Show(1), Show(2)]
for i, x in enumerate(items):
    # Rule triggers on items[i] -> should become x
    s = f'{items[i]}:{x}'
    print(s)

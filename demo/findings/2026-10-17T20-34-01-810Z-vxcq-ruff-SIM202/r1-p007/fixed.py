class Counter:
    def __init__(self):
        self.count = 0
    @property
    def value(self):
        self.count += 1
        return 5
c = Counter()
print('before:', c.count)
expr = not c.value != 5
print('after:', c.count, 'expr:', expr)

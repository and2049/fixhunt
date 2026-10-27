class Seq:
    def __init__(self):
        self.count = 0
    @property
    def value(self):
        self.count += 1
        return [10, 20]
s = Seq()
for _ in range(2):
    first = list(s.value)[0]  # RUF015 trigger
    print(f'call:{s.count}, first:{first}')

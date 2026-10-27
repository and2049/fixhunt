class Counter:
    count = 0
    @property
    def value(self):
        self.count += 1
        return self.count

c = Counter()
def f(r=range(c.value)):
    return list(r)

print(f())
print(f())

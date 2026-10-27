class Counter:
    count = 0
    @property
    def value(self):
        Counter.count += 1
        return Counter.count > 0

obj = Counter()
if obj.value:
    print('first access:', Counter.count)
else:
    print('unreachable')
print('second access:', Counter.count)

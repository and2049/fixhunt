class C:
    def __init__(self):
        self.counter = 0
        self.s = {1, 2}
    @property
    def attr(self):
        self.counter += 1
        return self.s
obj = C()
print('Start:', obj.counter)
if 1 in obj.attr:
    obj.attr.remove(1)
print('After if-remove:', obj.counter)
# Reset counter to see second evaluation
obj.counter = 0
if 2 in obj.attr:
    obj.attr.remove(2)
print('After second if-remove:', obj.counter)

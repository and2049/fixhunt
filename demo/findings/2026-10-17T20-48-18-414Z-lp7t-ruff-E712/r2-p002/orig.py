class X:
    def __init__(self):
        self.calls = 0
    @property
    def value(self):
        self.calls += 1
        return self.calls == 1

x = X()
print('First:', x.value == True)
print('Calls after first:', x.calls)
print('Second:', x.value == True)
print('Calls after second:', x.calls)

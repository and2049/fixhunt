class DictWithSideEffect:
    def __init__(self):
        self.data = {'a': 1}
        self.calls = 0
    def keys(self):
        self.calls += 1
        print(f'keys called {self.calls}')
        return super().keys()

obj = DictWithSideEffect()
if 'a' in obj.keys():
    pass
print(f'Total keys calls: {obj.calls}')

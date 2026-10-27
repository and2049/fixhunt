class Y:
    def __init__(self):
        self.side = 0
    def __ne__(self, other):
        self.side += 1
        return not (self == other)
    def __eq__(self, other):
        return other is True

y = Y()
print('Before !=:', y.side)
result = y != True
print('After !=:', y.side, 'result:', result)
print('Not y:', not y)

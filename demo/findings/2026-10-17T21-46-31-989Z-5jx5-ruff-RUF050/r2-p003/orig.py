class BoolCounter:
    def __init__(self):
        self.count = 0
    def __bool__(self):
        self.count += 1
        return self.count < 2  # True once, then False
x = BoolCounter()
result = []
if x:
    result.append('first')
if x:  # Second eval should be False -> no append
    result.append('second')
print('bool calls:', x.count, 'results:', result)

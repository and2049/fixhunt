class Counter:
    def __init__(self):
        self.count = 0
    def __bool__(self):
        self.count += 1
        return self.count == 1

a = Counter()
result = (a == None or a == False)
print(f'a.count={a.count}, result={result}')

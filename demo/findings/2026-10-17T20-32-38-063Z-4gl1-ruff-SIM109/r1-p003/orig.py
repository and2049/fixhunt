class A:
    def __init__(self):
        self.access_count = 0
    @property
    def value(self):
        self.access_count += 1
        return self.access_count

a = A()
data = [1, 2]
result = [z for z in data if a.value == 1 or a.value == 2]
print(f'a.access_count={a.access_count}, result={result}')

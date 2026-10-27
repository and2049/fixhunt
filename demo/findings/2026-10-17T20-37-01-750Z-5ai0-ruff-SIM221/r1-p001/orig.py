class A:
    def __init__(self):
        self.count = 0
    def __getattr__(self, name):
        self.count += 1
        return 42 if name == 'x' else None

a = A()
print(a.x or not a.x)
print('count:', a.count)

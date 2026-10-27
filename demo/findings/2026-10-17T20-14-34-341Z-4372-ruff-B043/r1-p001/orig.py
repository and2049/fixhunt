class C:
    def __init__(self):
        self.x = 1
        self.y = 2
obj = C()
result = len('a') + delattr(obj, 'y') if hasattr(obj, 'y') else 0
print(result)

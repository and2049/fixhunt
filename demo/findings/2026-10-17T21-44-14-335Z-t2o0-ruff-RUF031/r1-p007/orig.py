class CustomBool:
    def __init__(self, val):
        self.val = val
    def __bool__(self):
        return self.val > 0
    def __len__(self):
        return 1 if self.val else 0
x = [CustomBool(1), CustomBool(0)]
print(bool(x[(1, 0)]))

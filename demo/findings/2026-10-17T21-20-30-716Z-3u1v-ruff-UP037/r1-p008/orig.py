class Truthy:
    def __bool__(self):
        return len(self.data) > 0
    def __init__(self):
        self.data = [1]
t = Truthy()
if t:  # Not an annotation, rule should not trigger
    print('truthy')
else:
    print('falsy')

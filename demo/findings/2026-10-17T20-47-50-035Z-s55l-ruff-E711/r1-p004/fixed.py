class OptionalInt:
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        print('eq called')
        return self.value is None and other is None
x = OptionalInt(None)
print(x == None)

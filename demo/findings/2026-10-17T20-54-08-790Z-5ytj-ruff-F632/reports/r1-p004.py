class BadDict:
    def __eq__(self, other):
        return 42
d = BadDict()
print(d is {})     # False

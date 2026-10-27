class BadDict:
    def __eq__(self, other):
        return len(other) == 0
    def __hash__(self):
        return 42
d = BadDict()
print(d is {})     # False
print(d == {})     # True after fix → triggers __eq__
# Before fix: identity check → False; after fix: equality → True (calls __eq__)

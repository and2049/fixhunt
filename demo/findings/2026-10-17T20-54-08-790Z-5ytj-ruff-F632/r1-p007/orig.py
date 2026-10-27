import sys
sys.path.insert(0, '.')
# Cannot import numpy per constraints → simulate with a mock class that mimics np.array behavior
class MockArray:
    def __init__(self, val):
        self.val = val
    def __eq__(self, other):
        return [self.val == other]  # returns list of bool → like np.array([5]) == 5 → [True]
    def __is__(self, other):
        return False  # not real, but we simulate
x = MockArray(5)
print(x is 5)   # False
print(x == 5)   # [True] → truth value of list is True → changes conditional behavior
# Before: `if x is 5:` → False
# After fix: `if x == 5:` → if [True]: → True → different branch

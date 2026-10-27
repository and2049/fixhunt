class EqCounter:
    def __init__(self, val):
        self.val = val
        self.eq_count = 0
    def __eq__(self, other):
        self.eq_count += 1
        return self.val == other
obj = EqCounter(5)
if obj == 5 or obj == 5:
    print('matched,', obj.eq_count, 'comparisons')
else:
    print('no match,', obj.eq_count, 'comparisons')

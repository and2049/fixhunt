class EqNone:
    def __eq__(self, other):
        return other is None or (isinstance(other, EqNone) and self.value == other.value)
    def __hash__(self):
        return 42  # Fixed hash to cause collision
    def __init__(self, value):
        self.value = value

# Create two distinct EqNone instances that hash to same bucket
a = EqNone(1)
b = EqNone(2)
d = {a: 'first', b: 'second'}  # Due to hash collision, second overwrites first? Actually, dict uses eq too
# But we care about == None behavior
val = EqNone(99)
if val == None:  # Rule triggers: returns False because val.value=99 != None
    print('eq_true')
else:
    print('eq_false')
# After fix: val is None -> False (same result here, but we show the path)
# To make it differ, change __eq__ to return True for None
class EqNoneTrue:
    def __eq__(self, other):
        return other is None
    def __hash__(self):
        return 0
v = EqNoneTrue()
if v == None:  # True due to __eq__
    print('eq_true_overridden')
else:
    print('eq_false_overridden')
if v is None:  # Fix would make this: False
    print('is_true_overridden')
else:
    print('is_false_overridden')

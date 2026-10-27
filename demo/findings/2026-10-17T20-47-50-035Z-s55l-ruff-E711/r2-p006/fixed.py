class FakeNone:
    def __eq__(self, other):
        return True  # Pretends to equal everything, including None
    def __ne__(self, other):
        return False

x = FakeNone()
print(f'x == None: {x == None}')  # Rule triggers: True due to __eq__
print(f'x is None: {x is None}')   # False: x is instance, not None
# After fix: 'x is None' would be False — but originally 'x == None' was True
# So behavior flips: True -> False
print(f'After fix simulation: {x is None}')

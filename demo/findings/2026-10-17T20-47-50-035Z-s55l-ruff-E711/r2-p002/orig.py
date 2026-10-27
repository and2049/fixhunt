class Proxy:
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        if other is None:
            return self.value is None
        return self.value == other
    def __is__(self, other):  # Not real, but we simulate intent
        pass
# Simulate a generic Optional-like wrapper
Maybe = Proxy
x = Maybe(None)
if x == None:  # Rule triggers: uses __eq__, returns True because value is None
    print('eq_true')
else:
    print('eq_false')
# After fix: x is None -> False, because x is a Proxy instance, not None
if x is None:
    print('is_true')
else:
    print('is_false')
